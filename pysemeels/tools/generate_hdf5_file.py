# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.tools.generate_hdf5_file

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Generate HDF5 file from Hitachi EELS data.
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
import logging

# Third party modules.
import numpy as np

# Local modules.

# Project modules.
from pysemeels.hitachi.eels_su.elv_text_file import ElvTextParameters
from pysemeels.hitachi.eels_su.elv_file import ElvFile
from pysemeels.tools.hdf5_file_labels import *

# Globals and constants variables.


class GenerateHdf5File(object):
    def __init__(self, hdf5_file):
        self.hdf5_file = hdf5_file

    def add_spectrum(self, file_path, name=None):
        if name is None:
            basename, _extension = os.path.splitext(os.path.basename(file_path))
            name = basename

        spectrum_group = self.hdf5_file.create_group(name)

        elv_text_file_path, _extension = os.path.splitext(file_path)
        elv_text_file_path += '.txt'
        with open(elv_text_file_path, 'r', encoding="UTF-16", errors='ignore') as elv_text_file:
            elv_text_parameters = ElvTextParameters()
            elv_text_parameters.read(elv_text_file)

            spectrum_group.attrs[HDF5_MODEL] = elv_text_parameters.model
            spectrum_group.attrs[HDF5_SAMPLE_HEIGHT] = elv_text_parameters.sample_height_mm
            spectrum_group.attrs[HDF5_FILE_PATH] = elv_text_parameters.file_name
            spectrum_group.attrs[HDF5_COMMENT] = elv_text_parameters.comment
            spectrum_group.attrs[HDF5_DATE] = elv_text_parameters.date
            spectrum_group.attrs[HDF5_TIME] = elv_text_parameters.time
            spectrum_group.attrs[HDF5_ACCELERATING_VOLTAGE_V] = elv_text_parameters.accelerating_voltage_V
            spectrum_group.attrs[HDF5_ENERGY_WIDTH_eV] = elv_text_parameters.energy_width_eV
            spectrum_group.attrs[HDF5_ENERGY_LOSS] = elv_text_parameters.energy_loss_eV
            spectrum_group.attrs[HDF5_ACQUISITION_SPEED] = elv_text_parameters.speed_us

        with open(file_path, 'r', encoding="ANSI", errors='ignore') as elv_text_file:
            elv_file = ElvFile()
            elv_file.read(elv_text_file)

            self.compare_attribute(spectrum_group, HDF5_DATE, elv_file.date)
            self.compare_attribute(spectrum_group, HDF5_TIME, elv_file.time)
            self.compare_attribute(spectrum_group, HDF5_COMMENT, elv_file.comment)
            self.compare_attribute(spectrum_group, HDF5_ACQUISITION_SPEED, elv_file.dose)
            self.compare_attribute(spectrum_group, HDF5_ENERGY_LOSS, elv_file.le)

            spectrum_group.attrs[HDF5_RAW] = elv_file.raw

            self.compare_attribute(spectrum_group, HDF5_ENERGY_WIDTH_eV, elv_file.energy_width)

            spectrum_group.attrs[HDF5_DUAL_DET_POSITION] = elv_file.dual_det_position
            spectrum_group.attrs[HDF5_DUAL_DET_POST] = elv_file.dual_det_post
            spectrum_group.attrs[HDF5_DUAL_DET_CENTER] = elv_file.dual_det_center
            spectrum_group.attrs[HDF5_Q1] = elv_file.q1
            spectrum_group.attrs[HDF5_Q1S] = elv_file.q1s
            spectrum_group.attrs[HDF5_Q2] = elv_file.q2
            spectrum_group.attrs[HDF5_Q2S] = elv_file.q2s
            spectrum_group.attrs[HDF5_Q3] = elv_file.q3
            spectrum_group.attrs[HDF5_H1] = elv_file.h1
            spectrum_group.attrs[HDF5_H1S] = elv_file.h1s
            spectrum_group.attrs[HDF5_H2] = elv_file.h2
            spectrum_group.attrs[HDF5_H2S] = elv_file.h2s
            spectrum_group.attrs[HDF5_H4] = elv_file.h4
            spectrum_group.attrs[HDF5_ELV_X] = elv_file.elv_x
            spectrum_group.attrs[HDF5_ELV_Y] = elv_file.elv_y
            spectrum_group.attrs[HDF5_SPECTRUM_ALIGNMENT_X] = elv_file.spectrum_alignment_x
            spectrum_group.attrs[HDF5_SPECTRUM_ALIGNMENT_Y] = elv_file.spectrum_alignment_y
            spectrum_group.attrs[HDF5_DET_SPEC_ALIGNMENT_X] = elv_file.det_spec_alignment_x
            spectrum_group.attrs[HDF5_DET_SPEC_ALIGNMENT_Y] = elv_file.det_spec_alignment_y
            spectrum_group.attrs[HDF5_DET_MAP_ALIGNMENT_X] = elv_file.det_map_alignment_x
            spectrum_group.attrs[HDF5_DET_MAP_ALIGNMENT_Y] = elv_file.det_map_alignment_y

            spectrum_group.attrs[HDF5_MAGNIFICATION] = elv_file.mag

            data = np.zeros((1023, 5))
            data[:, 0] = elv_file.energies_eV[:-1]
            data[:, 1] = elv_file.counts[:-1]
            data[:, 2] = elv_file.raw_counts[:-1]
            data[:, 3] = elv_file.gain_corrections[:-1]
            data[:, 4] = elv_file.dark_currents[:-1]

            spectrum_data_set = spectrum_group.create_dataset(HDF5_SPECTRUM, data=data)

            data = np.arange(1, 1023+1)
            spectrum_channel_data_set = spectrum_group.create_dataset(HDF5_SPECTRUM_CHANNELS, data=data)
            spectrum_data_set.dims.create_scale(spectrum_channel_data_set, HDF5_SPECTRUM_CHANNEL)
            spectrum_data_set.dims[0].attach_scale(spectrum_channel_data_set)

            data_types = [HDF5_SPECTRUM_ENERGIES_eV, HDF5_SPECTRUM_COUNTS, HDF5_SPECTRUM_RAW_COUNTS,
                          HDF5_SPECTRUM_GAIN_CORRECTIONS, HDF5_SPECTRUM_DARK_CURRENTS]
            max_size = max([len(data_type) for data_type in data_types])
            data = np.array(data_types, dtype="S{}".format(max_size+1))
            spectrum_types_data_set = spectrum_group.create_dataset(HDF5_SPECTRUM_DATA_TYPES, data=data)
            spectrum_data_set.dims.create_scale(spectrum_types_data_set, HDF5_SPECTRUM_DATA_TYPE)
            spectrum_data_set.dims[1].attach_scale(spectrum_types_data_set)

    def compare_attribute(self, spectrum_group, attribute_name, attribute_value):
        if attribute_name in spectrum_group.attrs:
            if attribute_value != spectrum_group.attrs[attribute_name]:
                logging.error("{} is not the same in .txt and .elv files".format(attribute_name))
        else:
            spectrum_group.attrs[attribute_name] = attribute_value
