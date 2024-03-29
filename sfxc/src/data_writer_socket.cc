/* Copyright (c) 2007 Joint Institute for VLBI in Europe (Netherlands)
 * All rights reserved.
 *
 * Author(s): Nico Kruithof <Kruithof@JIVE.nl>, 2007
 *
 * $Id: Data_writer_socket.cc 278 2007-07-04 07:27:05Z kruithof $
 *
 */

#include "data_writer_socket.h"
#include "exception_common.h"

#include <iostream>
// defines send:
#include <sys/types.h>
#include <sys/socket.h>
#include <errno.h>
#include <utils.h>

#include <tcp_connection.h>
#include <connexion.h>


Data_writer_socket::Data_writer_socket(int socket) {
  m_socket = socket;
  SFXC_ASSERT(m_socket >= 0);
}

Data_writer_socket::Data_writer_socket(Connexion* connexion) {
  m_socket = connexion->get_socket();
  SFXC_ASSERT(m_socket >= 0);
}

Data_writer_socket::~Data_writer_socket() {}

size_t Data_writer_socket::do_put_bytes(size_t nBytes, char const *buff) {
  if (m_socket <= 0) return 0;
  SFXC_ASSERT(nBytes > 0);
  size_t bytes_written = 0;

  while (bytes_written != nBytes) {
    int result = write(m_socket, buff+bytes_written, nBytes-bytes_written);
    if (result <= 0) {
      return bytes_written;
    }
    bytes_written += result;
  }

  SFXC_ASSERT(bytes_written == nBytes);
  return bytes_written;
}

