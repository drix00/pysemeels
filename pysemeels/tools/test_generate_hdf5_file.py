#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.tools.test_generate_hdf5_file

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.tools.generate_hdf5_file`.
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
import h5py

# Local modules.

# Project modules.
from pysemeels.tools.generate_hdf5_file import GenerateHdf5File
from pysemeels import get_current_module_path
from pysemeels.tools.hdf5_file_labels import *

# Globals and constants variables.

class TestGenerateHdf5File(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.tools.generate_hdf5_file`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.elv_file_path = get_current_module_path(__file__, "../../test_data/hitachi/eels_su/30kV_7eV.elv")
        self.hdf5_file_path = get_current_module_path(__file__, "../../test_data/hitachi/eels_su/30kV_7eV.hdf5")

        if not os.path.isfile(self.elv_file_path):  # pragma: no cover
            raise SkipTest

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

        if os.path.isfile(self.hdf5_file_path):
            os.remove(self.hdf5_file_path)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_init(self):
        """
        Test the convert method.
        """
        self.assertFalse(os.path.isfile(self.hdf5_file_path))
        with h5py.File(self.hdf5_file_path, 'w') as hdf5_file:
            self.assertTrue(os.path.isfile(self.hdf5_file_path))

            generate_hdf5_file = GenerateHdf5File(hdf5_file)

            self.assertEqual(hdf5_file, generate_hdf5_file.hdf5_file)

        # self.fail("Test if the testcase is working.")

    def test_add_spectrum(self):
        """
        Test the convert method.
        """
        self.assertFalse(os.path.isfile(self.hdf5_file_path))
        with h5py.File(self.hdf5_file_path, 'w') as hdf5_file:
            self.assertTrue(os.path.isfile(self.hdf5_file_path))

            generate_hdf5_file = GenerateHdf5File(hdf5_file)

            generate_hdf5_file.add_spectrum(self.elv_file_path)
            self.assertTrue("30kV_7eV" in generate_hdf5_file.hdf5_file)

            name_ref = "Nominal spectrum"
            generate_hdf5_file.add_spectrum(self.elv_file_path, name=name_ref)
            self.assertTrue(name_ref in generate_hdf5_file.hdf5_file)

            spectrum_group = generate_hdf5_file.hdf5_file[name_ref]
            self.assertEqual("SU-EELS", spectrum_group.attrs[HDF5_MODEL])
            self.assertEqual("0.0mm", spectrum_group.attrs[HDF5_SAMPLE_HEIGHT])
            self.assertEqual(r"D:\2017\System_baseline_march2017\30kV_7eV.elv",
                             spectrum_group.attrs[HDF5_FILE_PATH])
            self.assertEqual("", spectrum_group.attrs[HDF5_COMMENT])
            self.assertEqual("01/Mar/2017", spectrum_group.attrs[HDF5_DATE])
            self.assertEqual("10:59", spectrum_group.attrs[HDF5_TIME])
            self.assertEqual(30000, spectrum_group.attrs[HDF5_ACCELERATING_VOLTAGE_V])
            self.assertEqual(7.0, spectrum_group.attrs[HDF5_ENERGY_WIDTH_eV])
            self.assertEqual("0.0eV", spectrum_group.attrs[HDF5_ENERGY_LOSS])
            self.assertEqual("500µs", spectrum_group.attrs[HDF5_ACQUISITION_SPEED])

            self.assertEqual("01/Mar/2017",spectrum_group.attrs[HDF5_DATE])
            self.assertEqual("10:59", spectrum_group.attrs[HDF5_TIME])
            self.assertEqual("", spectrum_group.attrs[HDF5_COMMENT])
            self.assertEqual("500µs", spectrum_group.attrs[HDF5_ACQUISITION_SPEED])
            self.assertEqual("0.0eV", spectrum_group.attrs[HDF5_ENERGY_LOSS])
            self.assertEqual(98.7, spectrum_group.attrs[HDF5_RAW])
            self.assertEqual(7.0, spectrum_group.attrs[HDF5_ENERGY_WIDTH_eV])
            self.assertEqual("586ch", spectrum_group.attrs[HDF5_DUAL_DET_POSITION])
            self.assertEqual("133ch", spectrum_group.attrs[HDF5_DUAL_DET_POST])
            self.assertEqual("608ch", spectrum_group.attrs[HDF5_DUAL_DET_CENTER])
            self.assertEqual(13575, spectrum_group.attrs[HDF5_Q1])
            self.assertEqual(3850, spectrum_group.attrs[HDF5_Q1S])
            self.assertEqual(0, spectrum_group.attrs[HDF5_Q2])
            self.assertEqual(0, spectrum_group.attrs[HDF5_Q2S])
            self.assertEqual(2700, spectrum_group.attrs[HDF5_Q3])
            self.assertEqual(2900, spectrum_group.attrs[HDF5_H1])
            self.assertEqual(6150, spectrum_group.attrs[HDF5_H1S])
            self.assertEqual(-600, spectrum_group.attrs[HDF5_H2])
            self.assertEqual(350, spectrum_group.attrs[HDF5_H2S])
            self.assertEqual(0, spectrum_group.attrs[HDF5_H4])
            self.assertEqual(0, spectrum_group.attrs[HDF5_ELV_X])
            self.assertEqual(0, spectrum_group.attrs[HDF5_ELV_Y])
            self.assertEqual(259, spectrum_group.attrs[HDF5_SPECTRUM_ALIGNMENT_X])
            self.assertEqual(0, spectrum_group.attrs[HDF5_SPECTRUM_ALIGNMENT_Y])
            self.assertEqual(-1500, spectrum_group.attrs[HDF5_DET_SPEC_ALIGNMENT_X])
            self.assertEqual(470, spectrum_group.attrs[HDF5_DET_SPEC_ALIGNMENT_Y])
            self.assertEqual(-1500, spectrum_group.attrs[HDF5_DET_MAP_ALIGNMENT_X])
            self.assertEqual(1500, spectrum_group.attrs[HDF5_DET_MAP_ALIGNMENT_Y])

            self.assertEqual(37443, spectrum_group.attrs[HDF5_MAGNIFICATION])

            spectrum_data_set = spectrum_group[HDF5_SPECTRUM]

            energies_eV = spectrum_data_set[:, 0]
            self.assertEqual(-32.00, energies_eV[0])
            self.assertEqual(21.789999999999999, energies_eV[-1])
            self.assertEqual(1023, len(energies_eV))

            counts = spectrum_data_set[:, 1]
            self.assertEqual(-33.755274261603375, counts[0])
            self.assertEqual(-26.345388037167261, counts[-1])
            self.assertEqual(1023, len(counts))

            raw_counts = spectrum_data_set[:, 2]
            self.assertEqual(2282, raw_counts[0])
            self.assertEqual(2293.0, raw_counts[-1])
            self.assertEqual(1023, len(raw_counts))

            gain_corrections = spectrum_data_set[:, 3]
            self.assertEqual(0.918375, gain_corrections[0])
            self.assertEqual(0.98689000000000004, gain_corrections[-1])
            self.assertEqual(1023, len(gain_corrections))

            dark_currents = spectrum_data_set[:, 4]
            self.assertEqual(2313, dark_currents[0])
            self.assertEqual(2319.0, dark_currents[-1])
            self.assertEqual(1023, len(dark_currents))

        # self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
