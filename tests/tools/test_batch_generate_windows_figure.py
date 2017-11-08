#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.tools.test_batch_generate_windows_figure

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.tools.batch_generate_windows_figure`.
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
from pysemeels.tools.batch_generate_windows_figure import BatchGenerateWindowsFigure
from pysemeels import get_current_module_path
from tests import is_bad_file

# Globals and constants variables.


class TestBatchGenerateWindowsFigure(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.tools.batch_generate_windows_figure`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.path = get_current_module_path(__file__, r"../../test_data")

        self.figures_file_path = get_current_module_path(__file__, r"../../test_data\hitachi\eels_su\SCNA9_EFSTEM_C_04\windows.png")

        if not os.path.isdir(self.path):  # pragma: no cover
            raise SkipTest

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

        if os.path.isfile(self.figures_file_path):
            os.remove(self.figures_file_path)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_generate(self):
        """
        Test generate method.
        """

        batch_generate_windows_figure = BatchGenerateWindowsFigure(self.path)

        self.assertFalse(os.path.isfile(self.figures_file_path))
        batch_generate_windows_figure.generate()
        self.assertTrue(os.path.isfile(self.figures_file_path))

        # self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
