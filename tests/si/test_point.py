#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.si.test_point

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.si.point`.
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
import os

# Third party modules.
import h5py
from nose import SkipTest

# Local modules.

# Project modules.
from pysemeels import get_current_module_path
from pysemeels.si.point import Point
from tests import is_bad_file

# Globals and constants variables.


class TestPoint(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.si.point`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.name_ref = "TestPoint"
        self.point = Point(self.name_ref)

        self.test_data_path = get_current_module_path(__file__, '../../test_data')

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

    def test_init(self):
        """
        Test __init__ method.
        """
        name_ref = "TestPoint_init"
        point = Point(name_ref)

        self.assertEqual(name_ref, point.name)

        # self.fail("Test if the testcase is working.")

    def test_write_hdf5(self):
        """
        Test write_hdf5 method.
        """

        filepath = os.path.join(self.test_data_path, "test_point_write_hdf5.hdf5")
        with h5py.File(filepath, "w") as hdf5_file:

            self.point.write_hdf5(hdf5_file)

            self.assertTrue(self.name_ref in hdf5_file)

            root_group = hdf5_file[self.name_ref]

        os.remove(filepath)

        # self.fail("Test if the testcase is working.")

    def test_read_hdf5(self):
        """
        Test read_hdf5 method.
        """

        filepath = os.path.join(self.test_data_path, "test_point_read_hdf5.hdf5")
        if is_bad_file(filepath):
            raise SkipTest

        with h5py.File(filepath, "r") as hdf5_file:
            self.point.read_hdf5(hdf5_file)

        # self.fail("Test if the testcase is working.")

    def test_read_hdf5_bad_project(self):
        """
        Test read_hdf5 method with a different project name.
        """

        name_ref = "TestPoint_init"
        point = Point(name_ref)

        filepath = os.path.join(self.test_data_path, "test_point_read_hdf5.hdf5")
        if is_bad_file(filepath):
            raise SkipTest

        with h5py.File(filepath, "r") as hdf5_file:
            self.assertRaises(ValueError, point.read_hdf5, hdf5_file)

        # self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
