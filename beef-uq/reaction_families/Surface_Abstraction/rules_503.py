#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Abstracting;Donating",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.35421813,
        E0 = (100.062775, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
These numbers for the general BEP are from the abstraction reaction of C-H to C.
BEP values from "Quantifying the Impact of Parametric Uncertainty on Automatic Mechanism Generation for CO2 Hydrogenation on Ni(111)", Kreitz et al., JACS Au, 2021, 1, 10, 1656-1673 DOI:10.1021/jacsau.1c00276
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
    """,
)

entry(
    index = 2,
    label = "Abstracting;*R-H",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.46095803,
        E0 = (103.37114, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Made up""",
    longDesc = u"""
These numbers for the general BEP are from the abstraction reaction of C-H to C.
BEP values from "Quantifying the Impact of Parametric Uncertainty on Automatic Mechanism Generation for CO2 Hydrogenation on Ni(111)", Kreitz et al., JACS Au, 2021, 1, 10, 1656-1673 DOI:10.1021/jacsau.1c00276
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
    """
)

entry(
    index = 3,
    label = "O;*C-H",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.86718905,
        E0 = (119.35462, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
These numbers for the BEP are from the abstraction reaction of C-H to O.
BEP values from "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt", Sutton et al., The Journal of Physical Chemistry C, 2013, 117, 4691-4706, DOI:10.1021/jp312593u
From Table 7 includes beta and alpha position. Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
    """
)

entry(
    index = 4,
    label = "O;*OH",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.59930074,
        E0 = (13.250076, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
These numbers for the BEP are from the abstraction reaction of O-H to O.
BEP values from "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt", Sutton et al., The Journal of Physical Chemistry C, 2013, 117, 4691-4706, DOI:10.1021/jp312593u
From Table 7 includes beta and alpha position. Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
    """
)

entry(
    index = 5,
    label = "C;*C-H",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.383107,
        E0 = (112.92116, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
These numbers for the general BEP are from the abstraction reaction of C-H to C.
BEP values from "Quantifying the Impact of Parametric Uncertainty on Automatic Mechanism Generation for CO2 Hydrogenation on Ni(111)", Kreitz et al., JACS Au, 2021, 1, 10, 1656-1673 DOI:10.1021/jacsau.1c00276
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
"""
)

entry(
    index = 6,
    label = "O;*=CH-H",
    kinetics = SurfaceArrheniusBEP(
        A = (2.09e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.9473327,
        E0 = (120.30895, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
These numbers for the BEP are from the abstraction reaction of C-H to O.
BEP values from "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt", Sutton et al., The Journal of Physical Chemistry C, 2013, 117, 4691-4706, DOI:10.1021/jp312593u
From Table 7 includes beta and alpha position. Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
Divided by 2 because of reaction path degeneracy for CH2 (2 equivalent H atoms)
    """
)

entry(
    index = 7,
    label = "O;*-CH-H",
    kinetics = SurfaceArrheniusBEP(
        A = (2.09e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.8875983,
        E0 = (117.451324, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
These numbers for the BEP are from the abstraction reaction of C-H to O.
BEP values from "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt", Sutton et al., The Journal of Physical Chemistry C, 2013, 117, 4691-4706, DOI:10.1021/jp312593u
From Table 7 includes beta and alpha position. Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
Divided by 2 because of reaction path degeneracy for CH2 (2 equivalent H atoms)
    """
)

entry(
    index = 8,
    label = "C;*-CH-H",
    kinetics = SurfaceArrheniusBEP(
        A = (2.09e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.44772756,
        E0 = (85.472916, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
These numbers for the general BEP are from the abstraction reaction of C-H to C.
BEP values from "Quantifying the Impact of Parametric Uncertainty on Automatic Mechanism Generation for CO2 Hydrogenation on Ni(111)", Kreitz et al., JACS Au, 2021, 1, 10, 1656-1673 DOI:10.1021/jacsau.1c00276
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
Divided by 2 because of reaction path degeneracy for CH2 (2 equivalent H atoms)
"""
)

entry(
    index = 9,
    label = "C;*=CH-H",
    kinetics = SurfaceArrheniusBEP(
        A = (2.09e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.2929069,
        E0 = (93.78377, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
These numbers for the general BEP are from the abstraction reaction of C-H to C.
BEP values from "Quantifying the Impact of Parametric Uncertainty on Automatic Mechanism Generation for CO2 Hydrogenation on Ni(111)", Kreitz et al., JACS Au, 2021, 1, 10, 1656-1673 DOI:10.1021/jacsau.1c00276
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
Divided by 2 because of reaction path degeneracy for CH2 (2 equivalent H atoms)
    """
)


entry(
    index = 10,
    label = "C;*-CH2-H",
    kinetics = SurfaceArrheniusBEP(
        A = (1.393e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.28276893,
        E0 = (109.09565, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
These numbers for the general BEP are from the abstraction reaction of C-H to C.
BEP values from "Quantifying the Impact of Parametric Uncertainty on Automatic Mechanism Generation for CO2 Hydrogenation on Ni(111)", Kreitz et al., JACS Au, 2021, 1, 10, 1656-1673 DOI:10.1021/jacsau.1c00276
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
Divided by 3 because of reaction path degeneracy for CH3 (3 equivalent H atoms)
    """
)

entry(
    index = 11,
    label = "O;*-CH2-H",
    kinetics = SurfaceArrheniusBEP(
        A = (1.393e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.8515464,
        E0 = (137.35548, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
These numbers for the BEP are from the abstraction reaction of C-H to O.
BEP values from "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt", Sutton et al., The Journal of Physical Chemistry C, 2013, 117, 4691-4706, DOI:10.1021/jp312593u
From Table 7 includes beta and alpha position. Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
Divided by 3 because of reaction path degeneracy for CH3 (3 equivalent H atoms)
    """
)

entry(
    index = 12,
    label = "O;*N-H",
    kinetics = SurfaceArrheniusBEP(
        A = (2.48e21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.30432907,
        E0 = (97.18883, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

entry(
    index = 13,
    label = "N;*OH",
    kinetics = SurfaceArrheniusBEP(
        A = (2.48e21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.6889324,
        E0 = (93.761185, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

