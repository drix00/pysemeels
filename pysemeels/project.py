#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.project

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Container of EELS data.

The EELS data are:

* raw EELS linescan
* spectral imaging

    * point
    * line scan
    * map

* EFSTEM image

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
from pysemeels.raw_spectrum import RawSpectrum
from pysemeels.si.point import Point
from pysemeels.si.linescan import Linescan
from pysemeels.si.map import Map
from pysemeels.eftem import Eftem

# Globals and constants variables.
HDF5_ATTRIBUTE_AUTHOR = "author"
HDF5_GROUP_SPECTRA = "spectra"
HDF5_GROUP_SPECTRAL_IMAGING = "spectral imaging"
HDF5_GROUP_POINTS = "points"
HDF5_GROUP_LINE_SCANS = "line scans"
HDF5_GROUP_MAPS = "maps"
HDF5_GROUP_ENERGY_FILTERED_MICROGRAPHS = "energy filtered micrographs"


class Project(object):
    def __init__(self, name):
        self.name = name
        self.author = ""

        self.spectra = []
        self.si_points = []
        self.si_line_scans = []
        self.si_maps = []
        self.energy_filtered_micrographs = []

    def read_hdf5(self, parent_group):
        if self.name in parent_group:
            project_group = parent_group[self.name]
            self.author = project_group.attrs[HDF5_ATTRIBUTE_AUTHOR]

            if HDF5_GROUP_SPECTRA in project_group:
                group = project_group[HDF5_GROUP_SPECTRA]
                for name in group.keys():
                    data = RawSpectrum(name)
                    data.read_hdf5(group)

            if HDF5_GROUP_SPECTRAL_IMAGING in project_group:
                si_group = project_group[HDF5_GROUP_SPECTRAL_IMAGING]
                if HDF5_GROUP_POINTS in si_group:
                    group = si_group[HDF5_GROUP_POINTS]
                    for name in group.keys():
                        data = Point(name)
                        data.read_hdf5(group)

                if HDF5_GROUP_LINE_SCANS in si_group:
                    group = si_group[HDF5_GROUP_LINE_SCANS]
                    for name in group.keys():
                        data = Linescan(name)
                        data.read_hdf5(group)

                if HDF5_GROUP_MAPS in si_group:
                    group = si_group[HDF5_GROUP_MAPS]
                    for name in group.keys():
                        data = Map(name)
                        data.read_hdf5(group)

            if HDF5_GROUP_ENERGY_FILTERED_MICROGRAPHS in project_group:
                group = project_group[HDF5_GROUP_ENERGY_FILTERED_MICROGRAPHS]
                for name in group.keys():
                    data = Eftem(name)
                    data.read_hdf5(group)

        else:
            raise ValueError("The parent group does not contain the project")

    def write_hdf5(self, parent_group):
        project_group = parent_group.require_group(self.name)

        project_group.attrs[HDF5_ATTRIBUTE_AUTHOR] = self.author

        if self.spectra:
            group = project_group.require_group(HDF5_GROUP_SPECTRA)
            for spectrum in self.spectra:
                spectrum.write_hdf5(group)

        if self.si_points:
            group = project_group.require_group(HDF5_GROUP_SPECTRAL_IMAGING)
            group = group.require_group(HDF5_GROUP_POINTS)
            for si_point in self.si_points:
                si_point.write_hdf5(group)

        if self.si_line_scans:
            group = project_group.require_group(HDF5_GROUP_SPECTRAL_IMAGING)
            group = group.require_group(HDF5_GROUP_LINE_SCANS)
            for si_line_scan in self.si_line_scans:
                si_line_scan.write_hdf5(group)

        if self.si_maps:
            group = project_group.require_group(HDF5_GROUP_SPECTRAL_IMAGING)
            group = group.require_group(HDF5_GROUP_MAPS)
            for si_map in self.si_maps:
                si_map.write_hdf5(group)

        if self.energy_filtered_micrographs:
            group = project_group.require_group(HDF5_GROUP_ENERGY_FILTERED_MICROGRAPHS)
            for energy_filtered_micrograph in self.energy_filtered_micrographs:
                energy_filtered_micrograph.write_hdf5(group)
