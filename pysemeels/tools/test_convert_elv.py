#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.tools.test_convert_elv
   :synopsis: Tests for the module :py:mod:`pysemeels.tools.convert_elv`

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.tools.convert_elv`.
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
from pysemeels.tools.convert_elv import ConvertElv
from pysemeels import get_current_module_path


# Globals and constants variables.

class TestConvertElv(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.tools.convert_elv`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.elv_file_path = get_current_module_path(__file__, "../../test_data/hitachi/eels_su/30kV_7eV.elv")
        self.msa_file_path = get_current_module_path(__file__, "../../test_data/hitachi/eels_su/30kV_7eV.msa")
        self.hdf5_file_path = get_current_module_path(__file__, "../../test_data/hitachi/eels_su/30kV_7eV.hdf5")

        if not os.path.isfile(self.elv_file_path): # pragma: no cover
            raise SkipTest

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

        if os.path.isfile(self.msa_file_path):
            os.remove(self.msa_file_path)

        if os.path.isfile(self.hdf5_file_path):
            os.remove(self.hdf5_file_path)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        # self.fail("Test if the testcase is working.")
        self.assert_(True)


    def test_convert(self):
        """
        Test the convert method.
        """
        convert_elv = ConvertElv(self.elv_file_path)
        convert_elv.convert_msa = True
        convert_elv.convert_hdf5 = False

        self.assertFalse(os.path.isfile(self.msa_file_path))
        self.assertFalse(os.path.isfile(self.hdf5_file_path))
        convert_elv.convert()
        self.assertTrue(os.path.isfile(self.msa_file_path))
        self.assertFalse(os.path.isfile(self.hdf5_file_path))

        # self.fail("Test if the testcase is working.")

if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
