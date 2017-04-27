#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.egerton2011.test_spec_gen
   :synopsis: Tests for the module :py:mod:`pysemeels.egerton2011.spec_gen`

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.egerton2011.spec_gen`.
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
from pysemeels.egerton2011.spec_gen import spec_gen
from pysemeels import get_current_module_path

# Globals and constants variables.

class TestSpecGen(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.egerton2011.spec_gen`.
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
        eout, outssd, outpsd = spec_gen(16.7, 3.2, 1, 5, 0.1, 10000, 1.5, 1000, 2, 0.5, 10)

        self.assertEqual(1000, len(eout))
        self.assertEqual(1000, len(outssd))
        self.assertEqual(1000, len(outpsd))

        test_data_file_path = get_current_module_path(__file__, "../../test_data/egerton2011/SpecGen.ssd")
        with open(test_data_file_path, 'r') as ref_file:
            lines = ref_file.readlines()

            for channel_id, line in enumerate(lines):
                items = line.split()

                xx = float(items[0])
                yy = float(items[1])

                self.assertAlmostEqual(xx, eout[channel_id], 7)
                self.assertAlmostEqual(yy, outssd[channel_id], 7, channel_id)

        test_data_file_path = get_current_module_path(__file__, "../../test_data/egerton2011/SpecGen.psd")
        with open(test_data_file_path, 'r') as ref_file:
            lines = ref_file.readlines()

            for channel_id, line in enumerate(lines):
                items = line.split()

                xx = float(items[0])
                yy = float(items[1])

                self.assertAlmostEqual(xx, eout[channel_id], 7)
                self.assertAlmostEqual(yy, outpsd[channel_id], 7, channel_id)

        #self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
