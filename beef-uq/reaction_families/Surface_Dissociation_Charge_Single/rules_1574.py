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
        alpha = 0.74391264,
        E0 = (126.14796, 'kJ/mol'),
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
        alpha = 1.005843,
        E0 = (144.26534, 'kJ/mol'),
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
        alpha = 1.0154783,
        E0 = (193.30185, 'kJ/mol'),
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
        alpha = 0.24288443,
        E0 = (125.39195, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

