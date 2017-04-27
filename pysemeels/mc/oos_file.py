#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.mc.oos_file
   :synopsis: Read and write oos file genereated by oos_maker code.

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read and write oos file genereated by oos_maker code.
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


class OosFile(object):
    def __init__(self):
        self.title = ""
        self.number_electrons = None
        self.molecular_weight = None
        self.density_g_cm3 = None
        self.switch_energy_eV = None

        self.energies_eV = []
        self.oos = []

    def read_file(self, file_path):
        with open(file_path, 'r') as oos_file:
            lines = oos_file.readlines()

            self.title = lines[0][1:].strip()
            self.number_electrons = int(lines[1].split()[0])
            self.molecular_weight = float(lines[2].split()[0])
            self.density_g_cm3 = float(lines[3].split()[0])
            self.switch_energy_eV = float(lines[4].split()[0])

            energies_eV = []
            oos = []

            for line in lines[5:]:
                items = line.split()
                energy_eV = float(items[0])
                df_dw =  float(items[1])

                energies_eV.append(energy_eV)
                oos.append(df_dw)

            self.energies_eV = energies_eV
            self.oos = oos
