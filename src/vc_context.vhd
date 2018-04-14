-- This Source Code Form is subject to the terms of the Mozilla Public
-- License, v. 2.0. If a copy of the MPL was not distributed with this file,
-- You can obtain one at http://mozilla.org/MPL/2.0/.
--
-- Copyright (c) 2014-2018, Lars Asplund lars.anders.asplund@gmail.com

context vc_context is
  library vunit_lib;
  use vunit_lib.bus_master_pkg.all;
  use vunit_lib.axi_pkg.all;
  use vunit_lib.axi_stream_pkg.all;
  use vunit_lib.uart_pkg.all;
  use vunit_lib.stream_master_pkg.all;
  use vunit_lib.stream_slave_pkg.all;
  context vunit_lib.com_context;
end context;
