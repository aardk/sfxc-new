#! /usr/bin/env python3

# Standard Python modules
from datetime import datetime, timedelta
import json
import os
import optparse
import re
import select
import socket
import subprocess
import struct
import sys
import signal
import time
import urllib.parse as urlparse
from threading import Thread

# Qt and Qwt
from PyQt5 import Qt, QtCore, QtWidgets
import PyQt5.Qwt as Qwt

# MySQL
import MySQLdb as db

# UI
from progress import *
from weightplot import WeightPlotWindow
from fringeplot import FringePlotWindow

# JIVE Python modules
from vex import Vex
from cordata import CorrelatedData

def vex2time(str):
    tupletime = time.strptime(str, "%Yy%jd%Hh%Mm%Ss");
    return time.mktime(tupletime)

def time2vex(secs):
    tupletime = time.gmtime(secs)
    return time.strftime("%Yy%jd%Hh%Mm%Ss", tupletime)

class progressDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self)

    def abort(self):
        if self.proc:
            self.status = 'ABORT'
            try:
                self.proc.terminate()
            except:
                self.update_status()
                self.reject()
                sys.exit(1)
                pass
        else:
            self.reject()
            pass
        pass

    def debug_thread(self):
        dirname = self.debug_path + \
                  datetime.now().strftime('/sfxclog-%Y%m%dT%Hh%Mm%Ss')
        try:
            os.mkdir(dirname)
        except FileExistsError:
            pass
        args = [self.path + '/create_debug.py', '-d', dirname, self.rank_file]
        proc = subprocess.Popen(args)
        proc.wait()
        self.ui.buttonDebug.setEnabled(True)

    def create_debug(self):
        if self.proc:
            self.ui.buttonDebug.setEnabled(False)
            self.__debug_thread = Thread(target = self.debug_thread, args = ())
            self.__debug_thread.start()

    def update_status(self):
        if self.subjob == -1:
            return

        try:
            num_integrations = self.cordata.integration_slice
            branch = self.cordata.correlator_branch
            revision = self.cordata.correlator_version
            correlator_version = "%s r%d" % (branch, revision)
        except:
            num_integrations = -1
            correlator_version = ""
            pass

        conn = db.connect(host=dbhost, port=3306,
                          db="correlator_control",
                          read_default_file="~/.my.cnf")

        cursor = conn.cursor()
        cursor.execute("UPDATE data_logbook" \
                           + " SET correlator_status='%s'" % self.status \
                           + " WHERE subjob_id=%d" % self.subjob)
        cursor.execute("UPDATE data_logbook" \
                           + " SET num_integrations='%d'" % num_integrations \
                           + " WHERE subjob_id=%d" % self.subjob)
        cursor.execute("UPDATE data_logbook" \
                           + " SET correlator_version='%s'" % correlator_version \
                           + " WHERE subjob_id=%d" % self.subjob)
        cursor.close()
        conn.commit()
        conn.close()
        pass

    def update_output(self):
        if self.subjob == -1:
            return

        bins = []
        sources = []
        try:
            if self.json_input['pulsar_binning']:
                bins = [1]
                scans = self.json_input['scans']
                pulsars = self.json_input['pulsars']
                for scan in scans:
                    for source in self.vex['SCHED'][scan].getall('source'):
                        if source in pulsars:
                            bins = range(pulsars[source]['nbins'] + 1)
                            break
                        continue
                    continue
                pass
        except:
            pass
        try:
            if self.json_input['multi_phase_center']:
                scans = self.json_input['scans']
                for scan in scans:
                    for source in self.vex['SCHED'][scan].getall('source'):
                        sources.append(source)
                        continue
                    continue
                pass
        except:
            pass

        conn = db.connect(host=dbhost, port=3306,
                          db="correlator_control",
                          read_default_file="~/.my.cnf")

        cursor = conn.cursor()
        output_file = self.json_input['output_file']
        if bins:
            for bin in bins:
                output_uri = "%s.bin%d" % (output_file, bin)
                path = urlparse.urlparse(output_uri).path
                if os.path.exists(path):
                    cursor.execute("INSERT INTO data_output" \
                                   + " (subjob_id, output_uri, pulsar_bin)" \
                                   + " VALUES (%d, '%s', %d)" \
                                   % (self.subjob, output_uri, bin))
                    pass
                continue
        elif sources:
            for source in sources:
                output_uri = "%s_%s" % (output_file, source)
                path = urlparse.urlparse(output_uri).path
                if os.path.exists(path):
                    cursor.execute("INSERT INTO data_output" \
                                   + " (subjob_id, output_uri, mpc_source)" \
                                   + " VALUES (%d, '%s', '%s')" \
                                   % (self.subjob, output_uri, source))
                    pass
                continue
        else:
            output_uri = output_file
            path = urlparse.urlparse(output_uri).path
            if os.path.exists(path):
                cursor.execute("INSERT INTO data_output" \
                               + " (subjob_id, output_uri)" \
                               + " VALUES (%d, '%s')" % \
                               (self.subjob, output_uri))
                pass
        cursor.close()
        conn.commit()
        conn.close()
        pass

    def get_job(self):
        if self.subjob == -1:
            return -1

        conn = db.connect(host=dbhost, port=3306,
                          db="correlator_control",
                          read_default_file="~/.my.cnf")

        cursor = conn.cursor()
        cursor.execute("SELECT job_id FROM cj_subjob " \
                           + " WHERE subjob_id=%d" % self.subjob)
        result = cursor.fetchone()
        if result:
            return result[0]
        return -1

    def run(self, vex_file, ctrl_file, machine_file, rank_file, options):
        self.vex = Vex(vex_file)
        self.ctrl_file = ctrl_file
        self.rank_file = rank_file
        self.evlbi = options.evlbi
        self.reference = options.reference
        self.timeout_interval = options.timeout_interval
        self.path = options.path
        self.label = options.label
        self.debug_path = options.debug_path if options.debug_path != "" \
                          else os.path.split(os.path.realpath(ctrl_file))[0]

        if self.label:
            self.setWindowTitle("Progress " + self.label)
            pass

        # Default to using the SFXC binaries in $HOME/bin
        if not self.path:
            self.path = os.environ['HOME'] + "/bin"
            pass

        # Disable the watchdog for e-VLBI.  We don't want to stop the
        # correlator just because there is a longish gap.
        if self.evlbi:
            self.timeout_interval = 0
            pass

        exper = self.vex['GLOBAL']['EXPER']
        exper = self.vex['EXPER'][exper]['exper_name']
        self.exper = exper

        basename = os.path.splitext(ctrl_file)[0]
        log_file = basename + ".log"
        self.log_fp = open(log_file, 'w', 1)

        fp = open(ctrl_file, 'r')
        self.json_input = json.load(fp)
        fp.close()

        # When doing e-VLBI we don't need to generate delays for the past.
        if self.evlbi:
            if time.time() > vex2time(self.json_input['start']):
                self.json_input['start'] = time2vex(time.time())
                pass
            pass

        self.start = int(vex2time(self.json_input['start']))
        self.stop = int(vex2time(self.json_input['stop']))
        self.subjob = self.json_input.get('subjob', -1)
        self.ui.progressBar.setRange(self.start, self.stop)
        self.ui.logEdit.setMaximumBlockCount(100000)
        self.time = self.start
        self.integr_time = self.json_input['integr_time']
        self.cordata = None
        self.scans = self.json_input['scans']
        self.scan = self.scans[0]
        self.wplot = None
        self.fplot = None
        self.status = 'CRASH'

        # Make sure we skip scans before the start time of the job.
        # This can happen during e-VLBI when the operators have
        # selected a range of scans that includes scans that have
        # already been completed.
        self.scan = self.next_scan()
        self.ui.scanEdit.setText(self.scan)

        # Parse the rankfile to figure out wher the input node for
        # each station runs.
        self.stations = self.json_input['stations']
        self.input_host = {}
        fp = open(rank_file, 'r')
        r1 = re.compile(r'rank (\d*)=(.*) slot=')
        for line in fp:
            m = r1.match(line)
            if not m:
                continue
            rank = int(m.group(1))
            if rank > 2 and rank < 3 + len(self.stations):
                self.input_host[self.stations[rank - 3]] = m.group(2)
                continue
            continue
        fp.close()

        # Generate delays for this subjob.
        if not options.skip_generate_delays:
            procs = {}
            success = True
            delay_directory = self.json_input['delay_directory']
            for station in self.json_input['stations']:
                path = urlparse.urlparse(delay_directory).path
                delay_file = path + '/' +  exper + '_' + station + '.del'
                args = [self.path + '/generate_delay_model', '-a', vex_file, station,
                        delay_file, time2vex(self.start), time2vex(self.stop)]
                procs[station] = subprocess.Popen(args)
                continue
            for station in procs:
                procs[station].wait()
                if procs[station].returncode != 0:
                    msg = "Delay model couldn't be generated for " + station + "."
                    QtWidgets.QMessageBox.warning(self, "Aborted", msg)
                    path = urlparse.urlparse(self.json_input['delay_directory']).path
                    delay_file = path + '/' +  exper + '_' + station + '.del'
                    os.remove(delay_file)
                    success = False
                    pass
                continue
            if not success:
                sys.exit(1)
                pass
            pass

        # When doing e-VLBI we want to start correlating a few seconds
        # from "now", but we have to make sure we're not in a gap
        # between scans.
        if self.evlbi:
            start = time.time() + 15
            for scan in self.vex['SCHED']:
                # Loop over all the "station" parameters in the scan,
                # figuring out the real length of the scan.
                start_time = stop_time = 0
                for transfer in self.vex['SCHED'][scan].getall('station'):
                    station = transfer[0]
                    stop_time = max(stop_time, int(transfer[2].split()[0]))
                    continue

                # Figure out the real start and stop time.
                start_time += vex2time(self.vex['SCHED'][scan]['start'])
                stop_time += vex2time(self.vex['SCHED'][scan]['start'])

                start = max(start, start_time)
                if start < stop_time:
                    break
                continue

            # Write out the control file with a modified start time.
            self.json_input['start'] = time2vex(start)
            os.unlink(ctrl_file)
            fp = open(ctrl_file, 'w')
            json.dump(self.json_input, fp, indent=4)
            fp.close()
            pass

        # Parse the rankfile to calculate the number of MPI processes
        # to start.  We simply count the number of lines that start
        # with "rank".
        ranks = 0
        fp = open(rank_file, 'r')
        r1 = re.compile(r'rank')
        for line in fp:
            m = r1.match(line)
            if m:
                ranks += 1
                pass
            continue
        fp.close()

        if self.subjob != -1:
            self.ui.jobEdit.setText(str(self.get_job()))
            self.ui.subjobEdit.setText(str(self.subjob))
            pass

        sfxc = self.path + '/sfxc'
        subnet = "10.88.0.0/24"
        args = ['/home/sfxc/bin/mpirun',
                '--mca', 'btl_tcp_if_include', subnet,
                '--mca', 'oob_tcp_if_include', subnet,
                '--mca', 'orte_keep_fqdn_hostnames', '1',
                '--mca', 'orte_hetero_nodes', '1',
                '--mca', 'btl', '^openib',
                '--mca', 'oob', '^ud',
                '--machinefile', machine_file, '--rankfile', rank_file,
                '--np', str(ranks), sfxc, ctrl_file, vex_file]
        print(' '.join(args))
        self.proc = subprocess.Popen(args, universal_newlines=True, bufsize=1,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT)
        if not self.proc:
            return
        os.set_blocking(self.proc.stdout.fileno(), False)

        # Update the map-on-the-wall.
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect(("wwpad", 4004))
            command = ",".join(self.json_input['stations']) + "\n"
            s.send(command)
            s.recv(1024)
            s.close()
        except:
            pass

        self.monitor_time = time.time()
        self.monitor_pos = 0
        self.t = QtCore.QTimer()
        self.t.timeout.connect(self.timeout)
        self.t.start(500)
        pass

    def _output_file(self, start):
        output_file = urlparse.urlparse(self.json_input['output_file']).path
        try:
            if self.json_input['multi_phase_center']:
                source = None
                for scan in self.vex['SCHED']:
                    if start >= vex2time(self.vex['SCHED'][scan]['start']):
                        source = self.vex['SCHED'][scan]['source']
                        pass
                    continue
                if source:
                    output_file = output_file + '_' + source
                    pass
                pass
        except:
            pass
        try:
            if self.json_input['pulsar_binning']:
                output_file = output_file + '.bin1'
                pass
        except:
                pass
        return output_file

    def next_scan(self):
        scan = self.scan
        while True:
            stop_time = 0
            for transfer in self.vex['SCHED'][scan].getall('station'):
                stop_time = max(stop_time, int(transfer[2].split()[0]))
                continue
            stop_time += vex2time(self.vex['SCHED'][scan]['start'])

            if self.time + self.integr_time < stop_time:
                break

            index = self.scans.index(scan)
            try:
                scan = self.scans[index + 1]
            except:
                break
            continue
        return scan

    def timeout(self):
        if self.cordata:
            self.cordata.read()
            if self.time < self.cordata.current_time:
                self.time = int(self.cordata.current_time)
                tupletime = time.gmtime(self.time)
                strtime = time.strftime("%H:%M:%S", tupletime)
                self.ui.timeEdit.setText(strtime)
                self.ui.progressBar.setValue(self.time)

                next_scan = self.next_scan()
                if next_scan != self.scan:
                    self.scan = next_scan
                    self.ui.scanEdit.setText(self.scan)
                    start = vex2time(self.vex['SCHED'][next_scan]['start'])
                    output_file = self._output_file(start)
                    self.cordata.switch(output_file)
                    pass
                pass
            pass
        output = self.proc.stdout.readlines()
        if output:
            r1 = re.compile(r'Starting correlation')
            r2 = re.compile(r'Terminating nodes')
            r3 = re.compile(r'^Node #(\d+) fatal error.*Could not find header')

            for line in output:
                m = r1.search(line)
                if m:
                    if not self.cordata:
                        self.output_file = self._output_file(self.start)
                        self.cordata = CorrelatedData(self.vex, self.output_file, True)
                        if not self.wplot:
                            self.wplot = WeightPlotWindow(self.vex, [self.ctrl_file], self.cordata, True)
                            if self.label:
                                title = self.exper + " Weights " + self.label
                                self.wplot.setWindowTitle(title)
                                pass
                            self.wplot.show()
                            pass
                        if not self.fplot and self.cordata:
                            self.fplot = FringePlotWindow(self.vex, [self.ctrl_file], self.cordata, self.reference, self.evlbi)
                            if self.label:
                                title = self.exper + " Fringes " + self.label
                                self.fplot.setWindowTitle(title)
                                pass
                            self.fplot.show()
                            pass
                        self.update_output()
                        pass
                    pass
                m = r2.search(line)
                if m:
                    self.ui.progressBar.setValue(self.stop)
                    pass
                m = r3.match(line)
                if m:
                    station = self.stations[int(m.group(1)) - 3]
                    unit = None
                    r = re.compile(r'10\.88\.1\.(\d+)')
                    m = r.match(self.input_host[station])
                    if m:
                        unit = int(m.group(1)) - 200
                        pass
                    if unit != None:
                        print >>sys.stderr, "Error: Disk problem with %s in unit %d" % (station, unit)
                    else:
                        print >>sys.stderr, "Error: Disk Problem with %s" % (station)
                        pass
                    pass
                self.ui.logEdit.appendPlainText(line.rstrip())
                self.log_fp.write(line)
                continue
            pass

        # Check if SFXC process is frozen
        curtime = time.time()
        if (self.timeout_interval > 0) and (curtime - self.monitor_time > self.timeout_interval):
            self.monitor_time = curtime
            terminate = False
            if (self.cordata == None) or (self.cordata.fp == None):
                terminate = True
            else:
                newpos = self.cordata.fp.tell()
                if newpos == self.monitor_pos: 
                    terminate = True
                self.monitor_pos = newpos
            if terminate:
                print('Watchdog timeout')
                os.kill(self.proc.pid, signal.SIGTERM)
                i = 0
                while (i < 15) and (self.proc.poll() == None):
                    time.sleep(1)
                    i += 1
                if self.proc.poll() == None:
                    os.kill(self.proc.pid, signal.SIGKILL)
                self.log_fp.write('ERROR: Watchdog timeout triggered!\n')

        self.proc.poll()
        if self.proc.returncode != None:
            self.t.stop()
            self.log_fp.close()

            if self.proc.returncode == 0:
                self.status = 'DONE'
                self.update_status()
                self.accept()
                sys.exit(0)
                pass
            else:
                self.update_status()
                self.reject()
                if self.status == 'ABORT':
                    sys.exit(1)
                else:
                    sys.exit(0)
                    pass
                pass
            pass

        return

    pass

usage = "usage: %prog [options] vexfile ctrlfile machinefile rankfile"
parser = optparse.OptionParser(usage=usage)
parser.add_option("-e", "--evlbi", dest="evlbi",
                  action="store_true", default=False,
                  help="e-VLBI")
parser.add_option("-i", "--timeout-interval", dest="timeout_interval",
                  type='int', default='600',
                  help="watchdog timeout", metavar="SECS")
parser.add_option("-p", "--path", dest="path",
                  default="", type="string",
                  help="use SFXC binaries in PATH", metavar="PATH")
parser.add_option("-r", "--reference", dest="reference",
                  default="", type="string",
                  help="reference station",
                  metavar="STATION")
parser.add_option("-s", "--skip-generate-delays", dest="skip_generate_delays",
                  action="store_true", default=False,
                  help="do not generate delay files")
parser.add_option("-d", "--database-host", dest="dbhost",
                  default="db0", type="string",
                  help="Database host to use, default = db0",
                  metavar="HOST")
parser.add_option("-l", "--label", dest="label",
                  default="", type="string",
                  help="label",
                  metavar="LABEL")
parser.add_option("-D", "--debug-path", dest="debug_path",
                  default="", type="string",
                  help="Directory in which debug information is written", metavar="PATH")

(options, args) = parser.parse_args()
if len(args) != 4:
    parser.error("incorrect number of arguments")
    pass

dbhost = options.dbhost

os.environ['TZ'] = 'UTC'
time.tzset()

app = QtWidgets.QApplication(sys.argv)
d = progressDialog()
d.run(args[0], args[1], args[2], args[3], options)
d.show()
sys.exit(app.exec_())
