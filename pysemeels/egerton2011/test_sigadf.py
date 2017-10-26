#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.egerton2011.test_sigadf

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.egerton2011.sigadf`.
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
from pysemeels.egerton2011.sigadf import sig_adf


# Globals and constants variables.

class TestSigAdf(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.egerton2011.sigadf`.
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
        result = sig_adf(6, 12, 20, 100, 100)

        self.assertAlmostEqual(20.2314, result.lenz_screening_angle_mrad, 4)
        self.assertAlmostEqual(667434.54739486391, result.rutherford_cross_section_barn, 4)
        self.assertAlmostEqual(667902.29509015649, result.mott_cross_section_barn, 4)

        #self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
