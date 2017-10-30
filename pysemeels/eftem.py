#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.linescan

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Raw EELS EFTEM data.
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


class Eftem(object):
    def __init__(self, name):
        self.name = name

    def read_hdf5(self, parent_group):
        if self.name in parent_group:
            project_group = parent_group[self.name]
        else:
            raise ValueError("The parent group does not contain the project")

    def write_hdf5(self, parent_group):
        project_group = parent_group.require_group(self.name)
