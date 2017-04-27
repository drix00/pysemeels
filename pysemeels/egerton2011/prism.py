#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.egerton2011.prism
   :synopsis: First order focusing based on Eq 2.8, 2.9, 2.10, and 2.11 in Egerton (2011) book.

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

First order focusing based on Eq 2.8, 2.9, 2.10, and 2.11 in Egerton (2011) book.

Details in: EELS in the Electron Microscope, 3rd edition, Springer 2011.
Corrections (28Sep2011): convert psi to psid (in degrees) at line 76, 
and add line 97:  m11(3,4) = phi.*R.*3.14159265./180.

"""

###############################################################################
# Copyright 2017 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License")
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
import logging
from collections import namedtuple

# Third party modules.
import numpy as np

# Local modules.

# Project modules.

# Globals and constants variables.
PrismResults = namedtuple('PrismResults', ['v', 'x', 'xp','y','yp'])

def prism( u, eps1, eps2, K1, g, R, phi, v ):
    logging.info("-----------------Prism---------------")
    logging.info('Object distance u : %g', u)
    logging.info('Entrance tilt epsilon1 (deg): %g', eps1)
    logging.info('Exit tilt epsilon2 (deg): %g', eps2)
    logging.info('Fringing-field parameter K1 (e.g. 0 or 0.4): %g', K1)
    logging.info('Polepiece gap g : %g', g)
    logging.info('Bend radius R : %g', R)
    logging.info('Bend angle phi (deg) : %g', phi)
    logging.info('Image distance v : %g', v)

    x0 = 0
    y0 = 0
    dx0 = 0.001 # 1 mrad entrance
    dy0 = 0.001 # 1 mrad entrance

    xy0 = [x0, dx0, y0, dy0]

    xy = eq8(xy0, u)
    xy = eq9(xy, eps1, K1, g, R) # caclulate for eps1
    xy = eq11(xy, phi, R) # magnetic field
    xy = eq9(xy, eps2, K1, g, R) # calculate for eps2

    fl = -xy[1-1] / xy[2-1]

    logging.info('Entrance-cone semi-angle = 1 mrad.')
    logging.info('For v = %g', v)
    ans1 = eq8(xy, v)
    result1 = PrismResults(v, ans1[0], ans1[1], ans1[2], ans1[3])
    logging.info("x  = %g", result1.x)
    logging.info("x' = %g", result1.xp)
    logging.info("y  = %g", result1.y)
    logging.info("y' = %g", result1.yp)
    logging.info('For v = %g', fl)
    ans2 = eq8(xy, fl)
    result2 = PrismResults(fl, ans2[0], ans2[1], ans2[2], ans2[3])
    logging.info("x  = %g", result2.x)
    logging.info("x' = %g", result2.xp)
    logging.info("y  = %g", result2.y)
    logging.info("y' = %g", result2.yp)

    return result1, result2


def eq8(xy, u):
    m8 = np.eye(4)
    m8[0, 1] = u
    m8[2, 3] = u
    xy = np.dot(m8, xy)

    return xy


def eq9(xy, eps, K1, g, R):

    psi = (g/ R) * K1 * (1 + np.sin(np.radians(eps)) ** 2) / np.cos(np.radians(eps))
    psid = psi * 180. / 3.14159265 # convert to degrees

    m9 = np.eye(4)
    m9[2-1, 1-1] = np.tan(np.radians(eps)) / R
    m9[4-1, 3-1] = -np.tan(np.radians(eps - psid)) / R
    xy = np.dot(m9, xy)

    return xy

def eq11(xy, phi, R):
    m11 = np.eye(4)
    m11[1-1, 1-1] = np.cos(np.radians(phi))
    m11[2-1, 1-1] = -np.sin(np.radians(phi)) / R
    m11[1-1, 2-1] = R * np.sin(np.radians(phi))
    m11[2-1, 2-1] = np.cos(np.radians(phi))
    m11[3-1, 4-1] = phi * R * 3.14159265 / 180.
    xy = np.dot(m11, xy)

    return xy
