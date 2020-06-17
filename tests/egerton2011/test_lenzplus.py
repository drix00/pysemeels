#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.egerton2011.test_lenzplus

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.egerton2011.lenzplus`.
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
from pysemeels.egerton2011.lenzplus import lenz_plus


# Globals and constants variables.

class TestSigAdf(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.egerton2011.lenzplus`.
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

        .. todo:: Check why some values on the website are wrong.
        """
        result1, result2, result3_wo_broadening, result3_w_broadening = lenz_plus(100, 40, 6, 10, 1.5)

        self.assertAlmostEqual(2.0231e-2, result1.theta0_rad, 6)
        self.assertAlmostEqual(2.1783e-4, result1.thetae_rad_rad, 8)
        #self.assertAlmostEqual(3.4137e-2, result1.dse_domega, 6)
        self.assertAlmostEqual(5.4622e-1, result1.dse_domega, 5)
        self.assertAlmostEqual(5.2233e-2, result1.dsi_domega, 6)
        #self.assertAlmostEqual(2.1452, result1.dse_dbeta, 4)
        self.assertAlmostEqual(3.4324e-2, result1.dse_dbeta, 6)
        #self.assertAlmostEqual(3.2823, result1.dsi_dbeta, 4)
        self.assertAlmostEqual(3.2823e-3, result1.dsi_dbeta, 7)
        self.assertAlmostEqual(1.3337e-5, result1.sigma_elastic_nm2, 9)
        self.assertAlmostEqual(1.6835e-4, result1.sigma_inelastic_nm2, 8)
        self.assertAlmostEqual(1.9634e-1, result1.f_elastic, 5)
        self.assertAlmostEqual(8.2043e-1, result1.f_inelastic, 5)
        self.assertAlmostEqual(3.0209, result1.total_inelastic_elastic_ratio, 4)

        self.assertAlmostEqual(1.2306, result2.t_lambda_beta, 4)

        self.assertAlmostEqual(1.3580e-1, result3_wo_broadening.p_unscat, 5)
        self.assertAlmostEqual(1.7146E-02, result3_wo_broadening.p_el, 6)
        self.assertAlmostEqual(3.8792E-01, result3_wo_broadening.p_inel, 5)
        self.assertAlmostEqual(4.8977E-02, result3_wo_broadening.p_total, 6)
        self.assertAlmostEqual(1.5295E-01, result3_wo_broadening.I0_I, 5)
        self.assertAlmostEqual(4.3690E-01, result3_wo_broadening.Ii_I, 5)
        self.assertAlmostEqual(1.3498, result3_wo_broadening.lnIt_I0, 4)

        self.assertAlmostEqual(1.3580e-1, result3_w_broadening.p_unscat, 5)
        self.assertAlmostEqual(1.4689E-02, result3_w_broadening.p_el, 6)
        self.assertAlmostEqual(3.2911E-01, result3_w_broadening.p_inel, 5)
        self.assertAlmostEqual(3.5598E-02, result3_w_broadening.p_total, 6)
        self.assertAlmostEqual(1.5049E-01, result3_w_broadening.I0_I, 5)
        self.assertAlmostEqual(3.6471E-01, result3_w_broadening.Ii_I, 5)
        self.assertAlmostEqual(1.2306, result3_w_broadening.lnIt_I0, 4)

        #self.fail("Test if the testcase is working.")
