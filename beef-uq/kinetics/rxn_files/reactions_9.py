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
        Ea = (79.6943750396371, 'kJ/mol'),
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
        A=0.06,
        n =0,
        Ea=(0, 'kJ/mol'),
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
        A=(5.00e21, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (94.73269512504339, 'kJ/mol'),
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
        A=(1.84e14, '1/s'),
        n = 0,
        Ea = (180.46968507021666, 'kJ/mol'),
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
        A=(4.03e13, '1/s'),
        n = 0,
        Ea = (209.00703040510416, 'kJ/mol'),
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
        A=(6.10e30, 'cm^4/(mol^2*s)'),
        n = 0,
        Ea = (74.55399636924267, 'kJ/mol'),
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
        A=(4.02e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (104.35308690369129, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 10, #Vlachos Ethane
    label = "XCHXCH <=> XCH + XCH",
    kinetics = SurfaceArrhenius(
        A=(8.5e12, '1/s'),
        n = 0,
        Ea = (90.817856, 'kJ/mol'),
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
        A=(4.73e30, 'cm^4/(mol^2*s)'),
        n = 0,
        Ea = (80.3646407648921, 'kJ/mol'),
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
        A=(2.03e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (141.0446603819728, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 13, #Vlachos Ethane
    label = "XCHXC <=> XCH + XC",
    kinetics = SurfaceArrhenius(
        A=(1.4e12, '1/s'),
        n = 0,
        Ea = (89.91817, 'kJ/mol'),
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
        Ea = (18.47074512451887, 'kJ/mol'),
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
        Ea = (62.41374570280314, 'kJ/mol'),
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
        Ea = (79.84794665932655, 'kJ/mol'),
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
        Ea = (26.824853596687316, 'kJ/mol'),
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
        Ea = (61.51332, 'kJ/mol'),
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
        Ea = (32.432156, 'kJ/mol'),
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
        Ea = (94.75926409780979, 'kJ/mol'),
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
        Ea = (37.77908544272184, 'kJ/mol'),
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
        Ea = (128.75728387624025, 'kJ/mol'),
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
        Ea = (90.12205272108316, 'kJ/mol'),
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
        Ea = (142.5220401608944, 'kJ/mol'),
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
        Ea = (214.3924316057563, 'kJ/mol'),
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
        Ea = (173.1225304427743, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value"""
)

entry(
    index = 27, #Vlachos Ethane
    label = "XCXC <=> XC + XC",
    kinetics = SurfaceArrhenius(
        A=(4.22E12, '1/s'),
        n = 0.0,
        Ea = (104.91749, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""DFT value from Katrin Blondal"""
)

entry(
    index = 28,
    label = "XCXCH2 + Pt <=> XCHXC + XH",
    kinetics = SurfaceArrhenius(
        A=(1.51e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (137.40366642922163, 'kJ/mol'),
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
        A=(1.78e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (63.93434612452984, 'kJ/mol'),
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
        A=(6.64E+28, 'cm^4/(mol^2*s)'),
        n = 0,
        Ea = (118.16639521718025, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""my value, it is endothermic, but kept in this direction, since we are going to switch it later afterwards due to the coverage dependence of CCH3"""
)

#entry(
#     index = 31,
#    label = "CHCHX + Pt <=> XCHXCH",
#    kinetics = SurfaceArrhenius(
#        A=(5.0E21, 'cm^2/(mol*s)'),
#        n = 0.0,
#        Ea=(5.0, 'kJ/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""Barrierless according to DFT calculations by Katrin Blondal"""
#)

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

#entry(
#    index = 36,
#    label = "NNO + Pt <=> NNOX",
#    kinetics = StickingCoefficient(
#        A = .1,
#        n = 0,
#        Ea = (0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Surface_Adsorption_Single""",
#    longDesc = u"""
#""",
#    metal = "Pt",
#)

entry(
    index = 37,
    label = "NH3 + Pt <=> NH3X",
    kinetics = StickingCoefficient(
        A = .8,
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
        Ea = (232.83255, 'kJ/mol'),
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
        A = (5.21E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (98.863675378263, 'kJ/mol'),
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
        Ea = (40.19987817108631, 'kJ/mol'),
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
        Ea = (86.33351036906242, 'kJ/mol'),
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
        Ea = (148.9709529131651, 'kJ/mol'),
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
        Ea = (119.72536665201187, 'kJ/mol'),
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
        Ea = (87.6701742336154, 'kJ/mol'),
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
        Ea = (174.81114070862532, 'kJ/mol'),
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
        Ea = (172.0887015387416, 'kJ/mol'),
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
        Ea = (326.0456067919731, 'kJ/mol'),
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
        Ea = (266.14257645606995, 'kJ/mol'),
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

entry(
    index = 51,
    label = "XNOH + Pt <=> XNO + XH",
    kinetics = SurfaceArrhenius(
        A = (2.75E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (95.42196542024612, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 52,
    label = "HXNO + Pt <=> XNO + XH",
    kinetics = SurfaceArrhenius(
        A = (1.13E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (24.2868178114295, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 53,
    label = "HXNO + Pt <=> XO + XNH",
    kinetics = SurfaceArrhenius(
        A = (1.54E20, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (101.2265306264162, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 54,
#    label = "NNOX + Pt <=> XNO + XN",
#    kinetics = SurfaceArrhenius(
#        A = (4.18e17, 'm^2/(mol*s)'),  
#        n = 0,
#        Ea=(97, 'kJ/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
#    longDesc = u"""
#""",
#    metal = "Pt",
#    facet = "111",
#)

entry(
    index = 55,
    label = "XCH + Pt <=> XC + XH",
    kinetics = SurfaceArrhenius(
        A = (1.157E22, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (140.78998078405857, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 56,
    label = "OXCCH3 + Pt + Pt <=> OXCXCH2 + XH",
    kinetics = SurfaceArrhenius(
        A = (1.92E30, 'cm^4/(mol^2*s)'),
        n = 0.0,
        Ea = (106.58565029501915, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 57,
    label = "OXCXCH2 + Pt <=> OXCXCH + XH",
    kinetics = SurfaceArrhenius(
        A = (4.87E21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (93.85956788808107, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 58,
    label = "OXCCH3 + Pt <=> XCCH3 + XO",
    kinetics = SurfaceArrhenius(
        A = (1.53e20, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (219.03658132255077, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 59,
    label = "OXCCH3 + Pt <=> XCO + XCH3",
    kinetics = SurfaceArrhenius(
        A = (8.84e20, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (130.81312759965658, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 60,
    label = "OXCXCH <=> XCO + XCH",
    kinetics = SurfaceArrhenius(
        A = (1.11e14, '1/s'),
        n = 0.0,
        Ea = (76.24758533388376, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 61,
    label = "OXCXCH2 <=> XCO + XCH2",
    kinetics = SurfaceArrhenius(
        A = (6.74e13, '1/s'),
        n = 0.0,
        Ea = (88.51623759418726, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 62,
    label = "OXCXCH2 + Pt <=> XO + XCXCH2",
    kinetics = SurfaceArrhenius(
        A = (1.71e21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (234.82749823480844, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 63,
    label = "OXCXCH + Pt <=> XCXCO + XH",
    kinetics = SurfaceArrhenius(
        A = (8.26e22, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (124.03677654266357, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 64,
    label = "XCXCO <=> XCO + XC",
    kinetics = SurfaceArrhenius(
        A = (1.82e13, '1/s'),
        n = 0.0,
        Ea = (57.86356280744076, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 65,
    label = "XCXCH2 <=> XC + XCH2",
    kinetics = SurfaceArrhenius(
        A = (2.59e13, '1/s'),
        n = 0.0,
        Ea = (225.56301940232515, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 66,
    label = "XCHXC + Pt <=> XCXC + XH",
    kinetics = SurfaceArrhenius(
        A = (1.66e22, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (127.72898492217064, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 67,
    label = "XNO2 + XCXCH2 <=> XNO + OXCXCH2",
    kinetics = SurfaceArrhenius(
        A = (9.04e19, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (48.84199386835098, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 68,
    label = "XNOH + XC <=> XNO + XCH",
    kinetics = SurfaceArrhenius(
        A = (6.01e20, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (82.75191313028336, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 69,
#    label = "XOXO <=> XO + XO",
#    kinetics = SurfaceArrhenius(
#        A = (4.21e+12, '1/s'),
#        n = 0.0,
#        Ea = (59, 'kJ/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
#    longDesc = u"""
#""",
#    metal = "Pt",
#    facet = "111",
#)

#entry(
#    index = 70,
#    label = "O2 + Pt + Pt <=> XOXO",
#    kinetics = StickingCoefficient(
#        A = 0.22,
#        n = 0,
#        Ea=(0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""  """
#)

entry(
    index = 71,
    label = "XNO2 + XCCH3 <=> XNO + OXCCH3",
    kinetics = SurfaceArrhenius(
        A = (5.82e18, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (81.91268168389797, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 72,
    label = "XNOH + XCH2XCH <=> XNO + XCH2XCH2",
    kinetics = SurfaceArrhenius(
        A = (5.71e21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (96.02444644272327, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Unpublished NOx containing exhaust gas conversion project""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 73,
    label = "XNO + XN <=> NNOX + Pt",
    kinetics = SurfaceArrhenius(
        A = (4.03e21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (119.344376, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""https://doi.org/10.1021/cs500668k""",
    longDesc = u""" decreases to 7 kJ/mol at 0.5 ML NO""
""",
    metal = "Pt",
    facet = "111",
)
