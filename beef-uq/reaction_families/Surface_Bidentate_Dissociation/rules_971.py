#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Bidentate_Dissociation/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Combined",
    kinetics = SurfaceArrheniusBEP(
        A = (1.187E12, '1/s'),
        n = 0.0, 
        alpha = 0.76033574,
        E0 = (146.90288, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
A factors are averages of training reactions 1-4 and the reverse direction of training reactions 5-7, 
and alpha and E0 are BEP parameters from training reactions 1-4 and the reverse of training reactions 5-7.

Details on the computational method to derive the rate constants for the BEP relation are provided in "Automatic mechanism generation involving 
kinetics of surface reactions with bidentate adsorbates" by B. Kreitz, K. Blöndal, K. Badger, R. H. West and C. F. Goldsmith, Digital Discovery, 2024, 3, 173
doi:10.1039/d3dd00184a
"""
)

entry(
    index = 2,
    label = "C-N",
    kinetics = SurfaceArrheniusBEP(
        A = (1e13, '1/s'),
        n = 0,
        alpha = 0.9680954,
        E0 = (184.82057, 'kJ/mol'),
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
    label = "N-C",
    kinetics = SurfaceArrheniusBEP(
        A = (1e13, '1/s'),
        n = 0,
        alpha = 0.72050935,
        E0 = (113.96634, 'kJ/mol'),
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
    label = "N-R",
    kinetics = SurfaceArrheniusBEP(
        A = (1e13, '1/s'),
        n = 0,
        alpha = 0.7643573,
        E0 = (130.74536, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)
entry(
    index = 5,
    label = "R-N",
    kinetics = SurfaceArrheniusBEP(
        A = (1e13, '1/s'),
        n = 0,
        alpha = 0.7542157,
        E0 = (132.91132, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"""
)

