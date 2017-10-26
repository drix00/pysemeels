#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.egerton2011.lenzplus

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Calculates Lenz x-secns for elastic and inelastic scattering.

LENZPLUS.m calculates Lenz x-secns for elastic and inelastic scattering,
then fractions of scattering collected by an aperture, including plural
scattering and broadening of the elastic and inelastic angular distributions
For details, see Egerton "EELS in the EM" 3rd edition, Appendix B.
Correction beta->sin(b) in expresssions for dsidb and dsedb [5 Nov 2012]

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
LenzplusResults = namedtuple('LenzplusResults', ['theta0_rad', 'thetae_rad_rad', 'dse_domega', 'dsi_domega',
                                                 'dse_dbeta', 'dsi_dbeta', 'sigma_elastic_nm2', 'sigma_inelastic_nm2',
                                                 'f_elastic', 'f_inelastic', 'total_inelastic_elastic_ratio'])

LenzplusResults2 = namedtuple('LenzplusResults2', ['t_lambda_beta'])

LenzplusResults3 = namedtuple('LenzplusResults3', ['p_unscat', 'p_el', 'p_inel', 'p_total', 'I0_I', 'Ii_I', 'lnIt_I0'])

def lenz_plus(e0, e, z, beta, toli):
    # Get E0(keV), Ebar(eV), Z, BeTa(mrad)
    logging.info('----------------------------------')  # start input
    if e == 0:
        e = 6.75 * z

    logging.info('E0(keV), Ebar(eV), Z, BeTa(mrad) are: %g, %g, %g, %g', e0, e, z, beta)

    gt = 500 * e0 * (1022 + e0) / (511 + e0)
    te = e / 2 / gt
    a0 = .0529
    gm = 1 + e0 / 511
    vr = np.sqrt(1 - 1 / gm / gm)
    k0 = 2590 * gm * vr
    coeff = 4 * gm * gm * z / a0 / a0 / k0 ** 4
    r0 = .0529 / z ** .3333  # units of nm
    t0 = 1 / k0 / r0
    logging.info('Theta0 = %0.4E rad \t\t\t\t\t ThetaE = %0.4E rad', t0, te)
    b = beta / 1000
    b2 = b * b
    te2 = te * te
    t02 = t0 * t0
    dsidom = coeff / (b2 + te2) / (b2 + te2) * (1 - t02 * t02 / (b2 + te2 + t02) / (b2 + te2 + t02))
    dsidb = 2 * 3.142 * np.sin(b) * dsidom
    # t1=b2/te2/(b2+te2)
    # t2=(2*b2+2*te2+t02)/(b2+te2)/(b2+te2+t02)
    # t3=-(t02+2*te2)/te2/(t02+te2)
    # t4=(2/t02)*log((b2+te2)*(t02+te2)/te2/(b2+t02+te2))
    # sigin=3.142*coeff*(t1+t2+t3+t4)
    sigin = 8 * 3.142 * gm * gm * z ** 0.333 / k0 / k0 * np.log((b2 + te2) * (t02 + te2) / te2 / (b2 + t02 + te2))
    # silim=3.142*coeff*2/t02*log(t02/te2) %asymptotic inelastic
    silim = 16 * 3.142 * gm * gm * z ** 0.333 / k0 / k0 * np.log(t0 / te)  # asymptotic inelastic
    f1i = sigin / silim
    # dsedom=z*coeff/(b2+t02)^2 % corrected from EELS2
    dsedom = z * coeff / (np.sin(b / 2) * np.sin(b / 2) + np.sin(t0 / 2) * np.sin(t0 / 2)) ** 2  # no small-angle
    dsedb = dsedom * 2 * 3.142 * np.sin(b)  # diffl. elastic
    selim = 4 * 3.142 * gm * gm * z ** 1.333 / k0 / k0  # asymptotic elastic
    f1e = 1 / (1 + t02 / b2)
    sigel = f1e * selim

    logging.info('dSe/dOmega = %0.4E nm^2/sr \t\t\t dSi/dOmega = %0.4E nm^2/sr', dsedom, dsidom)
    logging.info('dSe/dBeta = %0.4E nm^2/rad \t\t\t dSi/dBeta = %0.4E nm^2/rad', dsedb, dsidb)
    logging.info('Sigma(elastic) = %0.4E nm^2 \t\t\t Sigma(inelastic) = %0.4E nm^2', sigel, sigin)
    logging.info('F(elastic) = %0.4E \t\t\t\t\t F(inelastic) = %0.4E', f1e, f1i)
    nu = silim / selim
    logging.info('total-inelastic/total-elastic ratio = %0.4E', nu)

    result1 = LenzplusResults(t0, te, dsedom, dsidom, dsedb, dsidb, sigel, sigin, f1e, f1i, nu)

    # Get t/lambdaI
    if toli != 0:
        logging.info('t/lambda(beta)= %0.4E', toli * f1i)

        tole = toli / nu
        xe = np.exp(-tole)
        xi = np.exp(-toli)
        fie = f1e * f1i
        pun = xe * xi
        pel = (1 - xe) * xi * f1e
        pz = pun + pel
        pin = xe * (1 - xi) * f1i
        pie = (1 - xi) * (1 - xe) * fie
        pi = pin + pie

        logging.info('p(unscat) = %0.4E \t\t P(el) = %0.4E neglecting elastic broadening', pun, pel)
        logging.info('p(inel) = %0.4E \t\t\t P(in+el) = %0.4E neglecting inelastic broadening', pin, pie)
        logging.info('I0/I = %0.4E \t\t\t\t Ii/I = %0.4E neglecting angular broadening', pz, pi)
        pt = pz + pi
        lr = np.log(pt / pz)
        logging.info('ln(It/I0) = %0.4E without broadening', lr)

        result3_wo_broadening = LenzplusResults3(pun, pel, pin, pie, pz, pi, lr)

        f2e = 1 / (1 + 1.7 ** 2 * t02 / b2)
        f3e = 1 / (1 + 2.2 ** 2 * t02 / b2)
        f4e = 1 / (1 + 2.7 ** 2 * t02 / b2)
        pe = xe * (tole * f1e + tole ** 2 * f2e / 2 + tole ** 3 * f3e / 6 + tole ** 4 * f4e / 24)
        peni = pe * xi
        pu = xi * xe
        rz = pu + peni  # unscattered and el/no-inel compts.
        # pel=xi*xe*(np.exp(tole*f1e)-1) #not used
        # pz=pun+pel #not used
        pi = xi * (np.exp(toli * f1i) - 1)
        pine = xe * pi
        pie = pi * pe
        ri = pine + pie

        logging.info('P(unscat) = %0.4E \t\t P(el only) = %0.4E with elastic broadening', pu, peni)
        # ang distrib of inel+el taken same as broadened elastic
        logging.info('P(inel only) = %0.4E \t\t P(in+el) = %0.4E with inelastic broadening', pine, pie)
        logging.info('I0/I = %0.4E \t\t\t\t Ii/I = %0.4E with angular broadening', rz, ri)
        rt = rz + ri
        lr = np.log(rt / rz)
        logging.info('ln(It/I0) = %0.4E with angular broadening', lr)

        result3_w_broadening = LenzplusResults3(pu, peni, pine, pie, rz, ri, lr)

        result2 = LenzplusResults2(toli * f1i)

    return result1, result2, result3_wo_broadening, result3_w_broadening
