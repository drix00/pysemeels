#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: ana_file
   :synopsis: Read elv file.

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read elv file.
"""
from future.backports.misc import count

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

class AnaFile():
    def __init__(self):
        pass

    def read(self, file):
        lines = file.readlines()

        self.energies_eV = []
        self.counts = []
        self.gain_corrections = []
        self.dark_currents = []

        for line in lines:
            try:
                items = line.split(',')
                if len(items) == 2:
                    try:
                        energy_eV = float(items[0])
                        count = float(items[1])
                        self.energies_eV.append(energy_eV)
                        self.counts.append(count)
                    except ValueError:
                        pass
                if len(items) == 1:
                    if len(self.gain_corrections) < 1024:
                        try:
                            gain_correction = float(items[0])
                            self.gain_corrections.append(gain_correction)
                        except ValueError:
                            pass
                    else:
                        try:
                            dark_current = float(items[0])
                            self.dark_currents.append(dark_current)
                        except ValueError:
                            pass

            except ValueError:
                pass

        if len(self.dark_currents) > 1024:
            self.dark_currents = self.dark_currents[:-1]

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from pysemeels import get_current_module_path

    elv_file_path = get_current_module_path(__file__, "../../../test_data/hitachi/eels_su/30kV_7eV.ana")
    with open(elv_file_path, 'r') as elv_text_file:
        ana_file = AnaFile()
        ana_file.read(elv_text_file)

        plt.figure()

        plt.plot(ana_file.energies_eV, ana_file.counts, '.')

        plt.show()

