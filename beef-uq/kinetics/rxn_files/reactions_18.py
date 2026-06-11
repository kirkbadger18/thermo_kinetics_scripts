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
        Ea = (98.86818335354329, 'kJ/mol'),
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
        Ea = (92.33881286531687, 'kJ/mol'),
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
        Ea = (177.7333324700594, 'kJ/mol'),
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
        Ea = (220.25196333229542, 'kJ/mol'),
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
        Ea = (83.9334776327014, 'kJ/mol'),
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
        Ea = (103.81630425155163, 'kJ/mol'),
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
        Ea = (96.938736, 'kJ/mol'),
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
        Ea = (78.94729794561863, 'kJ/mol'),
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
        Ea = (148.49345722794533, 'kJ/mol'),
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
        Ea = (80.81954, 'kJ/mol'),
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
        Ea = (29.586188868284225, 'kJ/mol'),
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
        Ea = (75.8984095543623, 'kJ/mol'),
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
        Ea = (87.06171605795622, 'kJ/mol'),
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
        Ea = (18.868634161949156, 'kJ/mol'),
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
        Ea = (68.049225, 'kJ/mol'),
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
        Ea = (34.672596, 'kJ/mol'),
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
        Ea = (87.69700213640928, 'kJ/mol'),
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
        Ea = (37.053660400509834, 'kJ/mol'),
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
        Ea = (139.78011114388704, 'kJ/mol'),
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
        Ea = (99.65170711219311, 'kJ/mol'),
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
        Ea = (140.83805249124765, 'kJ/mol'),
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
        Ea = (224.93436121582985, 'kJ/mol'),
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
        Ea = (173.23191590338945, 'kJ/mol'),
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
        Ea = (95.28409, 'kJ/mol'),
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
        Ea = (145.71786389499903, 'kJ/mol'),
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
        Ea = (66.67457661777735, 'kJ/mol'),
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
        Ea = (128.1999636515975, 'kJ/mol'),
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
        Ea = (219.88585, 'kJ/mol'),
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
        Ea = (101.00690864771605, 'kJ/mol'),
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
        Ea = (33.06941009312868, 'kJ/mol'),
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
        Ea = (79.45170387625694, 'kJ/mol'),
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
        Ea = (130.61945533007383, 'kJ/mol'),
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
        Ea = (114.40486290305853, 'kJ/mol'),
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
        Ea = (81.8323521912098, 'kJ/mol'),
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
        Ea = (175.46993113309145, 'kJ/mol'),
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
        Ea = (169.46999162435532, 'kJ/mol'),
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
        Ea = (91.15462509542704, 'kJ/mol'),
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
        Ea = (236.09616301208735, 'kJ/mol'),
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
        Ea = (99.1066977456212, 'kJ/mol'),
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
        Ea = (26.583395659923553, 'kJ/mol'),
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
        Ea = (102.80204366147518, 'kJ/mol'),
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
        Ea = (145.58840510249138, 'kJ/mol'),
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
        Ea = (113.7103068754077, 'kJ/mol'),
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
        Ea = (90.67645259201527, 'kJ/mol'),
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
        Ea = (220.18728798627853, 'kJ/mol'),
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
        Ea = (145.35274109989405, 'kJ/mol'),
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
        Ea = (85.58405993133783, 'kJ/mol'),
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
        Ea = (100.89329995959997, 'kJ/mol'),
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
        Ea = (234.33105490356684, 'kJ/mol'),
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
        Ea = (127.17135114967823, 'kJ/mol'),
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
        Ea = (73.41668612509966, 'kJ/mol'),
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
        Ea = (241.9875813499093, 'kJ/mol'),
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
        Ea = (126.9752586260438, 'kJ/mol'),
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
        Ea = (61.8829435557127, 'kJ/mol'),
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
        Ea = (94.48217833042145, 'kJ/mol'),
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
        Ea = (102.9625385850668, 'kJ/mol'),
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
        Ea = (110.58875043690205, 'kJ/mol'),
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
        Ea = (125.272736, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""https://doi.org/10.1021/cs500668k""",
    longDesc = u""" decreases to 7 kJ/mol at 0.5 ML NO""
""",
    metal = "Pt",
    facet = "111",
)
