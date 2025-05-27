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
        Ea = (91.86657808870078, 'kJ/mol'),
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
        Ea = (70.25749978423119, 'kJ/mol'),
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
        Ea = (152.50880095005036, 'kJ/mol'),
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
        Ea = (223.44559086114168, 'kJ/mol'),
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
        Ea = (58.42415650933981, 'kJ/mol'),
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
        Ea = (86.54827199608087, 'kJ/mol'),
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
        Ea = (96.13411769717932, 'kJ/mol'),
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
        Ea = (55.127414946556094, 'kJ/mol'),
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
        Ea = (152.14482815653085, 'kJ/mol'),
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
        Ea = (76.35432361394167, 'kJ/mol'),
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
        Ea = (34.040999502539634, 'kJ/mol'),
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
        Ea = (83.58599701672793, 'kJ/mol'),
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
        Ea = (82.34175186663866, 'kJ/mol'),
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
        Ea = (24.953385782837866, 'kJ/mol'),
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
        Ea = (101.68734784543514, 'kJ/mol'),
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
        Ea = (41.63010842382908, 'kJ/mol'),
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
        Ea = (133.9290287965536, 'kJ/mol'),
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
        Ea = (97.92058961033821, 'kJ/mol'),
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
        Ea = (150.20785828918218, 'kJ/mol'),
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
        Ea = (233.03117054343224, 'kJ/mol'),
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
        Ea = (185.08571704953908, 'kJ/mol'),
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
        Ea = (179.98064853996038, 'kJ/mol'),
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
        Ea = (34.07792130112648, 'kJ/mol'),
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
        Ea = (61.255449287593365, 'kJ/mol'),
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
        Ea = (111.87838746607304, 'kJ/mol'),
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
        Ea = (207.8567396402359, 'kJ/mol'),
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
        Ea = (51.77208962291479, 'kJ/mol'),
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
        Ea = (81.26289554685354, 'kJ/mol'),
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
        Ea = (139.3109842017293, 'kJ/mol'),
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
        Ea = (112.30392915010452, 'kJ/mol'),
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
        Ea = (82.2582225650549, 'kJ/mol'),
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
        Ea = (174.79048969596624, 'kJ/mol'),
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
        Ea = (167.67515911906958, 'kJ/mol'),
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
        Ea = (115.60952632129192, 'kJ/mol'),
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
        Ea = (256.62799341231585, 'kJ/mol'),
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

