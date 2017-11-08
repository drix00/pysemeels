#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.hitachi.eels_su.test_elv_text_file

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`ElvTextFile`.
"""

###############################################################################
# Copyright 2017 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.
import unittest
import os.path

# Third party modules.
from nose import SkipTest

# Local modules.

# Project modules.
from pysemeels.hitachi.eels_su.elv_text_file import ElvTextParameters
from pysemeels import get_current_module_path
from tests import is_bad_file

# Globals and constants variables.


class TestElvTextFile(unittest.TestCase):
    """
    TestCase class for the module `ElvTextFile`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.elv_text_file_path = get_current_module_path(__file__, "../../../test_data/hitachi/eels_su/30kV_7eV.txt")

        if is_bad_file(self.elv_text_file_path):
            raise SkipTest

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_read_text_file(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        with open(self.elv_text_file_path, 'r', encoding="UTF-16") as elv_text_file:
            elv_text_parameters = ElvTextParameters()
            elv_text_parameters.read(elv_text_file)

            self.assertEqual("SU-EELS", elv_text_parameters.model)
            self.assertEqual(0.0, elv_text_parameters.sample_height_mm)
            self.assertEqual(r"D:\2017\System_baseline_march2017\30kV_7eV.elv", elv_text_parameters.file_name)
            self.assertEqual("", elv_text_parameters.comment)
            self.assertEqual("01/Mar/2017", elv_text_parameters.date)
            self.assertEqual("10:59", elv_text_parameters.time)
            self.assertEqual(30000, elv_text_parameters.accelerating_voltage_V)
            self.assertEqual(7.0, elv_text_parameters.energy_width_eV)
            self.assertEqual(0.0, elv_text_parameters.energy_loss_eV)
            self.assertEqual(500, elv_text_parameters.speed_us)

        # self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
