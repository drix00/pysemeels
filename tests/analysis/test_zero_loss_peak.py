#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.analysis.test_zero_loss_peak

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.analysis.zero_loss_peak`.
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
from pysemeels.analysis.zero_loss_peak import ZeroLossPeak
from pysemeels.hitachi.eels_su.elv_file import ElvFile
from tests import is_bad_file

# Globals and constants variables.

class TestZeroLossPeak(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.analysis.zero_loss_peak`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.elv_file_path = get_current_module_path(__file__, "../../test_data/hitachi/eels_su/30kV_7eV.elv")

        if is_bad_file(self.elv_file_path):
            SkipTest

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

    def test_find_position(self):
        """
        Test the find_position method is working.

        """
        with open(self.elv_file_path, 'r') as elv_text_file:
            elv_file = ElvFile()
            elv_file.read(elv_text_file)

            zero_lost_peak = ZeroLossPeak(elv_file.energies_eV, elv_file.raw_counts)
            zero_lost_peak.find_position()
            self.assertAlmostEqual(0.05, zero_lost_peak.position_eV)

        # self.fail("Test if the testcase is working.")

    def test_compute_fwhm(self):
        """
        Test the compute_fwhm method is working.
        """

        with open(self.elv_file_path, 'r') as elv_text_file:
            elv_file = ElvFile()
            elv_file.read(elv_text_file)

            zero_lost_peak = ZeroLossPeak(elv_file.energies_eV, elv_file.raw_counts)
            zero_lost_peak.compute_fwhm()
            self.assertAlmostEqual(0.57999999999999996, zero_lost_peak.fwhm_eV)
            self.assertAlmostEqual(1.3700, zero_lost_peak.fwtm_eV)
            self.assertAlmostEqual(1.74, zero_lost_peak.fwfm_eV)

        # self.fail("Test if the testcase is working.")

    def test_compute_statistics(self):
        """
        Test the compute_statistics method is working.
        """

        with open(self.elv_file_path, 'r') as elv_text_file:
            elv_file = ElvFile()
            elv_file.read(elv_text_file)

            zero_lost_peak = ZeroLossPeak(elv_file.energies_eV, elv_file.raw_counts)
            zero_lost_peak.compute_statistics()
            self.assertAlmostEqual(1042790, zero_lost_peak.number_counts)
            self.assertAlmostEqual(-4.16, zero_lost_peak.minimum_eV)
            self.assertAlmostEqual(4.16, zero_lost_peak.maximum_eV)
            self.assertAlmostEqual(0.04945319767163061, zero_lost_peak.mean_eV)
            self.assertAlmostEqual(2.2138369332753909, zero_lost_peak.variance_eV2)
            self.assertAlmostEqual(1.4878968153993042, zero_lost_peak.std_eV)
            self.assertAlmostEqual(-0.07548493790601353, zero_lost_peak.skewness)
            self.assertAlmostEqual(1.5175832076107003, zero_lost_peak.kurtosis)

        # self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose
    nose.runmodule()
