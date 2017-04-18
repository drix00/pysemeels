#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: xrayspectrummodeling.map.test_simulation_data
   :synopsis: Tests for the module :py:mod:`xrayspectrummodeling.map.simulation_data as simulation_data`

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`xrayspectrummodeling.map.simulation_data as simulation_data`.
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

# Local modules.

# Project modules.
from pysemeels import get_current_module_path
from pysemeels.hitachi.eels_su.elv_file import ElvFile

# Globals and constants variables.

class TestSimulationData(unittest.TestCase):
    """
    TestCase class for the module `xrayspectrummodeling.map.simulation_data`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.ana_file_path = get_current_module_path(__file__, "../../../test_data/hitachi/eels_su/30kV_7eV.elv")

        if not os.path.isfile(self.ana_file_path):
            raise SkipTest

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

    def test_read_file(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        with open(self.ana_file_path, 'r') as elv_text_file:
            elv_file = ElvFile()
            elv_file.read(elv_text_file)

            self.assertEqual("01/Mar/2017", elv_file.date)
            self.assertEqual("10:59", elv_file.time)
            self.assertEqual("", elv_file.comment)
            self.assertEqual("500µs", elv_file.dose)
            self.assertEqual("0.0eV", elv_file.le)
            self.assertEqual(98.7, elv_file.raw)
            self.assertEqual("7.0eV", elv_file.energy_width)
            self.assertEqual("586ch", elv_file.dual_det_position)
            self.assertEqual("133ch", elv_file.dual_det_post)
            self.assertEqual("608ch", elv_file.dual_det_center)
            self.assertEqual(13575, elv_file.q1)
            self.assertEqual(3850, elv_file.q1s)
            self.assertEqual(0, elv_file.q2)
            self.assertEqual(0, elv_file.q2s)
            self.assertEqual(2700, elv_file.q3)
            self.assertEqual(2900, elv_file.h1)
            self.assertEqual(6150, elv_file.h1s)
            self.assertEqual(-600, elv_file.h2)
            self.assertEqual(350, elv_file.h2s)
            self.assertEqual(0, elv_file.h4)
            self.assertEqual(0, elv_file.elv_x)
            self.assertEqual(0, elv_file.elv_y)
            self.assertEqual(259, elv_file.spectrum_alignment_x)
            self.assertEqual(0, elv_file.spectrum_alignment_y)
            self.assertEqual(-1500, elv_file.det_spec_alignment_x)
            self.assertEqual(470, elv_file.det_spec_alignment_y)
            self.assertEqual(-1500, elv_file.det_map_alignment_x)
            self.assertEqual(1500, elv_file.det_map_alignment_y)

            self.assertEqual(37443, elv_file.mag)

            self.assertEqual(-32.00, elv_file.energies_eV[0])
            self.assertEqual(2282, elv_file.counts[0])
            self.assertEqual(21.84, elv_file.energies_eV[-1])
            self.assertEqual(0, elv_file.counts[-1])
            self.assertEqual(1024, len(elv_file.energies_eV))
            self.assertEqual(1024, len(elv_file.counts))

            self.assertEqual(0.918375, elv_file.gain_corrections[0])
            self.assertEqual(0.000000, elv_file.gain_corrections[-1])
            self.assertEqual(1024, len(elv_file.gain_corrections))

            self.assertEqual(2313, elv_file.dark_currents[0])
            self.assertEqual(0, elv_file.dark_currents[-1])
            self.assertEqual(1024, len(elv_file.dark_currents))

        #self.fail("Test if the testcase is working.")
        self.assert_(True)


if __name__ == '__main__':  # pragma: no cover
    import nose
    nose.runmodule()
