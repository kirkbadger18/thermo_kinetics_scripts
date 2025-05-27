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
        alpha = 0.71893895,
        E0 = (111.30541, 'kJ/mol'),
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
        alpha = 1.0014572,
        E0 = (141.99509, 'kJ/mol'),
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
        alpha = 1.095517,
        E0 = (207.33102, 'kJ/mol'),
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
        alpha = 0.19359106,
        E0 = (106.556335, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

