#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.egerton2011.spec_gen
   :synopsis: Generates a plural-scattering distribution from a gaussian-shaped ssd of width wp, peaked at ep, 
   with background and poisson shot noise.

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Generates a plural-scattering distribution from a gaussian-shaped ssd of width wp, peaked at ep, with background 
and poisson shot noise.

Details in R.F.Egerton: EELS in the Electron Microscope, 3rd edition, Springer 2011)
Version 10.11.26
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
import matplotlib.pyplot as plt

# Local modules.

# Project modules.

# Globals and constants variables.

def spec_gen(ep, wp, wz, ez, epc, a0, tol, nd, back, fback, cpe):

    logging.info('   SpecGen(ep, wp, wz, ez, epc, a0, tol, nd, back, fback, cpe)')

    # persistent psd ssd
    psd = np.zeros(nd)
    ssd = np.zeros(nd)
    outssd = np.zeros(nd)
    outpsd = np.zeros(nd)
    eout = np.zeros(nd)

    # fid_1 = open('SpecGen.ssd', 'w+')  #contains SSD in xy format, with no background
    # fid_2 = open('SpecGen.psd', 'w+')  # contains the plural scattering distrib. with Z-L at EZ

    logging.info('SpecGen: plasmon energy (eV) = %g', ep)
    logging.info('plasmon FWHM (eV) : %g', wp)
    logging.info('zero-loss FWHM (eV): %g', wz)
    logging.info('zero-loss offset from first channel (eV): %g', ez)
    logging.info('eV/channel: %g', epc)
    logging.info('zero-loss total_spectra: %g', a0)
    logging.info('t/lambda: %g', tol)
    logging.info('number of channels: %g', nd)
    logging.info('instrumental background level (total_spectra/channel): %g', back)
    logging.info('instrumental noise/background (e.g. 0.1): %g', fback)
    logging.info('spectral total_spectra per beam electron (e.g. 0.1): %g', cpe)


    logging.info('-------------------------------\n')
    fpoiss = cpe ** 0.5
    sz = wz/1.665  # convert from FWHM to standard deviation
    sp = wp/1.665
    hz = a0/sz/1.772  # height of ZLP (epc* removed)
    rlnum = 1.23456

    # calculate intensity at each energy loss E :
    for i in range(nd):
        e = (i+1)*epc - ez
        fac = 1
        psd[i] = 0
        # sum contribution from each order of scattering:
        for order in range(0, 14+1):
            sn = np.sqrt(sz*sz+order*sp*sp)
            xpnt = (e-order*ep)**2/sn/sn
            if xpnt > 20.0:
                expo = 0.0

            if xpnt <= 20.0:
                expo = np.exp(-xpnt)

            dne = hz*sz/sn*expo/fac*tol**order
            rndnum = 2*((np.fix(rlnum))-rlnum)
            snoise = fpoiss*(np.sqrt(dne)*rndnum)
            rlnum = 9.8765*rndnum
            if order == 1:  # check if 1 or 0
                bnoise = fback*back*rndnum
                ssd[i] = dne + np.sqrt(snoise*snoise+bnoise*bnoise)
                outssd[i] = ssd[i] + back
                # line = '%0.15g %0.15g\n' % (e, outssd[i])
                # fid_1.write(line)

            psd[i] = psd[i] + dne
            fac = fac*(order+1)

        snoise = fpoiss*(np.sqrt(psd[i])*rndnum)
        outpsd[i] = psd[i] + np.sqrt(snoise*snoise+bnoise*bnoise)+back
        # line = '%0.15g %0.15g\n' % (e, outpsd[i])
        # fid_2.write(line)
        eout[i] = e

    return eout, outssd, outpsd

def create_figure(eout, outssd, outpsd):
    plt.figure()
    plt.plot(eout, outssd, 'b', label='SSD')
    plt.plot(eout, outpsd, ':r', label='PSD')

    plt.title('SpecGen')
    plt.xlabel('Energy Loss [eV]')
    plt.ylabel('Counts/channel')


if __name__ == '__main__':
    eout, outssd, outpsd = spec_gen(16.7, 3.2, 1, 5, 0.1, 10000, 1.5, 1000, 2, 0.5, 10)

    create_figure(eout, outssd, outpsd)

    plt.show()
