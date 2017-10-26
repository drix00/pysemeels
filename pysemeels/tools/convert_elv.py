#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.tools.convert_elv

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Convert an elv file into msa and/or hdf5 file.
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

# Local modules.

# Project modules.
from pysemeels.hitachi.eels_su.elv_file import ElvFile

# Globals and constants variables.


class ConvertElv(object):
    def __init__(self, elv_file_path, convert_msa=True, convert_hdf5=False):
        self.elv_file_path = elv_file_path

        self.convert_msa = convert_msa
        self.convert_hdf5 = convert_hdf5

        self.msa_file_path = None
        self.hdf5_file_path = None

    def convert(self):
        if self.convert_msa:
            self.generate_msa()
        if self.convert_hdf5:
            self.generate_hdf5()

    def generate_msa(self):
        if self.msa_file_path is None:
            file_path, _extension = os.path.splitext(self.elv_file_path)
            file_path += ".msa"

        with open(self.elv_file_path, 'r') as elv_text_file:
            elv_file = ElvFile()
            elv_file.read(elv_text_file)

            elv_file.export_msa(file_path)
