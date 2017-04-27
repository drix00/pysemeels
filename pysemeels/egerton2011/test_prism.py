#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.egerton2011.test_prism
   :synopsis: Tests for the module :py:mod:`pysemeels.egerton2011.prism`

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.egerton2011.prism`.
"""

###############################################################################
# Copyright ${year} Hendrix Demers
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
from pysemeels.egerton2011.prism import prism


# Globals and constants variables.

class TestPrism(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.egerton2011.prism`.
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


    def testBookExample(self):
        """
        Test from value given in the Egerton (2011) book.
        """
        result1, result2 = prism(620, 16, 47, 0.4, 1.25, 100, 90, 90)

        self.assertAlmostEqual(90.0, result1.v)
        self.assertAlmostEqual(-0.0121215, result1.x)
        self.assertAlmostEqual(-0.00322115, result1.xp)
        #self.assertAlmostEqual(-0.0480911, result1.y)
        #self.assertAlmostEqual(-0.00742323, result1.yp)
        self.assertAlmostEqual(-0.038228748388716927, result1.y)
        self.assertAlmostEqual(-0.0060215355528009697, result1.yp)

        self.assertAlmostEqual(86.2369, result2.v, 4)
        self.assertAlmostEqual(0.0, result2.x, 5)
        self.assertAlmostEqual(-0.00322115, result2.xp, 5)
        #self.assertAlmostEqual(-0.0201568, result2.y, 5)
        #self.assertAlmostEqual(-0.00742323, result2.yp, 5)
        self.assertAlmostEqual(-0.015569183272023723, result2.y, 5)
        self.assertAlmostEqual(-0.0060215355528009697, result2.yp, 5)

        #self.fail("Test if the testcase is working.")

    def testWebsiteExample(self):
        """
        Test from value given in the Egerton (2011) book website.
        """
        result1, result2 = prism(100, 0, 45, 0.4, 10, 3, 30, 100)

        self.assertAlmostEqual(100.0, result1.v)
        self.assertAlmostEqual(1.44479, result1.x, 5)
        self.assertAlmostEqual(0.0135669, result1.xp, 5)
        self.assertAlmostEqual(-6.5563, result1.y, 5)
        self.assertAlmostEqual(-0.068742, result1.yp, 5)

        self.assertAlmostEqual(-6.49395, result2.v, 5)
        self.assertAlmostEqual(0.0, result2.x, 5)
        self.assertAlmostEqual(0.0135669, result2.xp, 5)
        self.assertAlmostEqual(0.764315, result2.y, 5)
        self.assertAlmostEqual(-0.068742, result2.yp, 5)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
