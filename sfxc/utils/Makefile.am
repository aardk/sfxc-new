AM_CXXFLAGS = $(UTILS_CXXFLAGS)
AM_CPPFLAGS = $(UTILS_CPPLAGS)
LDADD = $(UTILS_LDADD)

if GENDELAY
  SUBDIRS = delay
endif

pkginclude_HEADERS = *.h *.py

bin_PROGRAMS = mark5a_print_headers \
               mark5b_print_headers \
	       vdif_check_data \
               vdif_print_headers \
               vlba_print_headers \
               print_new_output_format \
               extract_channelizer

if SFXC_UTILS
bin_PROGRAMS += generate_uvw_coordinates \
                plot_delay_table \
                phase_plot \
                make_anim \
                produce_html_plotpage \
                produce_html_diffpage \
                baseline_info \
                polyflag
endif

bin_SCRIPTS  = run_sfxc.py gen_all_delay_tables.py channel_extractor_compiler.py print_corfile.py \
               generate_jobs.py get_file_list.py create_debug.py

extract_channelizer_SOURCES = \
  extract_channelizer.cc \
  ../src/control_parameters.cc \
  ../src/log_writer_cout.cc \
  ../src/log_writer.cc \
  ../src/data_reader.cc \
  ../src/data_writer.cc \
  ../src/data_reader_file.cc \
  ../src/input_data_format_reader.cc \
  ../src/mark5a_reader.cc \
  ../src/mark5a_header.cc \
  ../src/data_reader_factory.cc \
  ../src/data_reader_mk5.cc \
  ../src/data_reader_socket.cc \
  ../src/data_reader_udp.cc \
  ../src/data_writer_socket.cc \
  ../src/data_reader_blocking.cc \
  ../src/channel_extractor_dynamic.cc \
  ../src/channel_extractor_5.cc \
  ../src/utils.cc \
  ../src/correlator_time.cc

mark5b_print_headers_SOURCES = \
  mark5b_print_headers.cc

vdif_print_headers_SOURCES = \
  vdif_print_headers.cc \
  ../src/utils.cc \
  ../src/correlator_time.cc

vdif_check_data_SOURCES = \
  vdif_check_data.cc \
  ../src/utils.cc \
  ../src/correlator_time.cc

mark5a_print_headers_SOURCES = \
  mark5a_print_headers.cc \
  ../src/data_reader.cc \
  ../src/data_reader_file.cc \
  ../src/data_reader_blocking.cc  \
  ../src/input_data_format_reader.cc \
  ../src/mark5a_reader.cc \
  ../src/mark5a_header.cc \
  ../src/channel_extractor_5.cc \
  ../src/utils.cc \
  ../src/control_parameters.cc \
  ../src/correlator_time.cc

vlba_print_headers_SOURCES = \
  vlba_print_headers.cc \
  ../src/data_reader.cc \
  ../src/data_reader_file.cc \
  ../src/data_reader_blocking.cc  \
  ../src/input_data_format_reader.cc \
  ../src/vlba_reader.cc \
  ../src/vlba_header.cc \
  ../src/channel_extractor_5.cc \
  ../src/utils.cc \
  ../src/control_parameters.cc \
  ../src/correlator_time.cc

produce_html_plotpage_SOURCES = \
  produce_html_plotpage.cc \
  fringe_info.cc \
  ../src/control_parameters.cc \
  ../src/log_writer.cc \
  ../src/log_writer_cout.cc \
  ../src/utils.cc \
  ../src/output_header.cc \
  ../src/correlator_time.cc\
  ../src/sfxc_fft_float.cc \
  gnuplot_i.cc

produce_html_diffpage_SOURCES = \
  produce_html_diffpage.cc \
  fringe_info.cc \
  ../src/control_parameters.cc \
  ../src/log_writer.cc \
  ../src/log_writer_cout.cc \
  ../src/utils.cc \
  ../src/output_header.cc \
  ../src/correlator_time.cc\
  ../src/sfxc_fft_float.cc \
  gnuplot_i.cc

baseline_info_SOURCES = \
  baseline_info.cc \
  fringe_info.cc \
  ../src/control_parameters.cc \
  ../src/log_writer.cc \
  ../src/log_writer_cout.cc \
  ../src/utils.cc \
  ../src/output_header.cc \
  ../src/correlator_time.cc\
  ../src/sfxc_fft_float.cc \
  gnuplot_i.cc

generate_uvw_coordinates_SOURCES = \
  generate_uvw_coordinates.cc \
  ../src/uvw_model.cc \
  ../src/utils.cc \
  ../src/correlator_time.cc

plot_delay_table_SOURCES = \
  plot_delay_table.cc \
  ../src/delay_table_akima.cc \
  ../src/uvw_model.cc \
  ../src/utils.cc \
  ../src/correlator_time.cc

print_new_output_format_SOURCES = \
  print_new_output_format.cc \
  ../src/output_header.cc \
   ../src/utils.cc

phase_plot_SOURCES = \
  phase_plot.cc \
  ../src/output_header.cc \
   ../src/utils.cc \
   ../src/sfxc_fft_float.cc

make_anim_SOURCES = \
  make_anim.cc \
  gnuplot_i.cc \
  ../src/utils.cc \
  ../src/sfxc_fft_float.cc

polyflag_SOURCES = \
  polyflag.cc \
  ../src/delay_table_akima.cc \
  ../src/correlator_time.cc \
  ../src/utils.cc
