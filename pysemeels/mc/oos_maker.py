#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.mc.oos_maker
   :synopsis: Make the oos input file for LEEPS Monte Carlo program.

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Make the oos input file for LEEPS Monte Carlo program.
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
from pysemeels.mc.oos_file import OosFile

# Globals and constants variables.

class OosMaker(object):
    def __init__(self):
        self.title = ""
        self.number_electrons = None
        self.molecular_weight = None
        self.density_g_cm3 = None
        self.switch_energy_eV = None
        self.transition_energy_eV = None

        self.energies_eV = None
        self.oos = None

    def get_oos_file(self):
        if self.energies_eV is None or self.oos is None:
            self.compute_oos()

        oos_file = OosFile()

        oos_file.title = self.title
        oos_file.number_electrons = self.number_electrons
        oos_file.molecular_weight = self.molecular_weight
        oos_file.density_g_cm3 = self.density_g_cm3
        oos_file.switch_energy_eV = self.switch_energy_eV

        return oos_file

    def compute_oos(self):
        dFn = 0

        
