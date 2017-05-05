#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.tools.batch_generate_windows_figure
   :synopsis: Batch generate spectra figure with position of the 3 windows from spectrum data in EFSTEM folder.

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Batch generate spectra figure with position of the 3 windows from spectrum data in EFSTEM folder.
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

# Local modules.

# Project modules.
from pysemeels.tools.generate_windows_figure import GenerateWindowsFigure

# Globals and constants variables.


class BatchGenerateWindowsFigure(object):
    def __init__(self, path, overwrite=True, recursive=True):
        self.path = path

        self.overwrite = overwrite
        self.recursive = recursive

    def generate(self):
        if self.recursive:
            for current_path, folder_names, filenames in os.walk(self.path):
                ela_file_name = ""
                elv_file_names = []
                for file_name in filenames:
                    if file_name.endswith(".ela"):
                        logging.info(file_name)
                        ela_file_name = file_name
                    if file_name.endswith(".elv"):
                        logging.info(file_name)
                        elv_file_names.append(file_name)

                if ela_file_name:
                    for elv_filename in elv_file_names:
                        elv_file_path = os.path.join(current_path, elv_filename)
                        generate_windows_figure = GenerateWindowsFigure(elv_file_path, self.overwrite)
                        generate_windows_figure.generate()
        else:
            for file_name in os.listdir(self.path):
                logging.info(file_name)
