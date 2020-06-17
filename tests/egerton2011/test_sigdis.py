#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.egerton2011.test_sigdis

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.egerton2011.sigdis`.
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
from pysemeels.egerton2011.sigdis import sigdis


# Globals and constants variables.

class TestSigDis(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.egerton2011.sigdis`.
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

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def testWebsiteExample(self):
        """
        Test from value given in the Egerton (2011) book website.
        """
        result = sigdis(6, 12, 10, 200)

        self.assertAlmostEqual(43.7334, result.emax_eV, 4)
        self.assertAlmostEqual(52.006, result.threshold_keV, 4)
        self.assertAlmostEqual(20.9125, result.emin_eV, 4)
        self.assertAlmostEqual(66.9327, result.spherical_escape_potential_barn, 4)
        self.assertAlmostEqual(21.6523, result.planar_escape_potential_barn, 4)
        self.assertAlmostEqual(54.101, result.spherical_potential_barn, 4)
        self.assertAlmostEqual(14.863, result.planar_potential_barn, 4)

        #self.fail("Test if the testcase is working.")
