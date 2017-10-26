#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.tools.batch_convert_elv

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Convert elv file in batch mode.
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
from pysemeels.tools.convert_elv import ConvertElv

# Globals and constants variables.


class BatchConvertElv(object):
    def __init__(self, path, overwrite=True, recursive=True):
        self.path = path

        self.overwrite = overwrite
        self.recursive = recursive

    def convert(self):
        if self.recursive:
            for current_path, folder_names, filenames in os.walk(self.path):
                for file_name in filenames:
                    if file_name.endswith(".elv"):
                        logging.info(file_name)
                        elv_file_path = os.path.join(current_path, file_name)
                        convert_elv = ConvertElv(elv_file_path, self.overwrite)
                        convert_elv.convert()
        else:
            for file_name in os.listdir(self.path):
                if file_name.endswith(".elv"):
                    logging.info(file_name)
                    elv_file_path = os.path.join(self.path, file_name)
                    convert_elv = ConvertElv(elv_file_path, self.overwrite)
                    convert_elv.convert()


