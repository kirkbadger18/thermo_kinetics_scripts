#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_NO2/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Combined;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (1.02e22, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.7203843,
        E0 = (137.48859, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

entry(
    index = 2,
    label = "C;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (7.49E21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.977031,
        E0 = (153.84396, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)


entry(
    index = 3,
    label = "O;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (3.18e21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 1.093436,
        E0 = (206.81857, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

entry(
    index = 4,
    label = "H;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (2.72e22, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.29988852,
        E0 = (124.79561, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

