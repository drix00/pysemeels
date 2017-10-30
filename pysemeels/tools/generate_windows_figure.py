#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.tools.generate_windows_figure

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Generate spectra figure with position of the 3 windows from spectrum data in EFSTEM folder.
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

# Third party modules.
import matplotlib.pyplot as plt

# Local modules.

# Project modules.
from pysemeels.hitachi.eels_su.elv_file import ElvFile

# Globals and constants variables.


class GenerateWindowsFigure(object):
    def __init__(self, elv_file_path, overwrite=True):
        self.elv_file_path = elv_file_path

        self.overwrite = overwrite

    def generate(self):
        with open(self.elv_file_path, 'r') as elv_text_file:
            elv_file = ElvFile()
            elv_file.read(elv_text_file)

            plt.figure()

            plt.plot(elv_file.energies_eV[:-1], elv_file.counts[:-1])

            energy_eV = elv_file.energies_eV[elv_file.loss_energy_channel]
            plt.axvline(energy_eV, ls='-', color='b', alpha=0.5, label="EL")

            colors = {"PreL": "g", "PreH": "b", "Post": "r"}

            for segment_name in elv_file.segments_channel:
                min_index, max_index = elv_file.segments_channel[segment_name]
                min_energy_eV = elv_file.energies_eV[min_index]
                max_energy_eV = elv_file.energies_eV[max_index]
                plt.axvspan(min_energy_eV, max_energy_eV, color=colors[segment_name], alpha=0.2, label=segment_name)

            plt.xlabel("Energy loss (eV)")
            plt.ylabel("Count")
            plt.legend()
            plt.tight_layout()

            path = os.path.dirname(self.elv_file_path)
            figure_file_path = os.path.join(path, "windows.png")
            plt.savefig(figure_file_path)
            plt.close()
