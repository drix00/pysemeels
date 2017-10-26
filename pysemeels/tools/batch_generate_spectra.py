#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.tools.batch_generate_spectra

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Generate spectra figure from spectrum imaging data in batch.
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
import os
import logging

# Third party modules.
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

# Local modules.

# Project modules.
from pysemeels.hitachi.eels_su.map.ana_file import AnaFile

# Globals and constants variables.


class BatchGenerateSpectra(object):
    def __init__(self, path):
        self.path = path

        self.overwrite = True
        self.recursive = True

    def generate(self):
        if self.recursive:
            for current_path, folder_names, filenames in os.walk(self.path):
                ela_file_name = ""
                ana_filenames = []
                for file_name in filenames:
                    if file_name.endswith(".ela"):
                        logging.info(file_name)
                        ela_file_name = file_name
                    if file_name.endswith(".ana"):
                        logging.info(file_name)
                        ana_filenames.append(file_name)

                if ela_file_name:
                    for ana_file_name in ana_filenames:
                        pdf_file_path = self.generate_pdf_file_path(current_path, ela_file_name, ana_file_name)
                        ana_file_path = os.path.join(current_path, ana_file_name)
                        self.generate_figures_pdf(ana_file_path, pdf_file_path)
        else:
            for file_name in os.listdir(self.path):
                logging.info(file_name)

    def generate_pdf_file_path(self, path, ela_file_name, ana_file_name):
        file_path = os.path.join(path, ela_file_name[:-4] + "_" + ana_file_name[:-4] + ".pdf")
        logging.info(file_path)
        return file_path

    def generate_figures_pdf(self, ana_file_path, pdf_file_path):
        with open(ana_file_path, 'r') as ana_text_file:
            ana_file = AnaFile()
            ana_file.read(ana_text_file)

            pp = PdfPages(pdf_file_path)

            for spectrum_id in sorted(ana_file.total_spectra):
                plt.figure()

                plt.title(spectrum_id+1)

                plt.plot(ana_file.energies_eV[:-1], ana_file.total_spectra[spectrum_id][:-1])

                plt.xlabel("Energy loss (eV)")
                plt.ylabel("Counts")
                plt.tight_layout()

                plt.savefig(pp, format='pdf')
                plt.close()

            pp.close()


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        path = sys.argv[1]
        print(path)
        batch_generate_windows_figure = BatchGenerateSpectra(path)

        batch_generate_windows_figure.generate()
    else:
        print("Usage: python batch_generate_spectra.py path")
