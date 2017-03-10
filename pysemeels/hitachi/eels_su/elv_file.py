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

class ElvFile():
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
                keyword, value = line.split('=')

                value = value.strip()

                if keyword.startswith("date"):
                    self.date = value
                elif keyword.startswith("Time"):
                    self.time = value
                elif keyword.startswith("comment"):
                    self.comment = value
                elif keyword.startswith("dose"):
                    self.dose = value
                elif keyword.startswith("Energy Window Width"):
                    self.energy_width = value
                elif keyword.startswith("center"):
                    self.dual_det_center = value
                elif keyword == "Q1":
                    self.q1 = int(value)
                elif keyword == "Q1S":
                    self.q1s = int(value)
                elif keyword == "Q2":
                    self.q2 = int(value)
                elif keyword == "Q2S":
                    self.q2s = int(value)
                elif keyword == "Q3":
                    self.q3 = int(value)
                elif keyword == "H1":
                    self.h1 = int(value)
                elif keyword == "H1S":
                    self.h1s = int(value)
                elif keyword == "H2":
                    self.h2 = int(value)
                elif keyword == "H2S":
                    self.h2s = int(value)
                elif keyword == "H4":
                    self.h4 = int(value)
                elif keyword.startswith("ELV-x"):
                    self.elv_x = int(value)
                elif keyword.startswith("ELV-y"):
                    self.elv_y = int(value)
                elif keyword.startswith("Spectrum align-x"):
                    self.spectrum_alignment_x = int(value)
                elif keyword.startswith("Spectrum align-y"):
                    self.spectrum_alignment_y = int(value)
                elif keyword.startswith("DET alignment-x(spec.)"):
                    self.det_spec_alignment_x = int(value)
                elif keyword.startswith("DET alignment-y(spec.)"):
                    self.det_spec_alignment_y = int(value)
                elif keyword.startswith("DET alignment-x(map)"):
                    self.det_map_alignment_x = int(value)
                elif keyword.startswith("DET alignment-y(map)"):
                    self.det_map_alignment_y = int(value)
                elif keyword.startswith("Mag"):
                    self.mag = int(value)
            except ValueError:
                try:
                    items = line.split(',')
                    for item in items:
                        try:
                            item = item.strip()
                            keyword, value = item.split('=')
                            value = value.strip()
                            if keyword.startswith("LE"):
                                self.le = value
                            elif keyword.startswith("Raw"):
                                self.raw = float(value)
                            elif keyword.startswith("Dual det. position"):
                                self.dual_det_position = value
                            elif keyword.startswith("post"):
                                self.dual_det_post = value
                        except ValueError:
                            if len(items) == 2:
                                try:
                                    if item == items[0]:
                                        energy_eV = float(items[0])
                                        count = int(items[1])
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

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from pysemeels import get_current_module_path
    from pysemeels.hitachi.eels_su.ana_file import AnaFile
    import numpy as np

    ana_file = AnaFile()
    ana_file_path = get_current_module_path(__file__, "../../../test_data/hitachi/eels_su/30kV_7eV.ana")
    with open(ana_file_path, 'r') as elv_text_file:
        ana_file.read(elv_text_file)

    elv_file_path = get_current_module_path(__file__, "../../../test_data/hitachi/eels_su/30kV_7eV.elv")
    with open(elv_file_path, 'r') as elv_text_file:
        elv_file = ElvFile()
        elv_file.read(elv_text_file)

        plt.figure()

        plt.plot(elv_file.energies_eV, elv_file.counts, '.')
        plt.plot(ana_file.energies_eV, ana_file.counts, '-')

        corrected_counts = np.array(elv_file.counts) - np.array(elv_file.dark_currents)
        plt.plot(ana_file.energies_eV, ana_file.counts, '.')

        print(elv_file.counts[0])
        print(elv_file.gain_corrections[0])
        print(elv_file.dark_currents[0])
        print(ana_file.counts[0])
        print(corrected_counts[0] - ana_file.counts[0])
        print(elv_file.counts[0]*elv_file.gain_corrections[0] - elv_file.dark_currents[0])
        print(elv_file.counts[0]/elv_file.gain_corrections[0] - elv_file.dark_currents[0])
        print((elv_file.counts[0] - elv_file.dark_currents[0])*elv_file.gain_corrections[0])
        print((elv_file.counts[0] - elv_file.dark_currents[0])/elv_file.gain_corrections[0])
        print(elv_file.counts[0] - elv_file.dark_currents[0]*elv_file.gain_corrections[0])
        print(elv_file.counts[0] - elv_file.dark_currents[0]/elv_file.gain_corrections[0])

        plt.show()

