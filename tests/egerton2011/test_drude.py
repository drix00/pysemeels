#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.egerton2011.test_drude

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.egerton2011.drude`.
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
import pytest

# Local modules.

# Project modules.
from pysemeels.egerton2011.drude import drude
from pysemeels import get_current_module_path
from tests import is_bad_file

# Globals and constants variables.


class TestDrude(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.egerton2011.drude`.
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

    def testWebsiteExample(self):
        """
        Test from value given in the Egerton (2011) book website.
        """
        # Drude(ep,ew,eb,epc,e0,beta,nn,tnm)
        energies_eV, eps1, eps2, im_eps, im4_eps, re_eps, probabilities_total, probabilities_volume, probabilities_surface, ps, pv, mfp_volume_nm, mfp_free_nm = drude(15, 3, 0, 0.1, 200, 5, 500, 50)

        self.assertEqual(500, len(eps1))
        self.assertEqual(500, len(eps2))
        self.assertEqual(500, len(im_eps))
        self.assertEqual(500, len(im4_eps))
        self.assertEqual(500, len(re_eps))
        self.assertEqual(500, len(probabilities_total))
        self.assertEqual(500, len(probabilities_volume))
        self.assertEqual(500, len(probabilities_surface))

        self.assertAlmostEqual(0.0163826, ps, 7)
        # self.assertAlmostEqual(0.254905, pv, 6)
        self.assertAlmostEqual(0.25491101951346251, pv, 6)
        # self.assertAlmostEqual(196.151, mfp_volume_nm, 3)
        self.assertAlmostEqual(196.14687546828225, mfp_volume_nm, 3)
        self.assertAlmostEqual(183.836505, mfp_free_nm, 6)

        test_data_file_path = get_current_module_path(__file__, "../../test_data/egerton2011/Drude.ssd")
        if is_bad_file(test_data_file_path):
            pytest.skip("File not found: {}".format(test_data_file_path))

        with open(test_data_file_path, 'r') as ref_file:
            lines = ref_file.readlines()

            for channel_id, line in enumerate(lines):
                items = line.split()

                xx = float(items[0])
                yy = float(items[1])

                self.assertAlmostEqual(xx, energies_eV[channel_id], 7)
                self.assertAlmostEqual(yy, probabilities_total[channel_id], 7, channel_id)

        test_data_file_path = get_current_module_path(__file__, "../../test_data/egerton2011/Drude.eps")
        if is_bad_file(test_data_file_path):
            pytest.skip("File not found: {}".format(test_data_file_path))

        with open(test_data_file_path, 'r') as ref_file:
            lines = ref_file.readlines()

            for channel_id, line in enumerate(lines):
                items = line.split()

                xx = float(items[0])
                yy = float(items[1])
                yy2 = float(items[2])

                self.assertAlmostEqual(xx, energies_eV[channel_id], 7)
                self.assertAlmostEqual(yy, eps1[channel_id], 7, channel_id)
                self.assertAlmostEqual(yy2, eps2[channel_id], 7, channel_id)

        # self.fail("Test if the testcase is working.")

    def testBookExample(self):
        """
        Test from value given in the Egerton (2011) book.
        """
        # Drude(ep,ew,eb,epc,e0,beta,nn,tnm)
        energies_eV, eps1, eps2, im_eps, im4_eps, re_eps, probabilities_total, probabilities_volume, probabilities_surface, ps, pv, mfp_volume_nm, mfp_free_nm = drude(15, 2, 0, 0.1, 100, 5, 300, 50)

        self.assertEqual(300, len(eps1))
        self.assertEqual(300, len(eps2))
        self.assertEqual(300, len(im_eps))
        self.assertEqual(300, len(im4_eps))
        self.assertEqual(300, len(re_eps))
        self.assertEqual(300, len(probabilities_total))
        self.assertEqual(300, len(probabilities_volume))
        self.assertEqual(300, len(probabilities_surface))

        self.assertAlmostEqual(0.0207314, ps, 6)
        self.assertAlmostEqual(0.36060575292202401, pv, 6)
        self.assertAlmostEqual(138.65558049156195, mfp_volume_nm, 3)
        self.assertAlmostEqual(131.691587, mfp_free_nm, 6)

        # self.fail("Test if the testcase is working.")
