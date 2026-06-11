#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_Beta_vdW/rules"
shortDesc = u""
longDesc = u"""
"""

entry(
    index = 1,
    label = "Abstracting;Donating",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0.,
        alpha = 1.0266256,
        E0 = (138.55907, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
BEP values from "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt", Sutton et al., The Journal of Physical Chemistry C, 2013, 117, 4691-4706
From Table 7 includes beta and alpha position. Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
    """
)

entry(
    index = 2,
    label = "O;R-C-H",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0.,
        alpha = 1.0147839,
        E0 = (128.22272, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
BEP values from "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt", Sutton et al., The Journal of Physical Chemistry C, 2013, 117, 4691-4706
From Table 7 includes beta and alpha position. Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
"""
)

entry(
    index = 3,
    label = "O;R-O-H",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0.,
        alpha = 0.9880278,
        E0 = (122.67981, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
BEP values from "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt", Sutton et al., The Journal of Physical Chemistry C, 2013, 117, 4691-4706
From Table 7 includes beta and alpha position. Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
"""
)

entry(
    index = 4,
    label = "Abstracting;R-CH3",
    kinetics = SurfaceArrheniusBEP(
        A = (1.393e17, 'm^2/(mol*s)'),
        n = 0.,
        alpha = 0.8707618,
        E0 = (128.65091, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
BEP values from "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt", Sutton et al., The Journal of Physical Chemistry C, 2013, 117, 4691-4706
From Table 7 includes beta and alpha position. Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
Divided by 3 because of reaction path degeneracy for CH3 (3 equivalent H atoms)
"""
)

entry(
    index = 5,
    label = "O;R-CH3",
    kinetics = SurfaceArrheniusBEP(
        A = (1.393e17, 'm^2/(mol*s)'),
        n = 0.,
        alpha = 1.0247666,
        E0 = (127.01649, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
BEP values from "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt", Sutton et al., The Journal of Physical Chemistry C, 2013, 117, 4691-4706
From Table 7 includes beta and alpha position. Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
Divided by 3 because of reaction path degeneracy for CH3 (3 equivalent H atoms)
"""
)

entry(
    index = 6,
    label = "Abstracting;R-R-N",
    kinetics = SurfaceArrheniusBEP(
        A = (5.20e21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.6097491,
        E0 = (140.69371, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
This BEP is created from a mixture of data in literature taken from the following papers: 

Ma and Schneider
https://doi.org/10.1021/acscatal.8b04251

Gomez-Díaz and Lopez
https://pubs.acs.org/doi/10.1021/jp1093349

Farberow et al.
https://doi.org/10.1021/cs500668k

Deng et al.
https://pubs.rsc.org/en/content/articlelanding/2014/ra/c3ra46544f

and the current manuscript in progress by Badger et al. looking at the effects
of NO on the light out curves for hydrocarbons.
"""
)

entry(
    index = 7,
    label = "Abstracting;R-N-R",
    kinetics = SurfaceArrheniusBEP(
        A = (5.20e21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.528831,
        E0 = (132.87346, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
This BEP is created from a mixture of data in literature taken from the following papers: 

Ma and Schneider
https://doi.org/10.1021/acscatal.8b04251

Gomez-Díaz and Lopez
https://pubs.acs.org/doi/10.1021/jp1093349

Farberow et al.
https://doi.org/10.1021/cs500668k

Deng et al.
https://pubs.rsc.org/en/content/articlelanding/2014/ra/c3ra46544f

and the current manuscript in progress by Badger et al. looking at the effects
of NO on the light out curves for hydrocarbons.
"""
)
