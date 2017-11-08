#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.hitachi.eels_su.map.test_ana_file

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.hitachi.eels_su.map.ana_file`.
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
from pysemeels import get_current_module_path
from pysemeels.hitachi.eels_su.map.ana_file import AnaFile
from tests import is_bad_file

# Globals and constants variables.


class TestSimulationData(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.hitachi.eels_su.ana_file`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.ana_file_path = get_current_module_path(__file__, "../../../../test_data/hitachi/eels_su/30kV_march2017_7eV/spectra_1.ana")

        if is_bad_file(self.ana_file_path):
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

    def test_read_file(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        with open(self.ana_file_path, 'r') as ana_text_file:
            ana_file = AnaFile()
            ana_file.read(ana_text_file)

            self.assertEqual("01/Mar/2017", ana_file.date)
            self.assertEqual("11:20", ana_file.time)
            self.assertEqual("", ana_file.comment)
            self.assertEqual("0.5ms", ana_file.dose)
            self.assertEqual("0.0eV", ana_file.le)
            self.assertEqual(98.7, ana_file.raw)
            self.assertEqual("7.0eV", ana_file.energy_width)
            self.assertEqual("586ch", ana_file.dual_det_position)
            self.assertEqual("133ch", ana_file.dual_det_post)
            self.assertEqual("608ch", ana_file.dual_det_center)
            self.assertEqual(13575, ana_file.q1)
            self.assertEqual(3850, ana_file.q1s)
            self.assertEqual(0, ana_file.q2)
            self.assertEqual(0, ana_file.q2s)
            self.assertEqual(2700, ana_file.q3)
            self.assertEqual(0, ana_file.q3s)
            self.assertEqual(2900, ana_file.h1)
            self.assertEqual(6150, ana_file.h1s)
            self.assertEqual(-600, ana_file.h2)
            self.assertEqual(350, ana_file.h2s)
            self.assertEqual(0, ana_file.h3)
            self.assertEqual(0, ana_file.h3s)
            self.assertEqual(0, ana_file.elv_x)
            self.assertEqual(0, ana_file.elv_y)
            self.assertEqual(259, ana_file.spectrum_alignment_x)
            self.assertEqual(0, ana_file.spectrum_alignment_y)
            self.assertEqual(-1500, ana_file.det_map_alignment_x)
            self.assertEqual(1500, ana_file.det_map_alignment_y)

            self.assertEqual(37443, ana_file.mag)

            self.assertEqual(-32.00, ana_file.energies_eV[0])
            self.assertEqual(4.0, ana_file.total_spectra[0][0])
            self.assertEqual(21.842, ana_file.energies_eV[-1])
            self.assertEqual(0, ana_file.total_spectra[0][-1])
            self.assertEqual(1024, len(ana_file.energies_eV))
            self.assertEqual(1024, len(ana_file.total_spectra[0]))

            self.assertEqual(20, len(ana_file.spectra[0]))
            self.assertEqual(19, ana_file.spectrum_id)

        # self.fail("Test if the testcase is working.")

    def test_read_file_linescan(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        ana_file_path = get_current_module_path(__file__, "../../../../test_data/hitachi/eels_su/vacuum_linescan_07eV_i50_52pts/spectra_3.ana")
        if is_bad_file(ana_file_path):
            raise SkipTest

        with open(ana_file_path, 'r') as ana_text_file:
            ana_file = AnaFile()
            ana_file.read(ana_text_file)

            self.assertEqual("03/Mar/2017", ana_file.date)
            self.assertEqual("15:32", ana_file.time)
            self.assertEqual("", ana_file.comment)
            self.assertEqual("0.5ms", ana_file.dose)
            self.assertEqual("0.0eV", ana_file.le)
            self.assertEqual(75.2, ana_file.raw)
            self.assertEqual("7.0eV", ana_file.energy_width)
            self.assertEqual("586ch", ana_file.dual_det_position)
            self.assertEqual("133ch", ana_file.dual_det_post)
            self.assertEqual("608ch", ana_file.dual_det_center)
            self.assertEqual(13560, ana_file.q1)
            self.assertEqual(4150, ana_file.q1s)
            self.assertEqual(0, ana_file.q2)
            self.assertEqual(0, ana_file.q2s)
            self.assertEqual(2700, ana_file.q3)
            self.assertEqual(0, ana_file.q3s)
            self.assertEqual(3050, ana_file.h1)
            self.assertEqual(5850, ana_file.h1s)
            self.assertEqual(-650, ana_file.h2)
            self.assertEqual(1250, ana_file.h2s)
            self.assertEqual(0, ana_file.h3)
            self.assertEqual(0, ana_file.h3s)
            self.assertEqual(0, ana_file.elv_x)
            self.assertEqual(0, ana_file.elv_y)
            self.assertEqual(196, ana_file.spectrum_alignment_x)
            self.assertEqual(0, ana_file.spectrum_alignment_y)
            self.assertEqual(-1280, ana_file.det_map_alignment_x)
            self.assertEqual(1500, ana_file.det_map_alignment_y)

            self.assertEqual(37443, ana_file.mag)

            self.assertEqual(1024, len(ana_file.energies_eV))
            self.assertEqual(52, len(ana_file.total_spectra))
            self.assertEqual(1024, len(ana_file.total_spectra[0]))
            self.assertEqual(1024, len(ana_file.total_spectra[51]))

            self.assertEqual(-32.00, ana_file.energies_eV[0])
            self.assertEqual(1.0, ana_file.total_spectra[0][0])
            self.assertEqual(21.842, ana_file.energies_eV[-1])
            self.assertEqual(0, ana_file.total_spectra[0][-1])

            self.assertEqual(52, len(ana_file.spectra))
            self.assertEqual(50, len(ana_file.spectra[0]))
            self.assertEqual(49, ana_file.spectrum_id)

        # self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
