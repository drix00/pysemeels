#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.tools.hdf5_file_labels

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Labels used in the HDF5 file.
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

HDF5_MODEL = "model"
HDF5_SAMPLE_HEIGHT = "sample height"
HDF5_FILE_PATH = "file path"
HDF5_COMMENT = "comment"
HDF5_DATE = "date"
HDF5_TIME = "time"
HDF5_ACCELERATING_VOLTAGE_V = "accelerating voltage (V)"
HDF5_ENERGY_WIDTH_eV = "energy width (eV)"
HDF5_ENERGY_LOSS = "energy loss (eV)"
HDF5_ACQUISITION_SPEED = "acquisition speed"
# todo Find meaning of these parameters.
HDF5_RAW = "raw"
HDF5_DUAL_DET_POSITION = "dual_det_position"
HDF5_DUAL_DET_POST = "dual_det_post"
HDF5_DUAL_DET_CENTER = "dual_det_center"
HDF5_Q1 = "q1"
HDF5_Q1S = "q1s"
HDF5_Q2 = "q2"
HDF5_Q2S = "q2s"
HDF5_Q3 = "q3"
HDF5_H1 = "h1"
HDF5_H1S = "h1s"
HDF5_H2 = "h2"
HDF5_H2S = "h2s"
HDF5_H4 = "h4"
HDF5_ELV_X = "elv_x"
HDF5_ELV_Y = "elv_y"
HDF5_SPECTRUM_ALIGNMENT_X = "spectrum_alignment_x"
HDF5_SPECTRUM_ALIGNMENT_Y = "spectrum_alignment_y"
HDF5_DET_SPEC_ALIGNMENT_X = "det_spec_alignment_x"
HDF5_DET_SPEC_ALIGNMENT_Y = "det_spec_alignment_y"
HDF5_DET_MAP_ALIGNMENT_X = "det_map_alignment_x"
HDF5_DET_MAP_ALIGNMENT_Y = "det_map_alignment_y"

HDF5_MAGNIFICATION = "magnification"

HDF5_SPECTRUM = "linescan"
HDF5_SPECTRUM_ENERGIES_eV = "energies (eV)"
HDF5_SPECTRUM_COUNTS = "counts"
HDF5_SPECTRUM_RAW_COUNTS = "raw counts"
HDF5_SPECTRUM_GAIN_CORRECTIONS = "gain corrections"
HDF5_SPECTRUM_DARK_CURRENTS = "dark currents"

HDF5_SPECTRUM_CHANNEL = "channel"
HDF5_SPECTRUM_DATA_TYPE = "linescan data type"
HDF5_SPECTRUM_CHANNELS = "channels"
HDF5_SPECTRUM_DATA_TYPES = "linescan data types"
