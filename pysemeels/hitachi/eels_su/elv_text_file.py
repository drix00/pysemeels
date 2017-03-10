#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: elv_text_file
   :synopsis: Read elv text file.

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

# Globals and constants variables.

class ElvTextParameters():
    def __init__(self):
        pass

    def read(self, file):
        lines = file.readlines()

        for line in lines:
            try:
                keyword, value = line.split('=')

                value = value.strip()

                if keyword.startswith("EELS model"):
                    self.model = value
                elif keyword.startswith("S.H."):
                    self.sample_height = value
                elif keyword.startswith("File name"):
                    self.file_name = value
                elif keyword.startswith("Comments"):
                    self.comment = value
                elif keyword.startswith("Date"):
                    self.date = value
                elif keyword.startswith("Time"):
                    self.time = value
                elif keyword.startswith("Accelerating Voltage"):
                    value, unit = value.split()
                    self.accelerating_voltage_V = int(value)
                elif keyword.startswith("Energy Width"):
                    self.energy_width = value
                elif keyword.startswith("Energy Loss"):
                    self.energy_loss = value
                elif keyword.startswith("Spectrum speed"):
                    self.speed = value
            except ValueError:
                pass
