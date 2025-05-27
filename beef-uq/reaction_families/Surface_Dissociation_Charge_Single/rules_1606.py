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
        alpha = 0.8790375,
        E0 = (133.41159, 'kJ/mol'),
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
        alpha = 0.95198333,
        E0 = (140.31364, 'kJ/mol'),
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
        alpha = 0.92908484,
        E0 = (180.79207, 'kJ/mol'),
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
        alpha = 0.25316164,
        E0 = (115.79823, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

