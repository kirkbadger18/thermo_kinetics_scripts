#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_Beta_double_vdW/rules"
shortDesc = u""
longDesc = u"""
"""

entry(
    index = 1,
    label = "Abstracting;Donating",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0.,
        alpha = 0.76552427,
        E0 = (111.651764, 'kJ/mol'),
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
    label = "OH;R-C-H",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0.,
        alpha = 0.6609393,
        E0 = (110.910484, 'kJ/mol'),
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
    label = "OH;R-O-H",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0.,
        alpha = 0.01191638,
        E0 = (3, 'kJ/mol'),
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
        alpha = 0.60744196,
        E0 = (105.50783, 'kJ/mol'),
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
    label = "OH;R-CH3",
    kinetics = SurfaceArrheniusBEP(
        A = (1.393e17, 'm^2/(mol*s)'),
        n = 0.,
        alpha = 0.678192,
        E0 = (106.26912, 'kJ/mol'),
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


