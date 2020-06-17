#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.tools.test_batch_convert_elv

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.tools.batch_convert_elv`.
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
import sys

# Third party modules.
import pytest

# Local modules.

# Project modules.
from pysemeels.tools.batch_convert_elv import BatchConvertElv
from pysemeels import get_current_module_path
from tests import is_bad_file

# Globals and constants variables.


class TestBatchConvertElv(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.tools.batch_convert_elv`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.path = get_current_module_path(__file__, r"../../test_data\hitachi\eels_su")
        self.msa_file_path_1 = get_current_module_path(__file__, r"../../test_data\hitachi\eels_su\30kV_7eV.msa")
        self.msa_file_path_2 = get_current_module_path(__file__, r"../../test_data\hitachi\eels_su\SCNA9_EFSTEM_C_04\windows.msa")

        if not os.path.isdir(self.path):  # pragma: no cover
            pytest.skip("File not found: {}".format(self.path))

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

        if os.path.isfile(self.msa_file_path_1):
            os.remove(self.msa_file_path_1)
        if os.path.isfile(self.msa_file_path_2):
            os.remove(self.msa_file_path_2)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    @pytest.mark.skipif(sys.platform != "win32", reason="only run on windows")
    def test_generate(self):
        """
        Test generate method.
        """

        batch_convert_elv = BatchConvertElv(self.path, recursive=False)

        self.assertFalse(os.path.isfile(self.msa_file_path_1))
        self.assertFalse(os.path.isfile(self.msa_file_path_2))
        batch_convert_elv.convert()
        self.assertTrue(os.path.isfile(self.msa_file_path_1))
        self.assertFalse(os.path.isfile(self.msa_file_path_2))

        # self.fail("Test if the testcase is working.")

    @pytest.mark.skipif(sys.platform != "win32", reason="only run on windows")
    def test_generate_recursive(self):
        """
        Test generate method.
        """

        batch_convert_elv = BatchConvertElv(self.path, recursive=True)

        self.assertFalse(os.path.isfile(self.msa_file_path_1))
        self.assertFalse(os.path.isfile(self.msa_file_path_2))
        batch_convert_elv.convert()
        self.assertTrue(os.path.isfile(self.msa_file_path_1))
        self.assertTrue(os.path.isfile(self.msa_file_path_2))

        # self.fail("Test if the testcase is working.")
