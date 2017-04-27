#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.egerton2011.sigdis
   :synopsis: Calculates cross sections for bulk atomic displacement or surface sputtering for both SPHERICAL and 
   PLANAR escape potentials.

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Calculates cross sections for bulk atomic displacement or surface sputtering for both SPHERICAL and 
PLANAR escape potentials.

sigdis.m calculates cross sections for bulk atomic displacement or 
surface sputtering for both SPHERICAL and PLANAR escape potentials, 
based on an analytical formula (Banhart, 1999 Eq.5) that uses the
McKinley-Feshbach (1948) approximation, valid for Z < 28
For Z>28, the Rutherford value should be used as a better approximation.

Details in R.F.Egerton: EELS in the Electron Microscope, 3rd edition, Springer 2011

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
SigdisResults = namedtuple('SigdisResults', ['emax_eV', 'threshold_keV', 'emin_eV', 'spherical_escape_potential_barn',
                                             'planar_escape_potential_barn', 'spherical_potential_barn',
                                             'planar_potential_barn'])

def sigdis(Z, A, Ed, E0):
    logging.info('-------------Sigdis------------')
    logging.info('sigdis: Atomic-displacement cross sections:')

    logging.info('Atomic number Z : %g', Z)
    logging.info('Atomic weight A : %g', A)
    logging.info('Surface or bulk displacement energy Ed(eV) : %g', Ed)
    logging.info('Incident-electron energy E0(keV) : %g', E0)

    Al = Z / 137
    A0 = 5.29e-11
    R = 13.606 # bohr radius in m, rydberg energy in ev
    #evfac = 2000 * E0 * (E0 + 1022) / 511 % rhs factor in eq.(5.17)
    t = E0 * (1 + E0 / 1022) / (1 + E0 / 511) ** 2
    b = np.sqrt(2 * t / 511)
    newrf = (1 - b * b) / b ** 4
    Emax = (E0 / A) * (E0 + 1022) / 465.7 # originally /460 from reimer
    E0min = 511 * (np.sqrt(1 + A * Ed / 561) - 1) # threshold in keV
    logging.info('Emax(eV) = %g eV, threshold = %g keV', Emax, E0min)
    coef = 4 * Z ** 2 * R ** 2 / (511000) ** 2
    Emin = np.sqrt(Ed * Emax) # for planar potential, otherwise Emin = Ed
    logging.info('Emin(planar potential) = %g eV', Emin)
    x = Emax / Ed # spherical potential
    xp = Emax / np.sqrt(Ed * Emax) # planar potential
    sdc = .2494 * Z ** 2 * newrf * (x - 1)
    pdc = .2494 * Z ** 2 * newrf * (xp - 1)
    logging.info('Rutherford value (spherical escape potential)= %g barn', sdc)
    logging.info('Rutherford value (planar escape potential)= %g barn', pdc)
    sqb = 1 + 2 * np.pi * Al * b + (b * b + np.pi * Al * b) * np.log(x)
    brace = 1 + 2 * np.pi * Al * b / np.sqrt(x) - sqb / x
    sdmf = 9.999999E+27 * coef * x * np.pi * A0 * A0 * (1 - b * b) / b ** 4 * brace
    logging.info('McKinley-Feshbach-Mott (spherical potential)= %g barn', sdmf)
    psqb = 1 + 2 * np.pi * Al * b + (b * b + np.pi * Al * b) * np.log(xp)
    pbrace = 1 + 2 * np.pi * Al * b / np.sqrt(xp) - psqb / xp
    pdmf = 9.999999E+27 * coef * xp * np.pi * A0 * A0 * (1 - b * b) / b ** 4 * pbrace
    logging.info('McKinley-Feshbach-Mott (planar potential) = %g barn', pdmf)

    result = SigdisResults(Emax, E0min, Emin, sdc, pdc, sdmf, pdmf)
    return result
