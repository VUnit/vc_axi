# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014-2019, Lars Asplund lars.anders.asplund@gmail.com

"""
Verify that all external run scripts work correctly
"""


import unittest
from os import environ
from os.path import join, dirname
from subprocess import call
import sys
from vunit.test.common import has_simulator, simulator_is


ROOT = dirname(__file__)


def simulator_supports_verilog():
    """
    Returns True if simulator supports Verilog
    """
    return simulator_is("modelsim", "incisive")


# pylint: disable=too-many-public-methods
@unittest.skipUnless(has_simulator(), "Requires simulator")
class TestExternalRunScripts(unittest.TestCase):
    """
    Verify that example projects run correctly
    """

    def test_vhdl_array_axis_vcs_example_project(self):
        self.check(join(ROOT, "array_axis_vcs", "run.py"))

    def test_vhdl_axi_dma_example_project(self):
        self.check(join(ROOT, "axi_dma", "run.py"))

    def setUp(self):
        self.output_path = join(dirname(__file__), "external_run_out")
        self.report_file = join(self.output_path, "xunit.xml")

    def check(self, run_file, args=None, vhdl_standard='2008', exit_code=0):
        """
        Run external run file and verify exit code
        """
        args = args if args is not None else []
        new_env = environ.copy()
        new_env["VUNIT_VHDL_STANDARD"] = vhdl_standard
        retcode = call([sys.executable, run_file,
                        "--clean",
                        "--output-path=%s" % self.output_path,
                        "--xunit-xml=%s" % self.report_file] + args,
                       env=new_env)
        self.assertEqual(retcode, exit_code)
