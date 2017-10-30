#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Python scripts to analyze SEM EELS data.
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
#: Maintainer of the project.
author = """Hendrix Demers"""
#: Email of the maintainer of the project.
email = 'hendrix.demers@mail.mcgill.ca'
version = '0.1.0'
"""
Version of the project.

.. note::
    The version of the project should be changed here.

"""


def get_current_module_path(module_filepath, relative_path=""):
    """
    Return the current module path by using :py:obj:`__file__` special module variable.

    An example of usage::

        module_path = get_current_module_path(__file__)

    :param str module_filepath: Pass :py:obj:`__file__` to get the current module path
    :param str relative_path: Optional parameter to return a path relative to the module path
    :return: a path, either the module path or a relative path from the module path
    :rtype: str
    """
    base_path = os.path.dirname(module_filepath)
    logging.debug(base_path)

    file_path = os.path.join(base_path, relative_path)
    logging.debug(file_path)
    file_path = os.path.normpath(file_path)

    return file_path
