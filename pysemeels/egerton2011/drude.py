#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.egerton2011.drude
   :synopsis: Simulation of a low-loss spectrum using Drude model.

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Simulation of a low-loss spectrum using Drude model.
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

# Third party modules.
import numpy as np

# Local modules.

# Project modules.

# Globals and constants variables.

def drude(ep, ew, eb, epc, e0, beta, nn, tnm):
    """
    Given the plasmon energy (ep), plasmon FWHM (ew) and binding energy (eb), 
    this program generates:
    EPS1, EPS2 from modified Eq. (3.40), ELF=Im(-1/EPS) from Eq. (3.42),
    single scattering from Eq. (4.26) and SRFINT from Eq. (4.31)
    The output is e,ssd into the file Drude.ssd (for use in Flog etc.) 
    and e,eps1 ,eps2 into Drude.eps (for use in Kroeger etc.)
     Gives probabilities relative to zero-loss integral (I0 = 1) per eV
     Details in R.F.Egerton: EELS in the Electron Microscope, 3rd edition, Springer 2011)
     Version 10.11.26
    """

    logging.info('plasmon energy (eV): %g', ep)
    logging.info('plasmon width (eV) : %g', ew)
    logging.info('binding energy (eV): %g', eb)
    logging.info('ev/channel : %g', epc)
    logging.info('E0(kev) : %g', e0)
    logging.info('beta(mrad) : %g', beta)
    logging.info('number of data points : %g', nn)
    logging.info('thickness(nm) : %g', tnm)

    b = beta / 1000. # rad
    T = 1000. * e0 * (1. + e0 / 1022.12) / (1. + e0 / 511.06)**2  # eV
    tgt = 1000. * e0 * (1022.12 + e0) / (511.06 + e0)  # eV
    rk0 = 2590. * (1. + e0 / 511.06) * np.sqrt(2. * T / 511060)
    fideps = open('Drude.eps', 'w')
    fidssd = open('Drude.ssd', 'w')

    iw = np.arange(2, nn+2)
    e = epc * (iw - 1.0)
    eps = 1.0 - ep**2 / (e**2 - eb**2 + e * ew * 1.0j)
    eps1 = np.real(eps)
    eps2 = np.imag(eps)
    # eps1 = 1.0 - ep**2  / (e**2 + ew**2)
    # eps2 = ew * ep**2 / e / (e**2 + ew**2)
    elf = ep**2 * e * ew / ((e**2 - ep**2)**2 + (e * ew)**2)
    rereps = eps1 / (eps1 * eps1 + eps2 * eps2)
    the = e / tgt  # varies with energy loss!
    # srfelf = 4..*eps2./((1+eps1).^2+eps2.^2) - elf %equivalent
    srfelf = np.imag(-4.0 / (1.0 + eps)) - elf # for 2 surfaces
    angdep = np.arctan(b / the) / the - b / (b * b + the * the)
    srfint = angdep * srfelf / (3.1416 * 0.0529 * rk0 * T)  # probability per eV
    anglog = np.log(1.0 + b * b / the / the)
    volint = tnm / 3.1416 / 0.0529 / T / 2. * elf * anglog  # probability per eV
    ssd = volint + srfint

    # %fprintf(fidssd,['%0.15g %0.15g %0.15g %0.15g \n'], [evolintsrfintssd])
    # fprintf(fidssd,['%0.15g %0.15g\n'], [essd])
    # fprintf(fideps,['%0.15g %0.15g %0.15g \n'], [eeps1eps2])
    # fclose(fidssd)
    # fclose(fideps)
    # %fprintf(1,'For Ep(eV) = %f, width(eV) = %f, Eb(eV) = %f, eV/ch = %f \n',ep,ew,eb,epc)
    # %fprintf(1,'beta(mrad) = %f, E0(keV) = %f, t(nm) = %f, #chan = %f\n',beta,e0,tnm,nn)

    # %Integrate over all energy loss
    Ps = np.trapz(srfint, e) # 2 surfaces but includes negative begrenzungs contribn.
    Pv = np.trapz(volint, e) # integrated volume probability
    lam = tnm / Pv # does NOT depend on free-electron approximation (no damping).
    lamfe = 4. * 0.05292 * T / ep / np.log(1.0 + (b * tgt / ep)**2)  # Eq.(3.44) approximation
    logging.info('Ps(2surfaces+begrenzung terms)=%g,Pv=t/lambda(beta)= %g', Ps, Pv)
    logging.info('Volume-plasmon MFP(nm) = %g, Free-electron MFP(nm) = %f', lam, lamfe)
    logging.info('--------------------------------')

    return e, eps1, eps2, elf, srfelf, rereps, ssd, volint, srfint, Ps, Pv, lam, lamfe

def plot_figure():
    energies_eV, eps1, eps2, im_eps, im4_eps, re_eps, probabilities_total, probabilities_volume, probabilities_surface, ps, pv, mfp_volume_nm, mfp_free_nm = drude(
        15, 3, 0, 0.1, 200, 5, 500, 50)

    plt.figure()
    plt.title('Drude dielectric data')

    plt.plot(energies_eV, eps1, 'r', label='eps1')

    plt.plot(energies_eV, eps2, 'g', label='eps2')
    plt.plot(energies_eV, im_eps, 'k', label='Im[-1/eps]')
    plt.plot(energies_eV, im4_eps, 'b', label='Im[(-4/(1+eps)]')
    plt.plot(energies_eV, re_eps, 'm', label='Re[1/eps]')

    plt.legend()
    plt.xlabel('Energy Loss [eV]')
    yScaleMax = 10
    plt.ylim((-yScaleMax, yScaleMax))

    # Plot volume, surface and total intensities
    plt.figure()
    plt.title('Drude probabilities')
    plt.plot(energies_eV, probabilities_volume, 'r', label='volume')
    plt.plot(energies_eV, probabilities_surface, 'g', label='surface')
    plt.plot(energies_eV, probabilities_total, 'b', label='total')
    plt.xlabel('Energy Loss [eV]')
    plt.ylabel('dP/dE [/eV]')

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    plot_figure()

    plt.show()
