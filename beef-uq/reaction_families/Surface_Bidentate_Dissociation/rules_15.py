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
        alpha = 1.1329316,
        E0 = (181.69582, 'kJ/mol'),
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
        alpha = 0.9311234,
        E0 = (207.7342, 'kJ/mol'),
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
        alpha = 0.9717748,
        E0 = (208.93996, 'kJ/mol'),
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
        alpha = 1.1000148,
        E0 = (165.18, 'kJ/mol'),
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
        alpha = 1.1604099,
        E0 = (161.50908, 'kJ/mol'),
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
