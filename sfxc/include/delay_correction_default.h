/* Copyright (c) 2007 Joint Institute for VLBI in Europe (Netherlands)
 * All rights reserved.
 *
 * Author(s): Nico Kruithof <Kruithof@JIVE.nl>, 2007
 *            Aard Keimpema <keimpema@jive.nl>, 2008
 *
 * $Id: channel_extractor.h 412 2007-12-05 12:13:20Z kruithof $
 *
 */

#ifndef DELAY_CORRECTION_DEFAULT_H
#define DELAY_CORRECTION_DEFAULT_H
#include <boost/shared_ptr.hpp>
#include <complex>
#include <fftw3.h>

#include "delay_correction_base.h"
#include "tasklet/tasklet.h"
#include "delay_table_akima.h"
#include "correlator_node_types.h"
#include "control_parameters.h"
#ifdef USE_DOUBLE
#include "sfxc_fft.h"
#else
#include "sfxc_fft_float.h"
#endif
class Delay_correction_default : public Delay_correction_base {
public:
  Delay_correction_default(int stream_nr);
  ~Delay_correction_default(){};

  void set_parameters(const Correlation_parameters &parameters);
  /// Do one delay step
  void do_task();

private:
  ///
  void fractional_bit_shift(FLOAT *input,
                            int integer_shift,
                            FLOAT fractional_delay);
  void fringe_stopping(FLOAT output[]);

private:
  Time fft_length;
  SFXC_FFT        fft_t2f, fft_f2t, fft_t2f_cor;
  Memory_pool_vector_element< std::complex<FLOAT> >  exp_array;
};

#endif /*DELAY_CORRECTION_DEFAULT_H*/