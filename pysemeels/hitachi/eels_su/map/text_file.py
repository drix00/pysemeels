#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: text_file

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read text file in map folder.
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

class Analysis():
    def __init__(self, dose=0.0, energy_width_eV=0, energy_loss_eV=0.0):
        self.dose = dose
        self.energy_width_eV = energy_width_eV
        self.energy_loss_eV = energy_loss_eV

class TextParameters():

    def __init__(self):
        self.analysis1 = Analysis(0.0, 0, 0.0)
        self.analysis2 = Analysis(0.0, 0, 0.0)
        self.analysis3 = Analysis(0.0, 0, 0.0)

    def read(self, file):
        lines = file.readlines()

        map_mode = True
        for line in lines:
            if line.startswith("[Analysis]"):
                map_mode = False

            try:
                keyword, value = line.split('=')

                keyword = keyword.strip()
                value = value.strip()

                if map_mode:
                    if keyword.startswith("SU9000 Magnification"):
                        self.magnification = int(value)
                    elif keyword.startswith("EELS model"):
                        self.model = value
                    elif keyword.startswith("S.H."):
                        self.sample_height = value
                    elif keyword.startswith("File Name"):
                        self.file_name = value
                    elif keyword.startswith("Date"):
                        self.date = value
                    elif keyword.startswith("Time"):
                        self.time = value
                    elif keyword.startswith("Capture resolution"):
                        self.capture_resolution = value
                    elif keyword.startswith("Accelerating Voltage"):
                        value, unit = value.split()
                        self.accelerating_voltage_V = int(value)
                    elif keyword.startswith("Energy Width"):
                        self.energy_width = value
                    elif keyword.startswith("Energy Loss"):
                        self.energy_loss = value
                    elif keyword.startswith("Scan Speed"):
                        self.speed = value
                    elif keyword.startswith("DPI"):
                        self.dpi = int(value)
                    elif keyword.startswith("Pixel Distance"):
                        self.pixel_distance = value

                else:
                    if keyword.startswith("Dose"):
                        unit = value[-2:]
                        items = value[:-2].split('/')

                        if not items[0].startswith('-'):
                            self.analysis1.dose = float(items[0])
                        if not items[1].startswith('-'):
                            self.analysis2.dose = float(items[1])
                        if not items[2].startswith('-'):
                            self.analysis3.dose = float(items[2])
                    elif keyword.startswith("Energy Width"):
                        unit = value[-2:]
                        items = value[:-2].split('/')

                        if not items[0].startswith('-'):
                            self.analysis1.energy_width_eV = int(items[0])
                        if not items[1].startswith('-'):
                            self.analysis2.energy_width_eV = int(items[1])
                        if not items[2].startswith('-'):
                            self.analysis3.energy_width_eV = int(items[2])
                    elif keyword.startswith("Energy Loss"):
                        unit = value[-2:]
                        items = value[:-2].split('/')

                        if not items[0].startswith('-'):
                            self.analysis1.energy_loss_eV = float(items[0])
                        if not items[1].startswith('-'):
                            self.analysis2.energy_loss_eV = float(items[1])
                        if not items[2].startswith('-'):
                            self.analysis3.energy_loss_eV = float(items[2])
                    elif keyword.startswith("A(x,y)"):
                        self.A = value
                    elif keyword.startswith("B(x,y)"):
                        self.B = value
                    elif keyword.startswith("Distance"):
                        self.distance = value
                    elif keyword.startswith("Pitch"):
                        self.pitch = value
                    elif keyword.startswith("Number"):
                        self.number = int(value)
                    elif keyword.startswith("Adjust"):
                        self.adjust = value
                    elif keyword.startswith("Data Size"):
                        self.data_size = value
                    elif keyword.startswith("Integration"):
                        self.integration = int(value)

            except ValueError:
                pass
