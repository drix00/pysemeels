#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.mc.test_oos_maker

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.mc.oos_maker`.
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
from nose.tools import nottest

# Local modules.

# Project modules.
from pysemeels.mc.oos_maker import OosMaker
from pysemeels.mc.oos_file import OosFile
from pysemeels import get_current_module_path

# Globals and constants variables.


class TestOosMaker(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.mc.oos_maker`.
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

    @nottest
    def test_make_oos(self):
        """
        Test the method to make the oos data.
        """

        oos_maker = OosMaker()
        oos_maker.title = "OOS of   li"
        oos_maker.number_electrons = 20
        oos_maker.molecular_weight = 6.941
        oos_maker.density_g_cm3 = 0.5
        oos_maker.switch_energy_eV = 55.0
        oos_maker.transition_energy_eV = 55.0

        oos_file = oos_maker.get_oos_file()

        file_path = get_current_module_path(__file__, "../../test_data/mc/li_hcp.oos")
        oos_file_ref = OosFile()
        oos_file_ref.read_file(file_path)

        self.assertEqual(oos_file_ref.title, oos_file.title)
        self.assertEqual(oos_file_ref.number_electrons, oos_file.number_electrons)
        self.assertEqual(oos_file_ref.molecular_weight, oos_file.molecular_weight)
        self.assertEqual(oos_file_ref.density_g_cm3, oos_file.density_g_cm3)
        self.assertEqual(oos_file_ref.switch_energy_eV, oos_file.switch_energy_eV)

        self.assertAlmostEqual(0.01361, oos_file.energies_eV[0])
        self.assertAlmostEqual(4.2988e-09, oos_file.oos[0])
        self.assertAlmostEqual(4.3295e+05, oos_file.energies_eV[-1])
        self.assertAlmostEqual(4.6583e-13, oos_file.oos[-1])

        for energy_ref_eV, df_dw_ref, energy_eV, df_dw in zip(oos_file_ref.energies_eV, oos_file_ref.oos,
                                                              oos_file.energies_eV, oos_file.oos):
            self.assertAlmostEqual(energy_ref_eV, energy_eV)
            self.assertAlmostEqual(df_dw_ref, df_dw)

        self.fail("Test if the testcase is working.")
        self.assert_(True)

if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
