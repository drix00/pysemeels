#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.raw_spectrum

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Raw EELS spectrum data.
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
import numpy as np

# Local modules.

# Project modules.
from pysemeels.hitachi.eels_su.elv_file import ElvFile
from pysemeels.hitachi.eels_su.elv_text_file import ElvTextParameters

# Globals and constants variables.
#:
HDF5_GROUP_EXTRA_PARAMETERS = "extra parameters"
#:
HDF5_GROUP_EELS_PARAMETERS = "eels parameters"

#:
HDF5_DATASET_ENERGIES_keV = "energies eV"
#:
HDF5_DATASET_RAW_COUNTS = "raw counts"
#:
HDF5_DATASET_GAIN_CORRECTIONS = "gain corrections"
#:
HDF5_DATASET_DARK_CURRENTS = "dark currents"


class RawSpectrum(object):
    """
    Container for raw EELS spectrum data.
    """
    def __init__(self, name):
        """

        :param str name: Name of the raw EELS spectrum data.
        """
        self.name = name

        self.extra_parameters = {}
        self.eels_parameters = {}

        self.energies_eV = None
        self.raw_counts = None
        self.gain_corrections = None
        self.dark_currents = None

    def read_hdf5(self, parent_group):
        """
        Read the raw EELS spectrum from the HDF5 parent group.

        :param `h5py.group` parent_group: read the data from this group.
        :return: None.
        :raises ValueError: If the parent group `parent_group` does not have the correct name.
        """
        if self.name in parent_group:
            project_group = parent_group[self.name]

            if HDF5_GROUP_EXTRA_PARAMETERS in project_group:
                extra_parameters_group = project_group[HDF5_GROUP_EXTRA_PARAMETERS]
                for name in extra_parameters_group.attrs:
                    self.extra_parameters[name] = extra_parameters_group.attrs[name]

            if HDF5_GROUP_EELS_PARAMETERS in project_group:
                eels_parameters_group = project_group[HDF5_GROUP_EELS_PARAMETERS]
                for name in eels_parameters_group.attrs:
                    self.eels_parameters[name] = eels_parameters_group.attrs[name]

            if HDF5_DATASET_ENERGIES_keV in project_group:
                self.energies_eV = project_group[HDF5_DATASET_ENERGIES_keV][...]

            if HDF5_DATASET_RAW_COUNTS in project_group:
                self.raw_counts = project_group[HDF5_DATASET_RAW_COUNTS][...]

            if HDF5_DATASET_GAIN_CORRECTIONS in project_group:
                self.gain_corrections = project_group[HDF5_DATASET_GAIN_CORRECTIONS][...]

            if HDF5_DATASET_DARK_CURRENTS in project_group:
                self.dark_currents = project_group[HDF5_DATASET_DARK_CURRENTS][...]

        else:
            raise ValueError("The parent group does not contain the project")

    def write_hdf5(self, parent_group):
        """
        Write the raw EELS spectrum into the parent group `parent_group`.

        :param `h5py.group` parent_group: write data into this group.
        :return: None.
        """
        project_group = parent_group.require_group(self.name)

        if self.extra_parameters:
            parameters_group = project_group.require_group(HDF5_GROUP_EXTRA_PARAMETERS)
            for name in self.extra_parameters:
                parameters_group.attrs[name] = self.extra_parameters[name]

        if self.eels_parameters:
            parameters_group = project_group.require_group(HDF5_GROUP_EELS_PARAMETERS)
            for name in self.eels_parameters:
                parameters_group.attrs[name] = self.eels_parameters[name]

        if self.energies_eV is not None:
            project_group.create_dataset(HDF5_DATASET_ENERGIES_keV, data=self.energies_eV)

        if self.raw_counts is not None:
            project_group.create_dataset(HDF5_DATASET_RAW_COUNTS, data=self.raw_counts)

        if self.gain_corrections is not None:
            project_group.create_dataset(HDF5_DATASET_GAIN_CORRECTIONS, data=self.gain_corrections)

        if self.dark_currents is not None:
            project_group.create_dataset(HDF5_DATASET_DARK_CURRENTS, data=self.dark_currents)

    def import_data(self, filepath, extra_parameters=None):
        """
        Import the raw EELS spectrum data (elv file).

        :param str filepath: File path of the .elv file.
        :param dict extra_parameters: Extra parameters to add as attribute in this data group.
        :return: None.
        """
        if extra_parameters:
            self.extra_parameters.update(extra_parameters)

        with open(filepath, 'r') as elv_file:
            elv_data = ElvFile()
            elv_data.read(elv_file)

            self.energies_eV = np.array(elv_data.energies_eV)
            self.raw_counts = np.array(elv_data.raw_counts)
            self.gain_corrections = np.array(elv_data.gain_corrections)
            self.dark_currents = np.array(elv_data.dark_currents)

            self.eels_parameters.update(elv_data.parameters())

        filepath_txt = os.path.splitext(filepath)[0] + ".txt"
        with open(filepath_txt, 'r', encoding="UTF-16") as elv_text_file:
            elv_text_parameters = ElvTextParameters()
            elv_text_parameters.read(elv_text_file)

            self.eels_parameters.update(elv_text_parameters.items())

    @property
    def counts(self):
        """
        Compute the net counts of the EELS spectrum.

        The corrected or net counts are calculated for each channel as

        .. math::
            N = \\frac{C - D}{G}

        where

            - :math:`N` is the net count
            - :math:`C` is the raw count
            - :math:`D` is the dark current
            - :math:`G` is the gain correction

        :return: Counts corrected for grain and dark current.
        :rtype: `np.array`
        """
        corrected_counts = (self.raw_counts - self.dark_currents) / self.gain_corrections
        return corrected_counts
