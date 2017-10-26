#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.egerton2011.sigadf

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Calculates high-angle cross sections for high-angle elastic scattering, as utilized in an annular dark-field
(ADF) detector.

based on an analytical formula (Banhart, 1999 Eq.5) using the McKinley-Feshbach (1948) approximation, valid for Z < 28

Details in R.F.Egerton: EELS in the Electron Microscope, 3rd edition,  with correction made (8 Sept. 2011)
to Eq.(3.12f) and  to Mott x-secn.

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
SigadfResults = namedtuple('SigadfResults', ['lenz_screening_angle_mrad', 'rutherford_cross_section_barn',
                                             'mott_cross_section_barn'])


def sig_adf(Z, A, qn, qx, E0):

    logging.info('------------SigADF-------------')
    logging.info('SigADF: HAADF elastic cross sections')
    logging.info('Atomic number Z : %g', Z)
    logging.info('Atomic weight A : %g', A)
    logging.info('Minimum scattering angle(mrad) : %g', qn)
    logging.info('Maximum scattering angle(mrad) : %g', qx)
    logging.info('Incident-electron energy E0(keV) : %g', E0)

    Al = Z / 137 # fine-structure constant
    a0 = 5.29e-11 # in m
    R = 13.606 # bohr radius in m, rydberg energy in ev
    #evfac = 2000 * E0 * (E0 + 1022) / 511 # rhs factor in eq.(5.17)
    t = E0 * (1 + E0 / 1022) / (1 + E0 / 511) ** 2  # m0v^2/2
    b = np.sqrt(2 * t / 511)  # v/c
    k0 = 2590E9*(1 + E0/511)*b  # m^-1
    q0 = 1000*Z**0.3333/k0/a0  # Lenz screening angle in mrad

    logging.info('Lenz screening angle = %g mrad', q0)
    if q0 > qn:
        logging.info('WARNING: minimum angle < Lenz screening angle!')

    newrf = (1 - b * b) / b ** 4  # relativistic factor
    smin = (np.sin(qn/2000)) ** 2
    smax = (np.sin(qx/2000)) ** 2
    x = 1/smin - 1/smax  # spherical potential
    sdc = .2494 * Z ** 2 * newrf * x  # Rutherford
    logging.info('Rutherford cross section = %g barn', sdc)

    coef = 4 * Z ** 2 * R ** 2 / (511000) ** 2
    sqb = 1 + 2 * np.pi * Al * b + (b * b + np.pi * Al * b) * np.log(x)
    brace = 1 + 2 * np.pi * Al * b / np.sqrt(x) - sqb / x
    sdmf = 9.999999E+27 * coef * x * np.pi * a0 * a0 * (1 - b*b) / b ** 4 * brace
    logging.info('McKinley-Feshbach-Mott cross section = %g barn', sdmf)

    result = SigadfResults(q0, sdc, sdmf)
    return result
