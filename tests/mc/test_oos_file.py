#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.mc.test_oos_file

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.mc.oos_file`.
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

# Third party modules.
from nose import SkipTest

# Local modules.

# Project modules.
from pysemeels.mc.oos_file import OosFile
from pysemeels import get_current_module_path
from tests import is_bad_file

# Globals and constants variables.


class TestOosFile(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.mc.oos_file`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

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

    def test_read_oos_file(self):
        """
        Test the method to read the oos file.
        """

        file_path = get_current_module_path(__file__, "../../test_data/mc/li_hcp.oos")
        if is_bad_file(file_path):
            raise SkipTest

        oos_file = OosFile()
        oos_file.read_file(file_path)

        self.assertEqual("OOS of   li", oos_file.title)
        self.assertEqual(20, oos_file.number_electrons)
        self.assertAlmostEqual(6.941, oos_file.molecular_weight)
        self.assertAlmostEqual(0.5, oos_file.density_g_cm3)
        self.assertAlmostEqual(55.0, oos_file.switch_energy_eV)

        self.assertEqual(346, len(oos_file.energies_eV))
        self.assertEqual(346, len(oos_file.oos))

        self.assertAlmostEqual(0.01361, oos_file.energies_eV[0])
        self.assertAlmostEqual(4.2988e-09, oos_file.oos[0])
        self.assertAlmostEqual(4.3295e+05, oos_file.energies_eV[-1])
        self.assertAlmostEqual(4.6583e-13, oos_file.oos[-1])

        # self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
