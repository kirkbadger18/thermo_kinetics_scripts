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
        alpha = 0.8158177,
        E0 = (187.86899, 'kJ/mol'),
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
        alpha = 0.93325377,
        E0 = (54.666203, 'kJ/mol'),
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
        alpha = 0.73863673,
        E0 = (156.76097, 'kJ/mol'),
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
        alpha = 0.51603854,
        E0 = (88.47334, 'kJ/mol'),
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
        alpha = 0.19883236,
        E0 = (59.4909, 'kJ/mol'),
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
        alpha = 0.63486063,
        E0 = (108.13074, 'kJ/mol'),
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
        alpha = 0.69802094,
        E0 = (126.961334, 'kJ/mol'),
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
        alpha = 0.55882037,
        E0 = (77.14443, 'kJ/mol'),
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
        alpha = 0.58447045,
        E0 = (87.837296, 'kJ/mol'),
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
        alpha = 0.48806322,
        E0 = (64.3964, 'kJ/mol'),
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
        alpha = 0.48997504,
        E0 = (61.08539, 'kJ/mol'),
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
        alpha = 0.94010323,
        E0 = (129.73799, 'kJ/mol'),
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
        alpha = 0.93138814,
        E0 = (140.72128, 'kJ/mol'),
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
        alpha = 0.38042942,
        E0 = (121.54125, 'kJ/mol'),
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
        alpha = 1.116779,
        E0 = (190.39384, 'kJ/mol'),
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
        alpha = 0.78748554,
        E0 = (134.0089, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

