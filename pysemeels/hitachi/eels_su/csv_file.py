#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.hitachi.eels_su.csv_file

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read csv file exported by EELS-SU.
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
import csv

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.

class CsvFile():
    def __init__(self):
        pass

    def read(self, file):
        reader = csv.reader(file)

        self.energies_eV = []
        self.counts = []

        row = next(reader)
        self.date = row[0]

        row = next(reader)
        self.time = row[0]

        row = next(reader)
        self.comment = row[0].split('=')[-1]

        row = next(reader)
        self.view_fast = row[0].split('=')[-1]
        skip_chars = len("view slow")
        self.view_slow = row[1][skip_chars:]

        row = next(reader)
        self.store_manual = row[0].split('=')[-1]
        skip_chars = len("store-auto")
        self.store_auto = row[1][skip_chars:]

        row = next(reader)
        self.le = row[1]

        row = next(reader)
        self.dual_det_center = row[1]

        row = next(reader)
        self.raw = float(row[1])

        row = next(reader)
        self.energy_width = row[1]
        self.dual_det_post = row[2]

        row = next(reader)
        self.dual_window1_position = row[1]
        self.dual_window2_position = row[2]

        row = next(reader)
        self.q1 = int(row[1])

        row = next(reader)
        self.q2 = int(row[1])

        row = next(reader)
        self.q3 = int(row[1])

        row = next(reader)
        self.spectrum_alignment_x = int(row[1])

        row = next(reader)
        self.spectrum_alignment_y = int(row[1])

        row = next(reader)
        self.mag = int(row[1])

        for row in reader:
            try:
                energy_eV = float(row[0])
                count = int(row[1])
                self.energies_eV.append(energy_eV)
                self.counts.append(count)
            except ValueError:
                pass

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from pysemeels import get_current_module_path
    import numpy as np

    elv_file_path = get_current_module_path(__file__, "../../../test_data/hitachi/eels_su/30kV_7eV.csv")
    with open(elv_file_path, 'r') as elv_text_file:
        csv_file = CsvFile()
        csv_file.read(elv_text_file)

        plt.figure()

        plt.plot(csv_file.energies_eV[:-1], csv_file.counts[:-1], '.')

        plt.show()
