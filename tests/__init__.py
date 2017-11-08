#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for package :py:mod:`pysemeels`.
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
import logging

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.


def _is_git_lfs_file(input_file):
    lines = []
    try:
        lines = input_file.readlines()
    except UnicodeDecodeError as message:
        logging.debug(message)
        if len(lines) > 0:
            logging.debug(lines[0])
        return False

    if len(lines) > 0:
        logging.debug(lines[0])
    if lines[0].startswith("version https://git-lfs.github.com/spec"):
        return True
    else:
        return False


def is_git_lfs_file(file_path):
    if isinstance(file_path, str):
        with open(file_path, 'r') as input_file:
            return _is_git_lfs_file(input_file)

    return _is_git_lfs_file(file_path)


def is_bad_file(file_path):
    if isinstance(file_path, str):
        if os.path.isfile(file_path) and not is_git_lfs_file(file_path):
            return False
        else:
            return True
    elif not is_git_lfs_file(file_path):
        return False
    else:
        return True
