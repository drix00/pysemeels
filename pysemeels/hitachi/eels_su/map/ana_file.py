#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: ana_file
   :synopsis: Read elv file.

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read elv file.
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
class Spectrum():
    def __init__(self):
        self.energies_eV = []
        self.counts = []

class AnaFile():
    def __init__(self):
        pass

    def read(self, file):
        lines = file.readlines()

        self.energies_eV = []
        self.counts = []

        self.raw_spectra = []
        self.raw_spectrum_id = -1

        for line in lines:
            if line.startswith("raw data"):
                self.raw_spectra.append(Spectrum())
                self.raw_spectrum_id += 1

            try:
                keyword, value = line.split('=')

                keyword = keyword.strip()
                value = value.strip()

                if keyword.startswith("date"):
                    self.date = value
                elif keyword.startswith("Time"):
                    self.time = value
                elif keyword.startswith("comment"):
                    self.comment = value
                elif keyword.startswith("Dose"):
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
                elif keyword == "Q3S":
                    self.q3s = int(value)
                elif keyword == "H1":
                    self.h1 = int(value)
                elif keyword == "H1S":
                    self.h1s = int(value)
                elif keyword == "H2":
                    self.h2 = int(value)
                elif keyword == "H2S":
                    self.h2s = int(value)
                elif keyword == "H3":
                    self.h3 = int(value)
                elif keyword == "H3S":
                    self.h3s = int(value)
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
                elif keyword.startswith("Det. align-x"):
                    self.det_map_alignment_x = int(value)
                elif keyword.startswith("Det. align-y"):
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
                            elif keyword.startswith("Image det. position"):
                                self.dual_det_position = value
                            elif keyword.startswith("post"):
                                self.dual_det_post = value
                        except ValueError:
                            if len(items) == 2:
                                try:
                                    if item == items[0] and self.raw_spectrum_id == -1:
                                        energy_eV = float(items[0])
                                        count = float(items[1])
                                        self.energies_eV.append(energy_eV)
                                        self.counts.append(count)
                                    elif item == items[0] and self.raw_spectrum_id > -1:
                                        energy_eV = float(items[0])
                                        count = float(items[1])
                                        self.raw_spectra[self.raw_spectrum_id].energies_eV.append(energy_eV)
                                        self.raw_spectra[self.raw_spectrum_id].counts.append(count)
                                except ValueError:
                                    pass
                except ValueError:
                    pass

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np

    from pysemeels import get_current_module_path

    ana_file_path = get_current_module_path(__file__, "../../../../test_data/hitachi/eels_su/30kV_march2017_7eV/spectra_1.ana")
    with open(ana_file_path, 'r') as ana_text_file:
        ana_file = AnaFile()
        ana_file.read(ana_text_file)

        plt.figure()
        plt.plot(ana_file.energies_eV, ana_file.counts, '.')
        energy_eV = ana_file.energies_eV[133]
        plt.axvline(energy_eV)
        energy_eV = ana_file.energies_eV[586]
        plt.axvline(energy_eV)
        energy_eV = ana_file.energies_eV[608]
        plt.axvline(energy_eV)

        plt.figure()
        for spectrum in ana_file.raw_spectra:
            plt.plot(spectrum.energies_eV, spectrum.counts, '.')

        plt.plot(ana_file.energies_eV, ana_file.counts, '-')

        spectra = np.zeros((len(ana_file.raw_spectra), len(ana_file.energies_eV)))
        print(spectra.shape)

        for spectrum_id, spectrum in enumerate(ana_file.raw_spectra):
            spectra[spectrum_id, :] = spectrum.counts

        plt.figure()
        plt.plot(ana_file.energies_eV, ana_file.counts, '-')
        plt.plot(ana_file.energies_eV, np.mean(spectra, axis=0), '.')

        plt.figure()
        plt.plot(ana_file.energies_eV, ana_file.counts - np.mean(spectra, axis=0), '.')

        plt.show()

