#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.hitachi.eels_su.test_csv_file

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.hitachi.eels_su.csv_file`.
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
from pysemeels.hitachi.eels_su.csv_file import CsvFile
from tests import is_bad_file

# Globals and constants variables.


class TestCsvFile(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.hitachi.eels_su.csv_file`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.file_path = get_current_module_path(__file__, "../../../test_data/hitachi/eels_su/30kV_7eV.csv")

        if is_bad_file(self.file_path):
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

        with open(self.file_path, 'r') as csv_text_file:
            csv_file = CsvFile()
            csv_file.read(csv_text_file)

            self.assertEqual("01/Mar/2017", csv_file.date)
            self.assertEqual("10:59", csv_file.time)
            self.assertEqual("", csv_file.comment)
            self.assertEqual("100msec", csv_file.view_fast)
            self.assertEqual("1msec", csv_file.view_slow)
            self.assertEqual("200msec", csv_file.store_manual)
            self.assertEqual("50msec", csv_file.store_auto)
            self.assertEqual("0.0eV", csv_file.le)
            self.assertEqual("608ch", csv_file.dual_det_center)
            self.assertEqual(100.0, csv_file.raw)
            self.assertEqual("7.0eV", csv_file.energy_width)
            self.assertEqual("133ch", csv_file.dual_det_post)
            self.assertEqual("586ch", csv_file.dual_window1_position)
            self.assertEqual("443ch", csv_file.dual_window2_position)
            self.assertEqual(13563, csv_file.q1)
            self.assertEqual(0, csv_file.q2)
            self.assertEqual(2700, csv_file.q3)
            self.assertEqual(273, csv_file.spectrum_alignment_x)
            self.assertEqual(0, csv_file.spectrum_alignment_y)
            self.assertEqual(37443, csv_file.mag)

            self.assertEqual(-32.00, csv_file.energies_eV[0])
            self.assertEqual(0, csv_file.counts[0])
            self.assertEqual(21.84, csv_file.energies_eV[-1])
            self.assertEqual(-2147483648, csv_file.counts[-1])
            self.assertEqual(1024, len(csv_file.energies_eV))
            self.assertEqual(1024, len(csv_file.counts))

        # self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
