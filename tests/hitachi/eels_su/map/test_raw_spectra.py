#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.hitachi.eels_su.map.test_raw_spectra

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.hitachi.eels_su.map.spectra`.
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
from pysemeels.hitachi.eels_su.map.raw_spectra import RawSpectra
from tests import is_bad_file

# Globals and constants variables.


class TestSimulationData(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.hitachi.eels_su.map.spectra`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.raw_spectra_file_path = get_current_module_path(__file__, "../../../../test_data/hitachi/eels_su/30kV_march2017_7eV/RawSpectra/rawspect-1.dat")

        if is_bad_file(self.raw_spectra_file_path):
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

        with open(self.raw_spectra_file_path, 'rb') as raw_spectra_file:
            raw_spectra = RawSpectra()
            raw_spectra.read(raw_spectra_file)

            self.assertEqual(20, len(raw_spectra.raw_spectra))
            self.assertEqual(20, raw_spectra.raw_spectrum_id)

            spectrum = raw_spectra.raw_spectra[0]
            self.assertEqual(2284, spectrum[0])
            self.assertEqual(0, spectrum[-1])
            self.assertEqual(1024, len(spectrum))

        # self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
