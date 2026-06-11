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
        alpha = 0.8493366,
        E0 = (194.465, 'kJ/mol'),
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
        A = (2.29e22, 'cm^2/(mol*s)'),
        n = 0.0,
        alpha = 0.81778157,
        E0 = (78.467865, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
This BEP is created from a mixture of data in literature taken from the following papers: 

Kreitz et al.
https://doi.org/10.1021/acscatal.2c03378

Deng et al.
https://pubs.rsc.org/en/content/articlelanding/2014/ra/c3ra46544f

and the current manuscript in progress by Badger et al. looking at the effects
of NO on the light out curves for hydrocarbons.
"""
)

entry(
    index = 3,
    label = "C-O;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (4.18e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.6799833,
        E0 = (128.36833, 'kJ/mol'),
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
        alpha = 0.6091492,
        E0 = (79.633194, 'kJ/mol'),
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
        alpha = 0.22594613,
        E0 = (71.197266, 'kJ/mol'),
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
        alpha = 0.54434586,
        E0 = (112.278564, 'kJ/mol'),
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
        alpha = 0.6221619,
        E0 = (137.58145, 'kJ/mol'),
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
    label = "C-N;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (6.72E21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.9406128,
        E0 = (176.82788, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
This BEP is created from a mixture of data in literature taken from the following papers: 

Gomez-Díaz and Lopez
https://pubs.acs.org/doi/10.1021/jp1093349

Deng et al.
https://pubs.rsc.org/en/content/articlelanding/2014/ra/c3ra46544f

and the current manuscript in progress by Badger et al. looking at the effects
of NO on the light out curves for hydrocarbons.
"""
)

entry(
    index = 9,
    label = "N-C;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (6.72E21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.81309456,
        E0 = (161.16835, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
This BEP is created from a mixture of data in literature taken from the following papers: 

Gomez-Díaz and Lopez
https://pubs.acs.org/doi/10.1021/jp1093349

Deng et al.
https://pubs.rsc.org/en/content/articlelanding/2014/ra/c3ra46544f

and the current manuscript in progress by Badger et al. looking at the effects
of NO on the light out curves for hydrocarbons.
"""
)

entry(
    index = 10,
    label = "N-H;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (1.63e22, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.43127677,
        E0 = (104.46895, 'kJ/mol'),
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
    index = 11,
    label = "N-O;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (2.08e21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 1.0726784,
        E0 = (171.98431, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
This BEP is created from a mixture of data in literature taken from the following papers: 

Ma and Schneider
https://doi.org/10.1021/acscatal.8b04251

Farberow et al.
https://doi.org/10.1021/cs500668k

and the current manuscript in progress by Badger et al. looking at the effects
of NO on the light out curves for hydrocarbons.
"""
)

entry(
    index = 12,
    label = "N;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (9.88e21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.5363335,
        E0 = (138.65062, 'kJ/mol'),
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

