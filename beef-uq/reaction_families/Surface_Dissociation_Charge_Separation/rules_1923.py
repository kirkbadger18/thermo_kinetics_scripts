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
        alpha = 0.8765439,
        E0 = (134.98999, 'kJ/mol'),
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
        alpha = 1.0208056,
        E0 = (153.814, 'kJ/mol'),
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
        alpha = 1.079268,
        E0 = (207.14923, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

