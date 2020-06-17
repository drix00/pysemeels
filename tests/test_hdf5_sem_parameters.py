#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.test_hdf5_sem_parameters

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.hdf5_sem_parameters`.
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

# Local modules.

# Project modules.
from pysemeels.hdf5_sem_parameters import *

# Globals and constants variables.


class TestEftem(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.hdf5_sem_parameters`.
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

    def test_parameters(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        self.assertEqual("instruct name", HDF5_ATTRIBUTE_INSTRUCT_NAME)
        self.assertEqual("accelerating voltage (V)", HDF5_ATTRIBUTE_ACCELERATING_VOLTAGE_V)
        self.assertEqual("deceleration voltage (V)", HDF5_ATTRIBUTE_DECELERATION_VOLTAGE_V)
        self.assertEqual("working distance (um)", HDF5_ATTRIBUTE_WORKING_DISTANCE_um)
        self.assertEqual("emission current (nA)", HDF5_ATTRIBUTE_EMISSION_CURRENT_nA)
        self.assertEqual("specimen bias (V)", HDF5_ATTRIBUTE_SPECIMEN_BIAS_V)
        self.assertEqual("dynamic focus", HDF5_ATTRIBUTE_DYNAMIC_FOCUS)

        self.assertEqual("condenser aperture size id", HDF5_ATTRIBUTE_CONDENSER_APERTURE_SIZE_ID)
        self.assertEqual("objective aperture size id", HDF5_ATTRIBUTE_OBJECTIVE_APERTURE_SIZE_ID)
        self.assertEqual("bright field aperture size id", HDF5_ATTRIBUTE_BRIGHT_FIELD_APERTURE_SIZE_ID)

        # self.fail("Test if the testcase is working.")
