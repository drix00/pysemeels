#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: ana_file

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
import csv

# Third party modules.
import numpy as np

# Local modules.
import pySpectrumFileFormat.emmff.emsa as emsa

# Project modules.
from pysemeels.tools.hdf5_file_labels import *
from pysemeels.hitachi.eels_su import UnitError

# Globals and constants variables.


class SpectrumData():
    def __init__(self):
        self.energies_eV = []
        self.raw_counts = []
        self.gain_corrections = []
        self.dark_currents = []

    @property
    def counts(self):
        corrected_counts = (np.array(self.raw_counts) - np.array(self.dark_currents)) / np.array(self.gain_corrections)
        return corrected_counts


class ElvFile():
    energy_windows_eV = [7, 15, 30, 60]
    segments_channel = {"PreL": (300, 300+133),
                        "PreH": (443, 433+133),
                        "Post": (586, 586+133)}
    loss_energy_channel = 608

    def __init__(self):
        self.energies_eV = []
        self.raw_counts = []
        self.gain_corrections = []
        self.dark_currents = []

    def read(self, file):
        lines = file.readlines()

        self.energies_eV = []
        self.raw_counts = []
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
                    value, unit = float(value[:-2]), value[-2:]
                    if unit == "ms":
                        value = value * 1.0e3
                    if unit != "µs" and unit != "ms":
                        raise UnitError("Dose is not µs: {}".format(unit))
                    self.dose = value
                elif keyword.startswith("Energy Window Width"):
                    value, unit = float(value[:-2]), value[-2:]
                    if unit != "eV":
                        raise UnitError("Energy width unit is not eV: {}".format(unit))
                    self.energy_width = value
                elif keyword.startswith("center"):
                    value, unit = float(value[:-2]), value[-2:]
                    if unit != "ch":
                        raise UnitError("Dual det. center unit is not ch: {}".format(unit))
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
                                value, unit = float(value[:-2]), value[-2:]
                                if unit != "eV":
                                    raise UnitError("Energy loss unit is not eV: {}".format(unit))
                                self.le = value
                            elif keyword.startswith("Raw"):
                                self.raw = float(value)
                            elif keyword.startswith("Dual det. position"):
                                value, unit = float(value[:-2]), value[-2:]
                                if unit != "ch":
                                    raise UnitError("Dual det. position unit is not ch: {}".format(unit))
                                self.dual_det_position = value
                            elif keyword.startswith("post"):
                                value, unit = float(value[:-2]), value[-2:]
                                if unit != "ch":
                                    raise UnitError("Dual det. post unit is not ch: {}".format(unit))
                                self.dual_det_post = value
                        except ValueError:
                            if len(items) == 2:
                                try:
                                    if item == items[0]:
                                        energy_eV = float(items[0])
                                        count = int(items[1])
                                        self.energies_eV.append(energy_eV)
                                        self.raw_counts.append(count)
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

    def get_spectrum_data(self):
        spectrum_data = SpectrumData()
        spectrum_data.energies_eV = self.energies_eV
        spectrum_data.raw_counts = self.raw_counts
        spectrum_data.gain_corrections = self.gain_corrections
        spectrum_data.dark_currents = self.dark_currents

        return spectrum_data

    def export_csv_row(self, file_path):
        with open(file_path, 'w', newline="\n") as csv_file:
            writer = csv.writer(csv_file)

            row = [count for count in self.raw_counts]
            writer.writerow(row)

    def export_msa(self, file_path):
        spectrum = emsa.Emsa()
        spectrum.xdata = self.energies_eV
        spectrum.ydata = self.counts

        spectrum.header.title = ''
        spectrum.header.date = self.date
        spectrum.header.time = self.time
        spectrum.header.owner = ''
        spectrum.header.npoints = len(self.energies_eV)
        spectrum.header.ncolumns = 1
        spectrum.header.xunits = 'eV'
        spectrum.header.yunits = 'Counts'
        spectrum.header.datatype = emsa.DATA_TYPE_Y
        spectrum.header.xperchan = "{}".format((self.energies_eV[-1] - self.energies_eV[0]) / float(len(self.energies_eV)))
        spectrum.header.offset = self.energies_eV[0]
        spectrum.header.signal = emsa.SIGNAL_TYPE_ELS

        spectrum.validate()

        with open(file_path, 'w', newline="\n") as msa_file:
            emsa.write(spectrum, msa_file)

    def parameters(self):
        _parameters = {}
        _parameters[HDF5_DATE] = self.date
        _parameters[HDF5_TIME] = self.time
        _parameters[HDF5_COMMENT] = self.comment
        _parameters[HDF5_ACQUISITION_SPEED] = self.dose
        _parameters[HDF5_ENERGY_LOSS] = self.le
        _parameters[HDF5_RAW] = self.raw
        _parameters[HDF5_ENERGY_WIDTH_eV] = self.energy_width
        _parameters[HDF5_DUAL_DET_POSITION] = self.dual_det_position
        _parameters[HDF5_DUAL_DET_POST] = self.dual_det_post
        _parameters[HDF5_DUAL_DET_CENTER] = self.dual_det_center
        _parameters[HDF5_Q1] = self.q1
        _parameters[HDF5_Q1S] = self.q1s
        _parameters[HDF5_Q2] = self.q2
        _parameters[HDF5_Q2S] = self.q2s
        _parameters[HDF5_Q3] = self.q3
        _parameters[HDF5_H1] = self.h1
        _parameters[HDF5_H1S] = self.h1s
        _parameters[HDF5_H2] = self.h2
        _parameters[HDF5_H2S] = self.h2s
        _parameters[HDF5_H4] = self.h4
        _parameters[HDF5_ELV_X] = self.elv_x
        _parameters[HDF5_ELV_Y] = self.elv_y
        _parameters[HDF5_SPECTRUM_ALIGNMENT_X] = self.spectrum_alignment_x
        _parameters[HDF5_SPECTRUM_ALIGNMENT_Y] = self.spectrum_alignment_y
        _parameters[HDF5_DET_SPEC_ALIGNMENT_X] = self.det_spec_alignment_x
        _parameters[HDF5_DET_SPEC_ALIGNMENT_Y] = self.det_spec_alignment_y
        _parameters[HDF5_DET_MAP_ALIGNMENT_X] = self.det_map_alignment_x
        _parameters[HDF5_DET_MAP_ALIGNMENT_Y] = self.det_map_alignment_y
        _parameters[HDF5_MAGNIFICATION] = self.mag

        return _parameters

    @property
    def counts(self):
        corrected_counts = (np.array(self.raw_counts) - np.array(self.dark_currents)) / np.array(
            self.gain_corrections)
        return corrected_counts


def plot_spectrum():
    import matplotlib.pyplot as plt
    from pysemeels import get_current_module_path
    from pysemeels.hitachi.eels_su.ana_file import AnaFile
    import numpy as np

    ana_file = AnaFile()
    ana_file_path = get_current_module_path(__file__, r"D:\Dropbox\hdemers\professional\results\experiments\2017\su9000\eels\2017\System_baseline_march2017/30kV_7eV.ana")
    with open(ana_file_path, 'r') as elv_text_file:
        ana_file.read(elv_text_file)

    elv_file_path = get_current_module_path(__file__, r"D:\Dropbox\hdemers\professional\results\experiments\2017\su9000\eels\2017\System_baseline_march2017/30kV_7eV.elv")
    with open(elv_file_path, 'r') as elv_text_file:
        elv_file = ElvFile()
        elv_file.read(elv_text_file)

        plt.figure()

        plt.plot(elv_file.energies_eV, elv_file.raw_counts, '.')
        plt.plot(ana_file.energies_eV, ana_file.counts, '-')

        corrected_counts = (np.array(elv_file.raw_counts) - np.array(elv_file.dark_currents)) / np.array(elv_file.gain_corrections)
        #plt.plot(ana_file.energies_eV, corrected_counts, '.')
        plt.plot(ana_file.energies_eV, elv_file.counts, '.')
        #plt.close()

        print(elv_file.raw_counts[0])
        print(elv_file.gain_corrections[0])
        print(elv_file.dark_currents[0])
        print(ana_file.counts[0])
        print(corrected_counts[0] - ana_file.counts[0])
        print(int(elv_file.raw_counts[0]) - int(elv_file.dark_currents[0]) - int(ana_file.counts[0]))
        print(elv_file.raw_counts[0] * elv_file.gain_corrections[0] - elv_file.dark_currents[0])
        print(elv_file.raw_counts[0] / elv_file.gain_corrections[0] - elv_file.dark_currents[0])
        print((elv_file.raw_counts[0] - elv_file.dark_currents[0]) * elv_file.gain_corrections[0])
        print((elv_file.raw_counts[0] - elv_file.dark_currents[0]) / elv_file.gain_corrections[0])
        print(elv_file.raw_counts[0] - elv_file.dark_currents[0] * elv_file.gain_corrections[0])
        print(ana_file.counts[0] - (elv_file.raw_counts[0] - elv_file.dark_currents[0]) / elv_file.gain_corrections[0])

        plt.figure()
        plt.plot(ana_file.energies_eV, np.array(ana_file.counts) - (np.array(elv_file.raw_counts) - np.array(elv_file.dark_currents)) / np.array(elv_file.gain_corrections))
        plt.figure()
        plt.plot(elv_file.energies_eV, elv_file.dark_currents, '-')
        plt.figure()
        plt.plot(elv_file.energies_eV, elv_file.gain_corrections, '-')
        plt.close()

        print(elv_file.energies_eV.index(0.0))
        plt.figure()
        plt.plot(elv_file.energies_eV, elv_file.raw_counts, '-')
        for energy_eV in [-30.0, -20.0, -10.0, 0.0, 10, 20.0]:
            plt.axvline(energy_eV, ls='--', color='b')

        for min_index in [586, 443, 300]:
            min_energy_eV = elv_file.energies_eV[min_index]
            max_energy_eV = elv_file.energies_eV[min_index+133]
            plt.axvspan(min_energy_eV, max_energy_eV, color='r', alpha=0.5)

        plt.xlim((elv_file.energies_eV[0], elv_file.energies_eV[-1]))
        #plt.subplots_adjust(left=0.0, bottom=0.0, right=1.0, top=1.0)
        plt.xlabel("Energy (eV)")
        plt.show()


def print_window_info():
    for energy_window_eV in ElvFile.energy_windows_eV:
        elv_file_path = r"D:\Dropbox\hdemers\professional\results\experiments\2017\su9000\eels\2017\System_baseline_march2017/30kV_{:d}eV.elv".format(energy_window_eV)

        with open(elv_file_path, 'r') as elv_text_file:
            elv_file = ElvFile()
            elv_file.read(elv_text_file)

            print("---------------------------------------------------------------------------------------------------")
            print("Energy window: {:7d} eV".format(energy_window_eV))
            print("Range          {:7.2f} eV".format(elv_file.energies_eV[-1] - elv_file.energies_eV[0]))
            print("eV per channel {:7.2f} eV".format(elv_file.energies_eV[1] - elv_file.energies_eV[0]))

            print("Loss energy    {:7.2f} eV".format(elv_file.energies_eV[elv_file.loss_energy_channel]))
            for segment_name in elv_file.segments_channel:
                min_index, max_index = elv_file.segments_channel[segment_name]
                min_energy_eV = elv_file.energies_eV[min_index]
                max_energy_eV = elv_file.energies_eV[max_index]
                middle_energy_eV = (max_energy_eV - min_energy_eV) / 2.0 + min_energy_eV
                print("Segment {:s}: {:7.2f} to {:7.2f} eV middle {:7.2f} eV".format(segment_name, min_energy_eV, max_energy_eV, middle_energy_eV))


def export_msa():
    from pysemeels import get_current_module_path
    elv_file_path = get_current_module_path(__file__, r"D:\Dropbox\hdemers\professional\results\experiments\2017\su9000\eels\2017\System_baseline_march2017/30kV_7eV.elv")

    with open(elv_file_path, 'r') as elv_text_file:
        elv_file = ElvFile()
        elv_file.read(elv_text_file)

        msa_file_path = get_current_module_path(__file__, r"D:\Dropbox\hdemers\professional\results\experiments\2017\su9000\eels\2017\System_baseline_march2017/30kV_7eV.msa")
        elv_file.export_msa(msa_file_path)

        for channel_id in range(len(elv_file.energies_eV)-1):
            print(elv_file.energies_eV[channel_id+1] - elv_file.energies_eV[channel_id])


if __name__ == '__main__':
    # plot_spectrum()
    print_window_info()
    # export_msa()
