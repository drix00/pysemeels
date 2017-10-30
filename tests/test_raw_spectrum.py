#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.test_raw_spectrum

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.raw_spectrum`.
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
import os

# Third party modules.
import h5py
from nose import SkipTest
import numpy as np

# Local modules.

# Project modules.
from pysemeels import get_current_module_path
from pysemeels.raw_spectrum import RawSpectrum, HDF5_GROUP_EXTRA_PARAMETERS, HDF5_GROUP_EELS_PARAMETERS, \
    HDF5_DATASET_ENERGIES_keV, HDF5_DATASET_RAW_COUNTS, HDF5_DATASET_GAIN_CORRECTIONS, HDF5_DATASET_DARK_CURRENTS
from pysemeels.hdf5_sem_parameters import HDF5_ATTRIBUTE_ACCELERATING_VOLTAGE_V
from pysemeels.hitachi.eels_su.elv_text_file import *
from pysemeels.tools.hdf5_file_labels import *

# Globals and constants variables.


class TestRawSpectrum(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.raw_spectrum`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.name_ref = "TestRawSpectrum"
        self.spectrum = RawSpectrum(self.name_ref)

        self.test_data_path = get_current_module_path(__file__, '../test_data')

        self.name_import_ref = "30kV_7eV"
        self.import_sem_parameters = {HDF5_ATTRIBUTE_ACCELERATING_VOLTAGE_V: 30.0e3}
        self.elv_file_path = os.path.join(self.test_data_path, "hitachi/eels_su/30kV_7eV.elv")

        if not os.path.isfile(self.elv_file_path):
            raise SkipTest

        filepath = self.elv_file_path
        name = os.path.splitext(os.path.basename(filepath))[0]
        self.spectrum_import = RawSpectrum(name)
        self.spectrum_import.import_data(filepath, self.import_sem_parameters)

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

    def test_init(self):
        """
        Test __init__ method.
        """
        name_ref = "TestRawSpectrum_init"
        spectrum = RawSpectrum(name_ref)

        self.assertEqual(name_ref, spectrum.name)

        # self.fail("Test if the testcase is working.")

    def test_write_hdf5(self):
        """
        Test write_hdf5 method.
        """

        filepath = os.path.join(self.test_data_path, "test_raw_spectrum_write_hdf5.hdf5")
        with h5py.File(filepath, "w") as hdf5_file:

            self.spectrum.write_hdf5(hdf5_file)

            self.assertTrue(self.name_ref in hdf5_file)

            root_group = hdf5_file[self.name_ref]

        os.remove(filepath)

        # self.fail("Test if the testcase is working.")

    def test_read_hdf5(self):
        """
        Test read_hdf5 method.
        """

        filepath = os.path.join(self.test_data_path, "test_raw_spectrum_read_hdf5.hdf5")
        with h5py.File(filepath, "r") as hdf5_file:
            self.spectrum.read_hdf5(hdf5_file)

        # self.fail("Test if the testcase is working.")

    def test_read_hdf5_bad_project(self):
        """
        Test read_hdf5 method with a different project name.
        """

        name_ref = "TestProject_init"
        spectrum = RawSpectrum(name_ref)

        filepath = os.path.join(self.test_data_path, "test_raw_spectrum_read_hdf5.hdf5")
        with h5py.File(filepath, "r") as hdf5_file:
            self.assertRaises(ValueError, spectrum.read_hdf5, hdf5_file)

        # self.fail("Test if the testcase is working.")

    def test_import_data(self):
        """
        Test import_data method.
        """

        self.elv_file_path = os.path.join(self.test_data_path, "hitachi/eels_su/30kV_7eV.elv")

        if not os.path.isfile(self.elv_file_path):
            raise SkipTest

        filepath = self.elv_file_path
        name = os.path.splitext(os.path.basename(filepath))[0]
        spectrum = RawSpectrum(name)
        spectrum.import_data(filepath)

        self.assertEqual(-32.00, spectrum.energies_eV[0])
        self.assertEqual(2282, spectrum.raw_counts[0])
        self.assertEqual(21.84, spectrum.energies_eV[-1])
        self.assertEqual(0, spectrum.raw_counts[-1])
        self.assertEqual(1024, len(spectrum.energies_eV))
        self.assertEqual(1024, len(spectrum.raw_counts))

        self.assertEqual(0.918375, spectrum.gain_corrections[0])
        self.assertEqual(0.000000, spectrum.gain_corrections[-1])
        self.assertEqual(1024, len(spectrum.gain_corrections))

        self.assertEqual(2313, spectrum.dark_currents[0])
        self.assertEqual(0, spectrum.dark_currents[-1])
        self.assertEqual(1024, len(spectrum.dark_currents))

        # self.fail("Test if the testcase is working.")

    def test_import_data_write_hdf5(self):
        """
        Test import_data method.
        """

        self.assertEqual(-32.00, self.spectrum_import.energies_eV[0])
        self.assertEqual(2282, self.spectrum_import.raw_counts[0])
        self.assertEqual(21.84, self.spectrum_import.energies_eV[-1])
        self.assertEqual(0, self.spectrum_import.raw_counts[-1])
        self.assertEqual(1024, len(self.spectrum_import.energies_eV))
        self.assertEqual(1024, len(self.spectrum_import.raw_counts))

        self.assertEqual(0.918375, self.spectrum_import.gain_corrections[0])
        self.assertEqual(0.000000, self.spectrum_import.gain_corrections[-1])
        self.assertEqual(1024, len(self.spectrum_import.gain_corrections))

        self.assertEqual(2313, self.spectrum_import.dark_currents[0])
        self.assertEqual(0, self.spectrum_import.dark_currents[-1])
        self.assertEqual(1024, len(self.spectrum_import.dark_currents))

        filepath = os.path.join(self.test_data_path, "test_raw_spectrum_import_data_write_hdf5.hdf5")
        with h5py.File(filepath, "w") as hdf5_file:

            self.spectrum_import.write_hdf5(hdf5_file)

            self.assertTrue(self.name_import_ref in hdf5_file)

            root_group = hdf5_file[self.name_import_ref]

            self.assertTrue(HDF5_DATASET_ENERGIES_keV in root_group)
            self.assertTrue(HDF5_DATASET_RAW_COUNTS in root_group)
            self.assertTrue(HDF5_DATASET_GAIN_CORRECTIONS in root_group)
            self.assertTrue(HDF5_DATASET_DARK_CURRENTS in root_group)

            self.assertTrue(HDF5_GROUP_EXTRA_PARAMETERS in root_group)
            self.assertTrue(HDF5_ATTRIBUTE_ACCELERATING_VOLTAGE_V in root_group[HDF5_GROUP_EXTRA_PARAMETERS].attrs)

            self.assertTrue(HDF5_GROUP_EELS_PARAMETERS in root_group)
            self.assertTrue(HDF5_ATTRIBUTE_ACCELERATING_VOLTAGE_V in root_group[HDF5_GROUP_EELS_PARAMETERS].attrs)

        # os.remove(filepath)

        # self.fail("Test if the testcase is working.")

    def test_import_data_read_hdf5(self):
        """
        Test read_hdf5 method.
        """

        filepath = self.elv_file_path
        name = os.path.splitext(os.path.basename(filepath))[0]
        spectrum_read = RawSpectrum(name)
        filepath = os.path.join(self.test_data_path, "test_raw_spectrum_import_data_read_hdf5.hdf5")
        with h5py.File(filepath, "r") as hdf5_file:
            spectrum_read.read_hdf5(hdf5_file)

            self.assertEqual(self.name_import_ref, spectrum_read.name)

            self.assertTrue(HDF5_ATTRIBUTE_ACCELERATING_VOLTAGE_V in spectrum_read.extra_parameters)
            self.assertAlmostEqual(self.import_sem_parameters[HDF5_ATTRIBUTE_ACCELERATING_VOLTAGE_V],
                                   spectrum_read.extra_parameters[HDF5_ATTRIBUTE_ACCELERATING_VOLTAGE_V])

            self.assertEqual(-32.00, spectrum_read.energies_eV[0])
            self.assertEqual(21.84, spectrum_read.energies_eV[-1])
            self.assertEqual(1024, len(spectrum_read.energies_eV))

            self.assertEqual(2282, spectrum_read.raw_counts[0])
            self.assertEqual(0, spectrum_read.raw_counts[-1])
            self.assertEqual(1024, len(spectrum_read.raw_counts))

            self.assertEqual(0.918375, spectrum_read.gain_corrections[0])
            self.assertEqual(0.000000, spectrum_read.gain_corrections[-1])
            self.assertEqual(1024, len(spectrum_read.gain_corrections))

            self.assertEqual(2313, spectrum_read.dark_currents[0])
            self.assertEqual(0, spectrum_read.dark_currents[-1])
            self.assertEqual(1024, len(spectrum_read.dark_currents))

            self.assertEqual(-33.755274261603375, spectrum_read.counts[0])
            self.assertTrue(np.isnan(spectrum_read.counts)[-1])
            self.assertEqual(1024, len(spectrum_read.counts))

            parameters = spectrum_read.eels_parameters
            self.assertEqual("SU-EELS", parameters[HDF5_ATTRIBUTE_MODEL])
            self.assertEqual(0.0, parameters[HDF5_ATTRIBUTE_SAMPLE_HEIGHT_mm])
            self.assertEqual(r"D:\2017\System_baseline_march2017\30kV_7eV.elv", parameters[HDF5_ATTRIBUTE_FILEPATH])
            self.assertEqual("", parameters[HDF5_ATTRIBUTE_COMMENT])
            self.assertEqual("01/Mar/2017", parameters[HDF5_ATTRIBUTE_DATE])
            self.assertEqual("10:59", parameters[HDF5_ATTRIBUTE_TIME])
            self.assertEqual(30000, parameters[HDF5_ATTRIBUTE_ACCELERATING_VOLTAGE_V])
            self.assertEqual(7.0, parameters[HDF5_ATTRIBUTE_ENERGY_WIDTH_eV])
            self.assertEqual(0.0, parameters[HDF5_ATTRIBUTE_ENERGY_LOSS_eV])
            self.assertEqual(500, parameters[HDF5_ATTRIBUTE_SPEED_us])

            self.assertEqual("01/Mar/2017", parameters[HDF5_DATE])
            self.assertEqual("10:59", parameters[HDF5_TIME])
            self.assertEqual("", parameters[HDF5_COMMENT])
            self.assertEqual(500.0, parameters[HDF5_ACQUISITION_SPEED])
            self.assertEqual(0.0, parameters[HDF5_ENERGY_LOSS])
            self.assertEqual(98.7, parameters[HDF5_RAW])
            self.assertEqual(7.0, parameters[HDF5_ENERGY_WIDTH_eV])
            self.assertEqual(586, parameters[HDF5_DUAL_DET_POSITION])
            self.assertEqual(133, parameters[HDF5_DUAL_DET_POST])
            self.assertEqual(608, parameters[HDF5_DUAL_DET_CENTER])
            self.assertEqual(13575, parameters[HDF5_Q1])
            self.assertEqual(3850, parameters[HDF5_Q1S])
            self.assertEqual(0, parameters[HDF5_Q2])
            self.assertEqual(0, parameters[HDF5_Q2S])
            self.assertEqual(2700, parameters[HDF5_Q3])
            self.assertEqual(2900, parameters[HDF5_H1])
            self.assertEqual(6150, parameters[HDF5_H1S])
            self.assertEqual(-600, parameters[HDF5_H2])
            self.assertEqual(350, parameters[HDF5_H2S])
            self.assertEqual(0, parameters[HDF5_H4])
            self.assertEqual(0, parameters[HDF5_ELV_X])
            self.assertEqual(0, parameters[HDF5_ELV_Y])
            self.assertEqual(259, parameters[HDF5_SPECTRUM_ALIGNMENT_X])
            self.assertEqual(0, parameters[HDF5_SPECTRUM_ALIGNMENT_Y])
            self.assertEqual(-1500, parameters[HDF5_DET_SPEC_ALIGNMENT_X])
            self.assertEqual(470, parameters[HDF5_DET_SPEC_ALIGNMENT_Y])
            self.assertEqual(-1500, parameters[HDF5_DET_MAP_ALIGNMENT_X])
            self.assertEqual(1500, parameters[HDF5_DET_MAP_ALIGNMENT_Y])

            self.assertEqual(37443, parameters[HDF5_MAGNIFICATION])

        # self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
