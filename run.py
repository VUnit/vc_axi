# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014-2019, Lars Asplund lars.anders.asplund@gmail.com

from os.path import join, dirname
from vunit import VUnit
from itertools import product

root = dirname(__file__)

ui = VUnit.from_argv()
ui.add_random()
ui.add_verification_components()
lib = ui.library("vunit_lib")
lib.add_source_files([
    join(root, "src", "*.vhd"),
    join(root, "test", "*.vhd")
])

tb_axi_stream_protocol_checker = lib.test_bench("tb_axi_stream_protocol_checker")

for data_length in [0, 8]:
    for test in tb_axi_stream_protocol_checker.get_tests("*passing*tdata*"):
        test.add_config(name="data_length=%d" % data_length, generics=dict(data_length=data_length))

for test in tb_axi_stream_protocol_checker.get_tests("*failing*tid width*"):
    test.add_config(name="dest_length=25", generics=dict(dest_length=25))
    test.add_config(name="id_length=8 dest_length=17", generics=dict(id_length=8, dest_length=17))

test_failing_max_waits = tb_axi_stream_protocol_checker.test(
    "Test failing check of that tready comes within max_waits after valid")
for max_waits in [0, 8]:
    test_failing_max_waits.add_config(name="max_waits=%d" % max_waits, generics=dict(max_waits=max_waits))

ui.main()
