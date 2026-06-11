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
        A = (4.55E13, '1/s'),
        n = 0.0, 
        alpha = 1.2652404,
        E0 = (162.68124, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
This BEP is created from a mixture of data in literature taken from: 

Gomez-Díaz and Lopez
https://pubs.acs.org/doi/10.1021/jp1093349

and the current manuscript in progress by Badger et al. looking at the effects
of NO on the light out curves for hydrocarbons.
"""
)

entry(
    index = 2,
    label = "C-N",
    kinetics = SurfaceArrheniusBEP(
        A = (1e13, '1/s'),
        n = 0,
        alpha = 0.9513388,
        E0 = (196.79008, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
This BEP is created from data in literature taken from: 
Gomez-Díaz and Lopez
https://pubs.acs.org/doi/10.1021/jp1093349
"""
)
entry(
    index = 3,
    label = "N-C",
    kinetics = SurfaceArrheniusBEP(
        A = (1e13, '1/s'),
        n = 0,
        alpha = 1.0129241,
        E0 = (189.01752, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
This BEP is created from data in literature taken from: 
Gomez-Díaz and Lopez
https://pubs.acs.org/doi/10.1021/jp1093349
"""
)
entry(
    index = 4,
    label = "N-R",
    kinetics = SurfaceArrheniusBEP(
        A = (4.55E13, '1/s'),
        n = 0.0, 
        alpha = 1.181164,
        E0 = (152.32558, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
This BEP is created from a mixture of data in literature taken from: 

Gomez-Díaz and Lopez
https://pubs.acs.org/doi/10.1021/jp1093349

and the current manuscript in progress by Badger et al. looking at the effects
of NO on the light out curves for hydrocarbons.
"""
)
entry(
    index = 5,
    label = "R-N",
    kinetics = SurfaceArrheniusBEP(
        A = (4.55E13, '1/s'),
        n = 0.0, 
        alpha = 1.2135077,
        E0 = (177.84743, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    
    longDesc = u"""
This BEP is created from a mixture of data in literature taken from: 

Gomez-Díaz and Lopez
https://pubs.acs.org/doi/10.1021/jp1093349

and the current manuscript in progress by Badger et al. looking at the effects
of NO on the light out curves for hydrocarbons.
"""
)
