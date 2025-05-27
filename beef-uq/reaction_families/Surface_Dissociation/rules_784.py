#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Combined;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.7937837,
        E0 = (186.71317, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
E0 and alpha are taken from:
"Universal Brønsted-Evans-Polanyi Relations for C–C, C–O, C–N, N–O, N–N, and O–O Dissociation Reactions" by Wang, ..., Norskov/ Catal. Lett (2011) 141:370-373, DOI: 10.1007/s10562-010-0477-y
(actual value for E0 was 1.92 eV.)
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
    """
)

entry(
    index = 2,
    label = "C-H_Bidentate;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (1.36e18, 'm^2/(mol*s)'),
        n = 0.0,
        alpha = 0.9271561,
        E0 = (66.08499, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
A and n factors are from the average rate constant of training reactions 60-63, and alpha and E0 are BEP
parameters from training reactions 60-63. The A factor has been divided by 2 here to account for the degeneracies of the training reactions.
    """
)

entry(
    index = 3,
    label = "C-O;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.7222784,
        E0 = (132.25635, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
E0 and alpha are taken from Table 5 for all metals from Sutton and Vlachos, "Ethanol Activation on closed-packed surfaces", Industrial & Engineering Chemistry Research, 2015, 54, 4213-4225, DOI: 10.1021/ie5043374.
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
"""
)

entry(
    index = 4,
    label = "C-H;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.5083885,
        E0 = (64.84097, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
E0 and alpha are taken from Table 5 for all metals from Sutton and Vlachos, "Ethanol Activation on closed-packed surfaces", Industrial & Engineering Chemistry Research, 2015, 54, 4213-4225, DOI: 10.1021/ie5043374.
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
"""
)


entry(
    index = 5,
    label = "O-H;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.24308047,
        E0 = (88.13308, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
E0 and alpha are taken from Table 5 for all metals from Sutton and Vlachos, "Ethanol Activation on closed-packed surfaces", Industrial & Engineering Chemistry Research, 2015, 54, 4213-4225, DOI: 10.1021/ie5043374.
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
    """
)

entry(
    index = 6,
    label = "C-OH;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.5963411,
        E0 = (107.901535, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
E0 and alpha are taken from Table 5 for all metals from Sutton and Vlachos, "Ethanol Activation on closed-packed surfaces", Industrial & Engineering Chemistry Research, 2015, 54, 4213-4225, DOI: 10.1021/ie5043374.
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
    """
)

entry(
    index = 7,
    label = "C-C;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.6408317,
        E0 = (134.28677, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
E0 and alpha are taken from Table 5 for all metals from Sutton and Vlachos, "Ethanol Activation on closed-packed surfaces", Industrial & Engineering Chemistry Research, 2015, 54, 4213-4225, DOI: 10.1021/ie5043374.
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
    """
)

entry(
    index = 8,
    label = "CH2;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (2.09e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.49586737,
        E0 = (67.62775, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
E0 and alpha are taken from Table 5 for all metals from Sutton and Vlachos, "Ethanol Activation on closed-packed surfaces", Industrial & Engineering Chemistry Research, 2015, 54, 4213-4225, DOI: 10.1021/ie5043374.
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
A divided by 2 because of reaction path degeneracy for CH2
"""
)

entry(
    index = 9,
    label = "CH3;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (1.39e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.47462177,
        E0 = (66.95036, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
E0 and alpha are taken from Table 5 for all metals from Sutton and Vlachos, "Ethanol Activation on closed-packed surfaces", Industrial & Engineering Chemistry Research, 2015, 54, 4213-4225, DOI: 10.1021/ie5043374.
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
A divided by 3 because of reaction path degeneracy for CH3
"""
)

entry(
    index = 10,
    label = "CH2R;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (2.09e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.5130427,
        E0 = (82.06178, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
E0 and alpha are taken from Table 5 for all metals from Sutton and Vlachos, "Ethanol Activation on closed-packed surfaces", Industrial & Engineering Chemistry Research, 2015, 54, 4213-4225, DOI: 10.1021/ie5043374.
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
A divided by 2 because of reaction path degeneracy for X-CH2-R (Abstraction of the alpha H atom)
"""
)

entry(
    index = 11,
    label = "CHR;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.5814737,
        E0 = (64.4371, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
E0 and alpha are taken from Table 5 for all metals from Sutton and Vlachos, "Ethanol Activation on closed-packed surfaces", Industrial & Engineering Chemistry Research, 2015, 54, 4213-4225, DOI: 10.1021/ie5043374.
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
A divided by 2 because of reaction path degeneracy for X-CH2-R (Abstraction of the alpha H atom)
"""
)

entry(
    index = 12,
    label = "C-N;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (4.94E21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.8880525,
        E0 = (145.30112, 'kJ/mol'),
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
    label = "N-C;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (4.94E21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.9342681,
        E0 = (135.3226, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

entry(
    index = 14,
    label = "N-H;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (2.18e22, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.30257475,
        E0 = (106.36441, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

entry(
    index = 15,
    label = "N-O;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (2.08e21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 1.2494004,
        E0 = (168.30528, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

entry(
    index = 16,
    label = "N;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (1.02e22, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.80910456,
        E0 = (118.373566, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

