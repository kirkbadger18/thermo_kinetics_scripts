#!/usr/bin/env python
# encoding: utf-8

name = "Pt111"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "CO + Pt <=> XCO",
    kinetics = StickingCoefficient(
        A = 8.0E-1,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
CO adsorption on Pt(111). From W. A. Brown, R. Kose, D. A. King, "Femtomole Adsorption Calorimetry on Single-Crystal Surfaces" Chem. Rev. 1998, 98, 797-831
"""
)
entry(
    index = 2,
    label = "XCO + XO <=> CO2X + Pt",
    kinetics = SurfaceArrhenius(
        A=(1.133e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (83.1264305651188, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 3,
    label = "O2 + Pt + Pt <=> XO + XO",
    kinetics = StickingCoefficient(
        A=0.064,
        n =0,
        Ea=(0.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""O2 adsorption on Pt(111). From W. A. Brown, R. Kose, D. A. King, "Femtomole Adsorption Calorimetry on Single-Crystal Surfaces" Chem. Rev. 1998, 98, 797-831"""
)

entry(
    index = 4,
    label = "C2H4 + Pt + Pt <=> XCH2XCH2",
    kinetics = StickingCoefficient(
        A=0.67,
        n =0,
        Ea=(0.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""O2 adsorption on Pt(111). From W. A. Brown, R. Kose, D. A. King, "Femtomole Adsorption Calorimetry on Single-Crystal Surfaces" Chem. Rev. 1998, 98, 797-831"""
)

entry(
    index = 5,
    label = "XCH2XCH2 + Pt <=> XCH2XCH + XH",
    kinetics = SurfaceArrhenius(
        A=(5.36e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (68.60002390295267, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 6,
    label = "XCH2XCH <=> XCH + XCH2",
    kinetics = SurfaceArrhenius(
        A=(2.94e13, '1/s'),
        n = 0,
        Ea = (145.6275210866332, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 7,
    label = "XCH2XCH2 <=> XCH2 + XCH2",
    kinetics = SurfaceArrhenius(
        A=(3.09e15, '1/s'),
        n = 0,
        Ea = (215.48180082440376, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 8,
    label = "XCHCH3 + Pt + Pt  <=>  XCH2XCH + XH",
    kinetics = SurfaceArrhenius(
        A=(2.32e30, 'cm^4/(mol^2*s)'),
        n = 0,
        Ea = (54.16614678502083, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 9,
    label = "XCH2XCH + Pt <=> XCHXCH + XH",
    kinetics = SurfaceArrhenius(
        A=(1.08e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (81.05901132255792, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 10,
    label = "XCHXCH <=> XCH + XCH",
    kinetics = SurfaceArrhenius(
        A=(8.5e12, '1/s'),
        n = 0,
        Ea = (93.01039992719889, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)


entry(
    index = 11,
    label = "XCH2CH3 + Pt + Pt <=> XCH2XCH2 + XH",
    kinetics = SurfaceArrhenius(
        A=(1.87e30, 'cm^4/(mol^2*s)'),
        n = 0,
        Ea = (55.76616818189621, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 12,
    label = "XCHXCH + Pt <=> XCHXC + XH",
    kinetics = SurfaceArrhenius(
        A=(2.033e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (149.85815795600413, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 13,
    label = "XCHXC <=> XCH + XC",
    kinetics = SurfaceArrhenius(
        A=(1.4e12, '1/s'),
        n = 0,
        Ea = (74.49553373783827, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 14,
    label = "XCO + XOH <=> XCOOH + Pt",
    kinetics = SurfaceArrhenius(
        A=(2.225e20, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (27.282149941325187, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 15,
    label = "H2OX + Pt <=> XOH + XH",
    kinetics = SurfaceArrhenius(
        A=(8.144e19, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (86.44413488507271, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 16,
    label = "XO + XH <=> XOH + Pt",
    kinetics = SurfaceArrhenius(
        A=(1.921e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (79.2866259893775, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 17,
    label = "XCOOH + XO <=> CO2X + XOH",
    kinetics = SurfaceArrhenius(
        A=(1.059e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (27.105034565031527, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 18,
    label = "CH4 + Pt + Pt <=> XCH3 + XH",
    kinetics = StickingCoefficient(
        A = 6.04,
        n = 0,
        Ea=(58, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 19,
    label = "C2H6 + Pt + Pt <=> XCH2CH3 + XH",
    kinetics = StickingCoefficient(
        A = 2.052,
        n = 0,
        Ea=(42.7, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 20,
    label = "XCH3 + Pt <=> XCH2 + XH",
    kinetics = SurfaceArrhenius(
        A=(1.337e20, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (96.15565646559, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 21,
    label = "XCH2 + Pt <=> XCH + XH",
    kinetics = SurfaceArrhenius(
        A=(5.510e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (40.51237661421299, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)


entry(
    index = 22,
    label = "XCH + XO <=> HXCO + Pt",
    kinetics = SurfaceArrhenius(
        A=(9.748e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (127.00281136721372, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 23,
    label = "XCO + XH <=> HXCO + Pt",
    kinetics = SurfaceArrhenius(
        A=(8.714e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (95.2994358459115, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 24,
    label = "XCO + XH <=> XCOH + Pt",
    kinetics = SurfaceArrhenius(
        A=(8.712e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (148.39914209634065, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 25,
    label = "XCOH + Pt <=> XC + XOH",
    kinetics = SurfaceArrhenius(
        A=(3.845e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (222.47555339723826, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 26,
    label = "XCH2CH3 + Pt <=> XCH2 + XCH3",
    kinetics = SurfaceArrhenius(
        A=(3.449e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (180.5632294613123, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 27,
    label = "XCXC <=> XC + XC",
    kinetics = SurfaceArrhenius(
        A=(4.22E12, '1/s'),
        n = 0.0,
        Ea = (128.73059310019016, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 28,
    label = "XCHXC + XH <=> XCXCH2 + Pt",
    kinetics = SurfaceArrhenius(
        A=(5.19e19, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (32.00747660547495, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value, implemented in reverse since it is endothermic according to RMG"""
)

entry(
    index = 29,
    label = "XCH2XCH + Pt <=> XCXCH2 + XH",
    kinetics = SurfaceArrhenius(
        A=(9.69e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (53.947065971791744, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 30,
    label = "XCCH3 + Pt + Pt <=> XCXCH2 + XH",
    kinetics = SurfaceArrhenius(
        A=(1.07E+30, 'cm^4/(mol^2*s)'),
        n = 0,
        Ea = (103.28662183880806, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value, it is endothermic, but kept in this direction, since we are going to switch it later afterwards due to the coverage dependence of CCH3"""
)

entry(
     index = 31,
    label = "CHCHX + Pt <=> XCHXCH",
    kinetics = SurfaceArrhenius(
        A=(5.0E21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea=(5.0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Barrierless according to DFT calculations by Katrin Blondal"""
)

#entry(
#    index = 32,
#    label = "C2H4X + Pt <=> XCH2XCH2",
#    kinetics = SurfaceArrhenius(
#        A=(1.78E21, 'cm^2/(mol*s)'),
#        n = 0.0,
#        Ea=(12, 'kJ/mol'), #12 #51
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""DFT value from Katrin Blondal"""
#)

entry(
    index = 33,
    label = "C2H2 + Pt + Pt <=> XCHXCH",
    kinetics = StickingCoefficient(
        A=0.0083,
        n =0,
        Ea=(0.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Experimental value with single-crystal adsorption calorimetry (SCAC) for #initial sticking probability:
    "Energetics and kinetics of the interaction of acetylene and ethylene with Pd{100} and #Ni{100}"
    Vattuone et al
    Surface Science, 2000, 447, 1-14""",
)

entry(
    index = 34,
    label = "NO + Pt <=> XNO",
    kinetics = StickingCoefficient(
        A = 0.88,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
""",
    metal = "Pt",
)

entry(
    index = 35,
    label = "NO2 + Pt <=> XNO2",
    kinetics = StickingCoefficient(
        A = .97,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
""",
    metal = "Pt",
)

entry(
    index = 36,
    label = "NNO + Pt <=> XNNO",
    kinetics = StickingCoefficient(
        A = .1,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
""",
    metal = "Pt",
)

entry(
    index = 37,
    label = "NH3 + Pt <=> NH3X",
    kinetics = StickingCoefficient(
        A = .73,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
""",
    metal = "Pt",
)

entry(
    index = 38,
    label = "N2 + Pt + Pt <=> XN + XN",
    kinetics = StickingCoefficient(
        A = 0.0001,
        n = 0,
        Ea = (176, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
""",
    metal = "Pt",
)

entry(
    index = 39,
    label = "XNO + Pt <=> XN + XO",
    kinetics = SurfaceArrhenius(
        A = (2.99E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (202.80040135979652, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 40,
    label = "XNO2 + Pt <=> XNO + XO",
    kinetics = SurfaceArrhenius(
        A = (5.90E20, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (62.51142347604036, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 41,
    label = "XNOH + Pt <=> XN + XOH",
    kinetics = SurfaceArrhenius(
        A = (4.56E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (79.3305632174015, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 42,
#    label = "XOXNO  <=> XNO2 + Pt",
#    kinetics = SurfaceArrhenius(
#        A = (6.63E11, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (6, 'kJ/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Nitrogen/51""",
#    longDesc = u"""
#""",
#    metal = "Pt",
#    facet = "111",
#)

entry(
    index = 43,
    label = "XNH2 + Pt <=> XNH + XH",
    kinetics = SurfaceArrhenius(
        A = (5.44E22, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (146.64573334157467, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 44,
    label = "XNH + Pt <=> XN + XH",
    kinetics = SurfaceArrhenius(
        A = (2.04E22, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (114.77819626778364, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 45,
    label = "XNHNH2 + Pt <=> XNNH2 + XH",
    kinetics = SurfaceArrhenius(
        A = (3.00E22, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (90.64478825032711, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 46,
    label = "XNHCH3 + Pt <=> XNH + XCH3",
    kinetics = SurfaceArrhenius(
        A = (1.70E22, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (179.39196144789457, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 47,
    label = "XNCH3 + Pt <=> XN + XCH3",
    kinetics = SurfaceArrhenius(
        A = (1.44E22, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (169.8191238641739, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 48,
    label = "XNCN + Pt <=> XN + XCN",
    kinetics = SurfaceArrhenius(
        A = (3.38E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (210.7550776451826, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 49,
    label = "XCN + Pt <=> XC + XN",
    kinetics = SurfaceArrhenius(
        A = (1.79E20, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (259.6449604332447, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 50,
#    label = "XOXNO <=> XNO + XO",
#    kinetics = SurfaceArrhenius(
#        A = (3.30E12, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (62, 'kJ/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
#    longDesc = u"""
#""",
#    metal = "Pt",
#    facet = "111",
#)

