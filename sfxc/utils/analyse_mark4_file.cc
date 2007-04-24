/* Copyright (c) 2007 Joint Institute for VLBI in Europe (Netherlands)
 * All rights reserved.
 * 
 * Author(s): Nico Kruithof <Kruithof@JIVE.nl>, 2007
 * 
 * $Id: Buffer.h 191 2007-04-05 11:34:41Z kruithof $
 *
 */

#include <iostream>
#include <../src/InData.cc>

#include <Log_writer_cout.h>
#include <Data_reader_file.h>
#include <Channel_extractor_mark4.h>

#include <genFunctions.h>
#include <constPrms.h>

#include <utils.h>

UINT32 seed;


//*****************************************************************************
// find the header in the Mk4 type file after offset bytes and
// reset usEarliest in GemPrms if necessary
// input : station station number
// output: usTime  header time in us for requested offset
//         jsynch
//*****************************************************************************
int NGHK_FindHeaderMk4(Data_reader &reader, int& jsynch,
  INT64& usTime, INT64 usStart, StaP &StaPrms, GenP &GenPrms)
{
  int retval = 0;
  
  //buffer for unpacked tracks, NTRACKS tracks, NFRMS Mk4 frames long
  char  tracks[trksMax][frameMk4*nfrms];
//  char  hdrmap[strLength];
  INT64 jsynch0, jsynch1;
  int nhs, synhs1, synhs2;

//  INT64 day, hr, min, sec;
    
  int Head0,Head1;  //Headstack IDs as seen in the header
  int year0,day0,hh0,mm0,ss0,ms0,us0; //TOT for headstack 0
  int year1,day1,hh1,mm1,ss1,ms1,us1; //TOT for headstack 1
  INT64 TOTusec0, TOTusec1; //in micro seconds
    
  //read and unpack scanfile data into tracks
  nhs = StaPrms.get_nhs();
  if (nhs==1) {
    if (read32datafile(reader, tracks) != 0) {
      get_log_writer().error("error in read32datafile.");
      return -1;
    }
  } else {
    if (read64datafile(reader, tracks) != 0) {
      get_log_writer().error("error in read64datafile.");
      return -1;
    }
  }

  //print track statistics on stdout
  if (get_log_writer().get_messagelevel()> 0)
    printTrackstats(tracks, nhs);
  
  //find sync word(s)
  synhs1 = StaPrms.get_synhs1();
  synhs2 = StaPrms.get_synhs2();
  if (findSyncWord(tracks, synhs1, 0,  &jsynch0) != 0)
    return -1;//no synchronisation word found
  if (nhs==2)
    if(findSyncWord(tracks, synhs2, 32, &jsynch1) != 0)
      return -1;//no synchronisation word found
  jsynch=jsynch0;
  
//  strcpy(hdrmap,StaPrms.get_hdrmap());
//  if (get_log_writer().get_messagelevel() > 0){
//    //printFrameHeader
//    printFrameHeader(tracks, jsynch0, jsynch1, nhs, hdrmap);
//  }  

      
  // calculating TOT for headstack 0 
  timeComps(tracks, jsynch0, nhs, 0,
    &Head0, &year0, &day0, &hh0, &mm0, &ss0, &ms0, &us0, &TOTusec0);
    
  std::cout << "Head stack 0: " << TOTusec0 << std::endl;

  //set time for output in microseconds
  usTime = TOTusec0;
  
  if (nhs==2) {
    // calculating TOT for headstack 1
    timeComps(tracks, jsynch1, synhs2, 1,
      &Head1, &year1, &day1, &hh1, &mm1, &ss1, &ms1, &us1, &TOTusec1);

    std::cout << "Head stack 1: " << TOTusec1 << std::endl;
      
    if(jsynch0 != jsynch1) {
      get_log_writer()(0) << "\nWARNING: jsynch mismatch\n";
      return -1;
    }  
  }

  return retval;
  
}

int main(int argc, char *argv[]) {
  Log_writer_cout log_writer(0);
  set_log_writer(log_writer);
  
  if (argc != 3) {
    std::cout << "usage: " << argv[0] << " <ccf-file> <station_nr>" << std::endl;
    return 1;
  }

  int station_nr;
  str2int(argv[2], station_nr);
  
  RunP runPrms;
  GenP genPrms;
  StaP staPrms[NstationsMax];
  
  if (initialise_control(argv[1], log_writer,
                         runPrms, genPrms, staPrms) != 0) {
    log_writer.error("Initialisation using control file failed");
    return 1;
  }
  
//  log_writer.set_messagelevel(0);

//  double *data_frame_old[1];
//  data_frame_old[0] = new double[frameMk4*staPrms.get_fo()];
//  
//  {
//    Data_reader_file data_reader(staPrms.get_mk4file());
//
//    
//    fill_Mk4frame(0, data_reader, data_frame_old, staPrms);
//  
//    std::ofstream out("out.txt");  
//    for (int i=0; i<frameMk4*staPrms.get_fo(); i++) {
//      out << data_frame_old[0][i] << std::endl;
//    }
//  }

  {
    Data_reader_file data_reader(staPrms[station_nr].get_mk4file());
    Channel_extractor_mark4 ch_extractor(data_reader, staPrms[station_nr]);
    int nBytes = (frameMk4*staPrms[station_nr].get_fo()*staPrms[station_nr].get_bps())/8;
    char data_frame[nBytes];
    
    for (int i=1; i>0; ) {
      i = ch_extractor.get_bytes(nBytes, data_frame);
      
//      int values[2][2] = {{-7, -2}, {2,7}};
//  
//      std::ofstream out("out2.txt");  
//      
//      int i=0;
//      for (int byte = 0; byte < nBytes; byte++) {
//        for (int bit=0; bit<8; bit += 2) {
//          out << values[(data_frame[byte] >> bit)&1][(data_frame[byte] >> (bit+1))&1]
//              << " " << data_frame_old[0][i]
//              << std::endl;
//          i++;
//        } 
//      }
    }
    
  }


//  delete[] data_frame_old[0];

//  UINT64 startIS=27121077500;
  
//  int   jsynch;
//  INT64 usTime;

  //find first header in data file
//  NGHK_FindHeaderMk4(data_reader, jsynch ,usTime, startIS, StaPrms, GenPrms);
//  NGHK_FindHeaderMk4(data_reader, jsynch ,usTime, startIS, StaPrms, GenPrms);
//  NGHK_FindHeaderMk4(data_reader, jsynch ,usTime, startIS, StaPrms, GenPrms);
//  NGHK_FindHeaderMk4(data_reader, jsynch ,usTime, startIS, StaPrms, GenPrms);
//  NGHK_FindHeaderMk4(data_reader, jsynch ,usTime, startIS, StaPrms, GenPrms);
//  NGHK_FindHeaderMk4(data_reader, jsynch ,usTime, startIS, StaPrms, GenPrms);
}
