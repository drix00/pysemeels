#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.test_project

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`pysemeels.project`.
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

# Local modules.

# Project modules.
from pysemeels import get_current_module_path
from pysemeels.project import Project, HDF5_ATTRIBUTE_AUTHOR

# Globals and constants variables.


class TestProject(unittest.TestCase):
    """
    TestCase class for the module `pysemeels.project`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.name_ref = "TestProject"
        self.project = Project(self.name_ref)

        self.test_data_path = get_current_module_path(__file__, '../test_data')

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
        name_ref = "TestProject_init"
        project = Project(name_ref)

        self.assertEqual(name_ref, project.name)

        # self.fail("Test if the testcase is working.")

    def test_write_hdf5(self):
        """
        Test write_hdf5 method.
        """

        filepath = os.path.join(self.test_data_path, "test_project_write_hdf5.hdf5")
        with h5py.File(filepath, "w") as hdf5_file:
            author_ref = "Hendrix Demers"
            self.project.author = author_ref

            self.project.write_hdf5(hdf5_file)

            self.assertTrue(self.name_ref in hdf5_file)

            root_group = hdf5_file[self.name_ref]
            self.assertEqual(author_ref, root_group.attrs[HDF5_ATTRIBUTE_AUTHOR])

        # self.fail("Test if the testcase is working.")

        # os.remove(filepath)

    def test_read_hdf5(self):
        """
        Test read_hdf5 method.
        """

        filepath = os.path.join(self.test_data_path, "test_project_read_hdf5.hdf5")
        with h5py.File(filepath, "r") as hdf5_file:
            self.project.read_hdf5(hdf5_file)

            author_ref = "Hendrix Demers"
            self.assertEqual(author_ref, self.project.author)

        # self.fail("Test if the testcase is working.")

    def test_read_hdf5_bad_project(self):
        """
        Test read_hdf5 method with a different project name.
        """

        name_ref = "TestProject_init"
        project = Project(name_ref)

        filepath = os.path.join(self.test_data_path, "test_project_read_hdf5.hdf5")
        with h5py.File(filepath, "r") as hdf5_file:
            self.assertRaises(ValueError, project.read_hdf5, hdf5_file)

        # self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose
    nose.runmodule()