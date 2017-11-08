#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.hitachi.eels_su.test_ana_file

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.hitachi.eels_su.ana_file`.
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
from pysemeels.hitachi.eels_su.ana_file import AnaFile
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

        self.ana_file_path = get_current_module_path(__file__, "../../../test_data/hitachi/eels_su/30kV_7eV.ana")

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

        with open(self.ana_file_path, 'r') as elv_text_file:
            ana_file = AnaFile()
            ana_file.read(elv_text_file)

            self.assertEqual(-32.00, ana_file.energies_eV[0])
            self.assertEqual(-33.0, ana_file.counts[0])
            self.assertEqual(21.84, ana_file.energies_eV[-1])
            self.assertEqual(0.0, ana_file.counts[-1])
            self.assertEqual(1024, len(ana_file.energies_eV))
            self.assertEqual(1024, len(ana_file.counts))

            self.assertEqual(1.0, ana_file.gain_corrections[0])
            self.assertEqual(1.0, ana_file.gain_corrections[-1])
            self.assertEqual(1024, len(ana_file.gain_corrections))

            self.assertEqual(0, ana_file.dark_currents[0])
            self.assertEqual(0, ana_file.dark_currents[-1])
            self.assertEqual(1024, len(ana_file.dark_currents))

        # self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
