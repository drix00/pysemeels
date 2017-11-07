#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.eftem

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

EELS EFTEM and electron micrograph data.
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

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.


class Eftem(object):
    """
    Container of the EELS EFTEM and electron micrographs.
    """
    def __init__(self, name):
        """

        :param str name: name of the set of micrographs.
        """
        self.name = name

    def read_hdf5(self, parent_group):
        """
        Read the micrographs from the HDF5 parent group.

        :param `h5py.group` parent_group: read the data from this group.
        :return: None.
        :raises ValueError: If the parent group `parent_group` does not have the correct name.
        """
        if self.name in parent_group:
            project_group = parent_group[self.name]
        else:
            raise ValueError("The parent group does not contain the project")

    def write_hdf5(self, parent_group):
        """
        Write the micrographs into the parent group `parent_group`.

        :param `h5py.group` parent_group: write micrographs into this group.
        :return: None.
        """
        project_group = parent_group.require_group(self.name)
