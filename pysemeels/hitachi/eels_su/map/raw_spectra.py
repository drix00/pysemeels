#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.hitachi.eels_su.map.spectra

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read raw spectra from a map.
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
import struct

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.
class Spectrum():
    def __init__(self):
        self.energies_eV = []
        self.counts = []

class RawSpectra():
    def __init__(self):
        pass

    def read(self, file):
        self.raw_spectra = []
        self.raw_spectrum_id = 0

        format = "1024H"

        size = struct.calcsize(format)

        while True:
            buffer = file.read(size)

            if len(buffer) == 0:
                break

            counts = struct.unpack(format, buffer)
            self.raw_spectra.append(counts)
            self.raw_spectrum_id += 1

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np

    from pysemeels import get_current_module_path

    file_path = get_current_module_path(__file__, "../../../../test_data/hitachi/eels_su/30kV_march2017_7eV/RawSpectra/rawspect-1.dat")
    with open(file_path, 'rb') as raw_spectra_file:
        raw_spectra = RawSpectra()
        raw_spectra.read(raw_spectra_file)

        xs = np.arange(1024)
        plt.figure()
        for spectrum in raw_spectra.raw_spectra:
            plt.plot(xs, spectrum, '-')

        plt.show()
