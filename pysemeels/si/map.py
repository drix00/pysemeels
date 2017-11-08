#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.si.map

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Spectral imaging map EELS data.
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
import os.path

# Third party modules.

# Local modules.

# Project modules.
from pysemeels.hitachi.eels_su.map.ana_file import AnaFile
from pysemeels.hitachi.eels_su.map.text_file import TextParameters

# Globals and constants variables.
HDF5_GROUP_SPECTRA_1 = "spectra 1"
HDF5_GROUP_SPECTRA_2 = "spectra 2"
HDF5_GROUP_SPECTRA_3 = "spectra 3"


class Map(object):
    """
    Container for spectral imaging map EELS data.
    """
    def __init__(self, name):
        """

        :param str name: Name of the spectral imaging map EELS data folder.
        """
        self.name = name

        self.extra_parameters = {}
        self.eels_parameters = {}

        self.energies_eV = None

    def read_hdf5(self, parent_group):
        if self.name in parent_group:
            project_group = parent_group[self.name]
        else:
            raise ValueError("The parent group does not contain the project")

    def write_hdf5(self, parent_group):
        project_group = parent_group.require_group(self.name)

    def import_data(self, folder, extra_parameters=None):
        """
        Import the EELS spectral map data (ana file).

        :param str folder: Folder that contain the .ana file.
        :param dict extra_parameters: Extra parameters to add as attribute in this data group.
        :return: None.
        """
        if extra_parameters:
            self.extra_parameters.update(extra_parameters)

        for data_id in [1, 2, 3]:
            filename = "spectra_{}.ana".format(data_id)
            filepath = os.path.join(folder, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'r') as ana_file:
                    ana_file_data = AnaFile()
                    ana_file_data.read(ana_file)

                    self.energies_eV = ana_file_data.energies_eV
                    # self.energies_eV = np.array(elv_data.energies_eV)
                    # self.raw_counts = np.array(elv_data.raw_counts)
                    # self.gain_corrections = np.array(elv_data.gain_corrections)
                    # self.dark_currents = np.array(elv_data.dark_currents)
                    #
                    # self.eels_parameters.update(elv_data.parameters())

        name = os.path.basename(folder)
        filepath_txt = os.path.join(folder, name + ".txt")
        with open(filepath_txt, 'r', encoding="UTF-16") as text_file:
            text_parameters = TextParameters()
            text_parameters.read(text_file)

            # self.eels_parameters.update(text_parameters.items())
