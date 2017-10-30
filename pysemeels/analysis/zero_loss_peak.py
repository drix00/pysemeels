#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.analysis.zero_loss_peak

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Analyze the zero loss peak from an EELS linescan.
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
import numpy as np
import scipy.stats
from lmfit.models import VoigtModel

# Local modules.

# Project modules.

# Globals and constants variables.


class ZeroLossPeak():
    def __init__(self, energies_eV, intensities):
        self.energies_eV = np.array(energies_eV)
        self.intensities = np.array(intensities)

        self.background = 0.0
        self.position_eV = 0.0
        self.fwhm_eV = 0.0
        self.fwtm_eV = 0.0
        self.fwfm_eV = 0.0
        self.maximum = 0.0

        self.fit_results = None
        self.fit_results_position_eV = 0.0
        self.fit_results_fwhm_eV = 0.0
        self.fit_results_sigma_eV = 0.0
        self.fit_results_gamma_eV = 0.0
        self.fit_results_area = 0.0
        self.fit_results_height = 0.0

        self.max_intensity_index = 0
        self.roi_indices = (0, 0)

    def find_position(self):
        self.max_intensity_index = np.argmax(self.intensities)
        self.position_eV = self.energies_eV[self.max_intensity_index]

        eV_channel = self.energies_eV[1] - self.energies_eV[0]
        self.roi_indices = (int(self.max_intensity_index - 4.0 / eV_channel), int(self.max_intensity_index + 4.0 / eV_channel))

    def compute_fwhm(self):
        self.find_position()

        if self.position_eV is not None:
            maximum = self.intensities[self.max_intensity_index]

            eV_channel = self.energies_eV[1] - self.energies_eV[0]

            background_min = int(self.roi_indices[0] - 2.0/eV_channel)
            if background_min < 0:
                background_min = 0

            background_max = int(self.roi_indices[0] + 2.0/eV_channel)
            if background_min < 0:
                background_min = 0

            self.background = np.mean(self.intensities[background_min:background_max])

            half_maximum = (maximum - self.background) / 2.0
            indices = np.where(self.intensities-self.background >= half_maximum)[0]

            self.fwhm_eV = self.energies_eV[indices[-1]] - self.energies_eV[indices[0]]

            tenth_maximum = (maximum - self.background) / 10.0
            indices = np.where(self.intensities-self.background >= tenth_maximum)[0]
            self.fwtm_eV = self.energies_eV[indices[-1]] - self.energies_eV[indices[0]]

            tenth_maximum = (maximum - self.background) / 20.0
            indices = np.where(self.intensities-self.background >= tenth_maximum)[0]
            self.fwfm_eV = self.energies_eV[indices[-1]] - self.energies_eV[indices[0]]

            self.maximum = maximum

    def compute_statistics(self):
        self.find_position()

        data = []
        for energy_eV, counts in zip(self.energies_eV[self.roi_indices[0]:self.roi_indices[1]], self.intensities[self.roi_indices[0]:self.roi_indices[1]]):
            data.extend([energy_eV for _i in range(int(counts))])

        data = np.array(data)
        describe = scipy.stats.describe(data)
        self.number_counts = describe.nobs
        self.minimum_eV = describe.minmax[0]
        self.maximum_eV = describe.minmax[1]
        self.mean_eV = describe.mean
        self.variance_eV2 = describe.variance
        self.std_eV = np.sqrt(describe.variance)
        self.skewness = describe.skewness
        self.kurtosis = describe.kurtosis

    def fit(self):
        x = self.energies_eV
        y = self.intensities

        model = VoigtModel()

        init_parameters = model.guess(y ,x=x)
        self.fit_results = model.fit(y, init_parameters, x=x)

        values = self.fit_results.params.valuesdict()

        self.fit_results_position_eV = values['center']
        self.fit_results_fwhm_eV = values['fwhm']
        self.fit_results_sigma_eV = values['sigma']
        self.fit_results_gamma_eV = values['gamma']
        self.fit_results_area = values['amplitude']
        self.fit_results_height = values['height']

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from pysemeels import get_current_module_path
    from pysemeels.hitachi.eels_su.elv_file import ElvFile
    import numpy as np

    elv_file_path = get_current_module_path(__file__, "../../test_data/hitachi/eels_su/30kV_7eV.elv")
    with open(elv_file_path, 'r') as elv_text_file:
        elv_file = ElvFile()
        elv_file.read(elv_text_file)

        plt.figure()

        plt.plot(elv_file.energies_eV, np.array(elv_file.raw_counts) - np.array(elv_file.dark_currents), '.')

        zlp = ZeroLossPeak(elv_file.energies_eV, np.array(elv_file.raw_counts) - np.array(elv_file.dark_currents))
        zlp.compute_statistics()
        zlp.compute_fwhm()
        energy_min_eV = zlp.energies_eV[zlp.roi_indices[0]]
        energy_max_eV = zlp.energies_eV[zlp.roi_indices[1]]

        plt.axvspan(energy_min_eV, energy_max_eV, color='g', alpha=0.3)

        plt.axvline(zlp.mean_eV, color='r')
        plt.axvline(zlp.position_eV, color='orange')

        plt.axhline(zlp.background, color='b')

        plt.xlim(-5, 5)

        plt.figure()

        plt.plot(elv_file.energies_eV, elv_file.gain_corrections)

    plt.show()
