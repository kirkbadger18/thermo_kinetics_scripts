#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Monodentate_to_Bidentate/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Monodentate;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (7.15e20, 'cm^2/(mol*s)'),
        n = 0.0,
        alpha = 0,
        E0 = (3, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
""",
)



