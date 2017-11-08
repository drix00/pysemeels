#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.hitachi.eels_su.map.test_text_file

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.hitachi.eels_su.map.text_file`.
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
from pysemeels.hitachi.eels_su.map.text_file import TextParameters
from pysemeels import get_current_module_path
from tests import is_bad_file

# Globals and constants variables.

class TestTextFile(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.hitachi.eels_su.map.text_file`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.text_file_path = get_current_module_path(__file__, "../../../../test_data/hitachi/eels_su/30kV_march2017_7eV/30kV_march2017_7eV.txt")
        if is_bad_file(self.text_file_path):
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

        with open(self.text_file_path, 'r', encoding="UTF-16") as text_file:
            text_parameters = TextParameters()
            text_parameters.read(text_file)

            self.assertEqual(130000, text_parameters.magnification)
            self.assertEqual("SU-EELS", text_parameters.model)
            self.assertEqual("0.0mm", text_parameters.sample_height)
            self.assertEqual(r"30kV_march2017_7eV", text_parameters.file_name)
            self.assertEqual("01/Mar/2017", text_parameters.date)
            self.assertEqual("11:20:40", text_parameters.time)
            self.assertEqual("512x512", text_parameters.capture_resolution)
            self.assertEqual(30000, text_parameters.accelerating_voltage_V)
            self.assertEqual("7eV", text_parameters.energy_width)
            self.assertEqual("0.0eV", text_parameters.energy_loss)
            self.assertEqual("Slow1", text_parameters.speed)
            self.assertEqual(128, text_parameters.dpi)
            self.assertEqual("", text_parameters.pixel_distance)

            self.assertEqual(0.5, text_parameters.analysis1.dose)
            self.assertEqual(7, text_parameters.analysis1.energy_width_eV)
            self.assertEqual(0.0, text_parameters.analysis1.energy_loss_eV)
            self.assertEqual(0.0, text_parameters.analysis2.dose)
            self.assertEqual(0, text_parameters.analysis2.energy_width_eV)
            self.assertEqual(0.0, text_parameters.analysis2.energy_loss_eV)
            self.assertEqual(0.0, text_parameters.analysis3.dose)
            self.assertEqual(0, text_parameters.analysis3.energy_width_eV)
            self.assertEqual(0.0, text_parameters.analysis3.energy_loss_eV)

            self.assertEqual("", text_parameters.A)
            self.assertEqual("", text_parameters.B)
            self.assertEqual("", text_parameters.distance)
            self.assertEqual("", text_parameters.pitch)
            self.assertEqual(1, text_parameters.number)
            self.assertEqual("", text_parameters.adjust)
            self.assertEqual("", text_parameters.data_size)
            self.assertEqual(20, text_parameters.integration)

        # self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
