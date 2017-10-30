#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: elv_text_file

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read elv text file.
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
from pysemeels.hitachi.eels_su import UnitError

# Globals and constants variables.
HDF5_ATTRIBUTE_MODEL = "model"
HDF5_ATTRIBUTE_SAMPLE_HEIGHT_mm = "sample height (mm)"
HDF5_ATTRIBUTE_FILEPATH = "filepath"
HDF5_ATTRIBUTE_COMMENT = "comment"
HDF5_ATTRIBUTE_DATE = "date"
HDF5_ATTRIBUTE_TIME = "time"
HDF5_ATTRIBUTE_ACCELERATING_VOLTAGE_V = "accelerating voltage (V)"
HDF5_ATTRIBUTE_ENERGY_WIDTH_eV = "energy width (eV)"
HDF5_ATTRIBUTE_ENERGY_LOSS_eV = "energy loss (eV)"
HDF5_ATTRIBUTE_SPEED_us = "speed (us)"


class ElvTextParameters():
    def __init__(self):
        self.parameters = {}

    def read(self, file):
        lines = file.readlines()

        for line in lines:
            try:
                keyword, value = line.split('=')

                value = value.strip()

                if keyword.startswith("EELS model"):
                    self.parameters[HDF5_ATTRIBUTE_MODEL] = value
                elif keyword.startswith("S.H."):
                    value, unit = float(value[:-2]), value[-2:]
                    if unit != "mm":
                        raise UnitError("Sample height unit is not mm: {}".format(unit))
                    self.parameters[HDF5_ATTRIBUTE_SAMPLE_HEIGHT_mm] = value
                elif keyword.startswith("File name"):
                    self.parameters[HDF5_ATTRIBUTE_FILEPATH] = value
                elif keyword.startswith("Comments"):
                    self.parameters[HDF5_ATTRIBUTE_COMMENT] = value
                elif keyword.startswith("Date"):
                    self.parameters[HDF5_ATTRIBUTE_DATE] = value
                elif keyword.startswith("Time"):
                    self.parameters[HDF5_ATTRIBUTE_TIME] = value
                elif keyword.startswith("Accelerating Voltage"):
                    value, unit = value.split()
                    if unit != "Volt":
                        raise UnitError("Accelerating voltage unit is not V: {}".format(unit))
                    self.parameters[HDF5_ATTRIBUTE_ACCELERATING_VOLTAGE_V] = int(value)
                elif keyword.startswith("Energy Width"):
                    value, unit = float(value[:-2]), value[-2:]
                    if unit != "eV":
                        raise UnitError("Energy width unit is not eV: {}".format(unit))
                    self.parameters[HDF5_ATTRIBUTE_ENERGY_WIDTH_eV] = value
                elif keyword.startswith("Energy Loss"):
                    value, unit = float(value[:-2]), value[-2:]
                    if unit != "eV":
                        raise UnitError("Energy loss unit is not eV: {}".format(unit))
                    self.parameters[HDF5_ATTRIBUTE_ENERGY_LOSS_eV] = value
                elif keyword.startswith("Spectrum speed"):
                    value, unit = float(value[:-2]), value[-2:]
                    if unit != "µs":
                        raise UnitError("Speed unit is not µs: {}".format(unit))
                    self.parameters[HDF5_ATTRIBUTE_SPEED_us] = value
            except ValueError:
                pass

    def items(self):
        return self.parameters

    @property
    def model(self):
        return self.parameters[HDF5_ATTRIBUTE_MODEL]

    @property
    def sample_height_mm(self):
        return self.parameters[HDF5_ATTRIBUTE_SAMPLE_HEIGHT_mm]

    @property
    def file_name(self):
        return self.parameters[HDF5_ATTRIBUTE_FILEPATH]

    @property
    def comment(self):
        return self.parameters[HDF5_ATTRIBUTE_COMMENT]

    @property
    def date(self):
        return self.parameters[HDF5_ATTRIBUTE_DATE]

    @property
    def time(self):
        return self.parameters[HDF5_ATTRIBUTE_TIME]

    @property
    def accelerating_voltage_V(self):
        return self.parameters[HDF5_ATTRIBUTE_ACCELERATING_VOLTAGE_V]

    @property
    def energy_width_eV(self):
        return self.parameters[HDF5_ATTRIBUTE_ENERGY_WIDTH_eV]

    @property
    def energy_loss_eV(self):
        return self.parameters[HDF5_ATTRIBUTE_ENERGY_LOSS_eV]

    @property
    def speed_us(self):
        return self.parameters[HDF5_ATTRIBUTE_SPEED_us]
