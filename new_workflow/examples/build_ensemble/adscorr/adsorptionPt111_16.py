#!/usr/bin/env python
# encoding: utf-8
name = " "
shortDesc = u"""
"""
longDesc = u"""
 
"""
entry(
    index = 1,
    label = "RX",
    group=
"""
1 R  ux
2 * X ux
""",
    thermo=None,
    shortDesc=u"""Anything adsorbed anyhow.""",
    longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 2,
    label = "RXbidentate",
    group=
"""
1 * X  u0 p0 c0 {3,[S,D,T]}
2 X  u0 p0 c0 {4,[S,D,T]}
3 R!H u0 {1,[S,D,T]} {4,[S,D,T]}
4 R!H u0 {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.521, 7.713, 10.235, 11.751, 13.233, 13.812, 14.188], 'J/(mol*K)'),
        H298=(-201.456, 'kJ/mol'),
        S298=(-186.501, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 3,
    label = "CXCX",
    group=
"""
1 * X u0 {3,[S,D,T]}
2 X u0 {4,[S,D,T]}
3 C  u0 {1,[S,D,T]} {4,[S,D,T]}
4 C  u0 {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.57, 4.379, 7.518, 9.51, 11.661, 12.666, 13.548], 'J/(mol*K)'),
        H298=(-333.353, 'kJ/mol'),
        S298=(-195.899, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "C#XC-XR",
    group=
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,T} {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {5,D}
5 R!H  u0 px c0 {4,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.406, 8.303, 11.6, 13.474, 15.227, 15.907, 16.407], 'J/(mol*K)'),
        H298=(-410.979, 'kJ/mol'),
        S298=(-204.353, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "C#XC-XR2",
    group=
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,T} {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 R  u0 px c0 {4,S}
6 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.902, 4.58, 8.212, 10.593, 13.246, 14.529, 15.765], 'J/(mol*K)'),
        H298=(-429.05, 'kJ/mol'),
        S298=(-201.882, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 6,
    label = "C#XC=XR",
    group=
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,T} {4,S}
4 C  u0 p0 c0 {2,D} {3,S} {5,S}
5 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.997, 1.292, 3.271, 4.542, 5.969, 6.69, 7.482], 'J/(mol*K)'),
        H298=(-471.234, 'kJ/mol'),
        S298=(-152.622, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 7,
    label = "C-XC-X",
    group=
"""
1 * X u0  p0 c0 {3,D}
2 X u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,D} {4,D}
4 C  u0  p0 c0 {2,D} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.847, 3.224, 5.377, 6.552, 7.603, 7.987, 8.243], 'J/(mol*K)'),
        H298=(-575.185, 'kJ/mol'),
        S298=(-172.682, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 8,
    label = "C-XR2C-XR",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,D}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
7 R!H  u0 px c0 {4,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.178, 10.538, 13.14, 14.737, 16.34, 16.95, 17.203], 'J/(mol*K)'),
        H298=(-193.781, 'kJ/mol'),
        S298=(-191.92, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 9,
    label = "C-XR2C-XR2",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {4,S}
8 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.944, 10.721, 13.46, 15.034, 16.536, 17.102, 17.324], 'J/(mol*K)'),
        H298=(-149.859, 'kJ/mol'),
        S298=(-192.345, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 10,
    label = "C-XR2C=XR",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,D} {3,S} {7,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.737, 6.176, 9.658, 11.873, 14.279, 15.412, 16.395], 'J/(mol*K)'),
        H298=(-331.114, 'kJ/mol'),
        S298=(-214.968, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 11,
    label = "C-XRC-XR",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u0 p0 c0 {2,S} {3,D} {6,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.8, 1.82, 4.657, 6.682, 9.212, 10.778, 13.112], 'J/(mol*K)'),
        H298=(-224.941, 'kJ/mol'),
        S298=(-194.29, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 12,
    label = "C-XRC=X",
    group=
"""
1 * X u0  p0 c0 {3,S}
2 X u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,D} {5,S}
4 C  u0  p0 c0 {2,D} {3,D}
5 R  u0  px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-5.689, -0.923, 1.99, 3.824, 5.844, 6.836, 7.789], 'J/(mol*K)'),
        H298=(-415.513, 'kJ/mol'),
        S298=(-193.307, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 13,
    label = "C=XRC-XR",
    group=
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 C  u0 p0 c0 {2,S} {3,S} {6,D}
5 R  u0 px c0 {3,S}
6 R!H  u0 px c0 {4,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-9.522, -3.487, 0.526, 3.158, 6.094, 7.472, 8.537], 'J/(mol*K)'),
        H298=(-345.568, 'kJ/mol'),
        S298=(-211.081, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 14,
    label = "C=XRC=XR",
    group=
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 C  u0 p0 c0 {2,D} {3,S} {6,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-9.568, -4.218, -0.109, 2.801, 6.219, 7.87, 9.08], 'J/(mol*K)'),
        H298=(-211.935, 'kJ/mol'),
        S298=(-184.879, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 15,
    label = "CXNX",
    group=
"""
1 X u0 p0 c0 {3,[S,D,T]}
2 * X u0 p0 c0 {4,[S,D]}
3 C u0 p0 c0 {1,[S,D,T]} {4,[S,D]}
4 N u0 p[0,1] c[0,+1] {2,[S,D]} {3,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.814, 8.69, 11.032, 12.458, 13.852, 14.367, 14.618], 'J/(mol*K)'),
        H298=(-153.699, 'kJ/mol'),
        S298=(-186.3, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 16,
    label = "C-XR2N-XR",
    group=
"""
1 X u0 p0 c0 {3,S}
2 * X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,S} {3,S} {7,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.405, 12.921, 16.012, 17.371, 18.056, 17.95, 17.424], 'J/(mol*K)'),
        H298=(-99.229, 'kJ/mol'),
        S298=(-197.829, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 17,
    label = "C-XR2N=X",
    group=
"""
1 X u0 p0 c0 {3,S}
2 * X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.669, 8.592, 11.419, 13.048, 14.565, 15.167, 15.763], 'J/(mol*K)'),
        H298=(-192.324, 'kJ/mol'),
        S298=(-193.314, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 18,
    label = "C-XRN-X",
    group=
"""
1 X u0 p0 c0 {3,S}
2 * X u0 p0 c0 {5,S}
3 C u0 p0 c0 {1,S} {4,S} {5,D}
4 R u0 px c0 {3,S}
5 N u0 p2 c0 {2,S} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.606, 2.686, 4.939, 6.472, 8.169, 8.878, 9.184], 'J/(mol*K)'),
        H298=(-76.111, 'kJ/mol'),
        S298=(-171.411, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 19,
    label = "C-XRN-XR",
    group=
"""
1 X u0  p0 c0 {3,S}
2 * X u0  p0 c0 {4,S}
3 C  u0  p0 c0 {1,S} {4,S} {5,D}
4 N  u0  p1 c0 {2,S} {3,S} {6,S}
5 R!H u0 px c0 {3,D}
6 R u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.142, 10.448, 12.782, 14.385, 16.144, 16.874, 17.246], 'J/(mol*K)'),
        H298=(-81.109, 'kJ/mol'),
        S298=(-183.708, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 20,
    label = "C-XRN=X",
    group=
"""
1 X u0  p0 c0 {3,S}
2 * X u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,S} {5,D}
4 N  u0  p1 c0 {2,D} {3,S}
5 R!H u0 px c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.842, 9.2, 10.954, 11.87, 12.579, 12.736, 12.69], 'J/(mol*K)'),
        H298=(-206.812, 'kJ/mol'),
        S298=(-188.758, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 21,
    label = "C=XRN-XR",
    group=
"""
1 X u0 p0 c0 {3,D}
2 * X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.764, 8.663, 11.11, 12.692, 14.407, 15.204, 15.963], 'J/(mol*K)'),
        H298=(-284.452, 'kJ/mol'),
        S298=(-195.23, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 22,
    label = "C=XRN=X",
    group=
"""
1 X u0 p0 c0 {3,D}
2 * X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.994, 7.386, 9.644, 11.128, 12.658, 13.207, 13.314], 'J/(mol*K)'),
        H298=(-89.141, 'kJ/mol'),
        S298=(-175.675, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 23,
    label = "CXOX",
    group=
"""
1 * X u0 {3,[S,D,T]}
2 X u0 {4,S}
3 C  u0 {1,[S,D,T]} {4,S}
4 O  u0 p2 {2,S} {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.503, 12.504, 14.797, 16.033, 16.96, 17.124, 16.993], 'J/(mol*K)'),
        H298=(-83.534, 'kJ/mol'),
        S298=(-170.773, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 24,
    label = "C-XR2O-X",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.782, 13.6, 16.068, 17.197, 17.75, 17.624, 17.161], 'J/(mol*K)'),
        H298=(-43.861, 'kJ/mol'),
        S298=(-170.273, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 25,
    label = "C-XRO-X",
    group=
"""
1 * X u0  p0 c0 {3,S}
2 X u0  p0 c0 {4,S}
3 C  u0  p0 c0 {1,S} {4,S} {5,D}
4 O  u0  p2 c0 {2,S} {3,S}
5 R!H u0 px c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([10.817, 13.644, 15.48, 16.629, 17.68, 17.938, 17.721], 'J/(mol*K)'),
        H298=(-0.284, 'kJ/mol'),
        S298=(-174.316, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 26,
    label = "C=XRO-X",
    group=
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.909, 10.268, 12.842, 14.274, 15.451, 15.809, 16.096], 'J/(mol*K)'),
        H298=(-206.457, 'kJ/mol'),
        S298=(-167.729, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 27,
    label = "NXCX",
    group=
"""
1 * X u0 p0 c0 {3,[S,D,T]}
2 X u0 p0 c0 {4,[S,D]}
3 C u0 p0 c0 {1,[S,D,T]} {4,[S,D]}
4 N u0 p[0,1] c[0,+1] {2,[S,D]} {3,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.814, 8.69, 11.032, 12.458, 13.852, 14.367, 14.618], 'J/(mol*K)'),
        H298=(-153.699, 'kJ/mol'),
        S298=(-186.3, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 28,
    label = "inv(C-XR2N-XR)",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,S} {3,S} {7,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.405, 12.921, 16.012, 17.371, 18.056, 17.95, 17.424], 'J/(mol*K)'),
        H298=(-99.229, 'kJ/mol'),
        S298=(-197.829, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 29,
    label = "inv(C-XR2N=X)",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.669, 8.592, 11.419, 13.048, 14.565, 15.167, 15.763], 'J/(mol*K)'),
        H298=(-192.324, 'kJ/mol'),
        S298=(-193.314, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 30,
    label = "inv(C-XRN-X)",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C u0 p0 c0 {1,S} {4,S} {5,D}
4 R u0 px c0 {3,S}
5 N u0 p2 c0 {2,S} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.606, 2.686, 4.939, 6.472, 8.169, 8.878, 9.184], 'J/(mol*K)'),
        H298=(-76.111, 'kJ/mol'),
        S298=(-171.411, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 31,
    label = "inv(C-XRN-XR)",
    group=
"""
1 * X u0  p0 c0 {3,S}
2 X u0  p0 c0 {4,S}
3 C  u0  p0 c0 {1,S} {4,S} {5,D}
4 N  u0  p1 c0 {2,S} {3,S} {6,S}
5 R!H u0 px c0 {3,D}
6 R u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.142, 10.448, 12.782, 14.385, 16.144, 16.874, 17.246], 'J/(mol*K)'),
        H298=(-81.109, 'kJ/mol'),
        S298=(-183.708, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 32,
    label = "inv(C-XRN=X)",
    group=
"""
1 * X u0  p0 c0 {3,S}
2 X u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,S} {5,D}
4 N  u0  p1 c0 {2,D} {3,S}
5 R!H u0 px c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.842, 9.2, 10.954, 11.87, 12.579, 12.736, 12.69], 'J/(mol*K)'),
        H298=(-206.812, 'kJ/mol'),
        S298=(-188.758, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 33,
    label = "inv(C=XRN-XR)",
    group=
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.764, 8.663, 11.11, 12.692, 14.407, 15.204, 15.963], 'J/(mol*K)'),
        H298=(-284.452, 'kJ/mol'),
        S298=(-195.23, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 34,
    label = "inv(C=XRN=X)",
    group=
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.994, 7.386, 9.644, 11.128, 12.658, 13.207, 13.314], 'J/(mol*K)'),
        H298=(-89.141, 'kJ/mol'),
        S298=(-175.675, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 35,
    label = "NXNX",
    group=
"""
1 * X u0 {3,[S,D]}
2 X u0 {4,[S,D]}
3 N  u0 {1,[S,D]} {4,[S,D]}
4 N  u0 {2,[S,D]} {3,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.107, 10.571, 12.444, 13.424, 14.153, 14.311, 14.357], 'J/(mol*K)'),
        H298=(-132.028, 'kJ/mol'),
        S298=(-177.885, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 36,
    label = "N-XRN-XR",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.625, 11.666, 13.041, 13.56, 13.614, 13.356, 12.881], 'J/(mol*K)'),
        H298=(-92.86, 'kJ/mol'),
        S298=(-159.55, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 37,
    label = "N-XRN=X",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,D}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.588, 9.475, 11.847, 13.288, 14.692, 15.266, 15.833], 'J/(mol*K)'),
        H298=(-171.196, 'kJ/mol'),
        S298=(-196.22, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 38,
    label = "NXOX",
    group=
"""
1 * X u0 p0 c0 {3,[S,D]}
2 X u0 p0 c0 {4,S}
3 N  u0 px cx {1,[S,D]} {4,[S,D]}
4 O  u0 p2 c0 {2,S} {3,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.828, 8.982, 11.072, 12.03, 12.538, 12.504, 12.333], 'J/(mol*K)'),
        H298=(-126.905, 'kJ/mol'),
        S298=(-164.124, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 39,
    label = "N-XRO-X",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 R u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.908, 11.467, 14.333, 15.65, 16.315, 16.243, 16.06], 'J/(mol*K)'),
        H298=(-122.669, 'kJ/mol'),
        S298=(-186.753, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 40,
    label = "N[+]=XR[-]O-X",
    group=
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 N  u0 p0 c+1 {1,D} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 R u0 px c-1 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.747, 6.497, 7.811, 8.41, 8.761, 8.765, 8.607], 'J/(mol*K)'),
        H298=(-131.141, 'kJ/mol'),
        S298=(-141.494, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 41,
    label = "OXOX",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.536, 7.866, 9.241, 9.716, 9.734, 9.477, 8.969], 'J/(mol*K)'),
        H298=(-54.236, 'kJ/mol'),
        S298=(-176.349, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 42,
    label = "RXbridgedBidentate",
    group=
"""
1 * X  u0 {3,[S,D,T]}
2 X  u0 {4,[S,D,T]}
3 R!H ux {1,[S,D,T]} {5,[S,D,T]}
4 R!H ux {2,[S,D,T]} {5,[S,D,T]}
5 R!H ux {3,[S,D,T]} {4,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.915, 5.633, 8.64, 10.601, 12.832, 13.947, 15.003], 'J/(mol*K)'),
        H298=(-432.744, 'kJ/mol'),
        S298=(-205.343, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 43,
    label = "CXRCX",
    group=
"""
1 * X u0 {3,[S,D,T]}
2 X u0 {4,[S,D,T]}
3 C  u0 {1,[S,D,T]} {5,[S,D,T]}
4 C  u0 {2,[S,D,T]} {5,[S,D,T]}
5 R!H  u0 {3,[S,D,T]} {4,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.358, 5.428, 8.678, 10.802, 13.21, 14.401, 15.498], 'J/(mol*K)'),
        H298=(-459.604, 'kJ/mol'),
        S298=(-209.129, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 44,
    label = "C#X-R-C#X",
    group=
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {5,T}
3 C  u0 p0 c0 {1,T} {4,S}
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,T} {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-4.884, 4.756, 10.174, 13.182, 15.816, 16.675, 17.026], 'J/(mol*K)'),
        H298=(-643.38, 'kJ/mol'),
        S298=(-243.646, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 45,
    label = "C#X-R-C-XR2",
    group=
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,T} {4,S}
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6 R  u0 px c0 {5,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.53, 3.814, 6.889, 9.138, 12.063, 13.729, 15.503], 'J/(mol*K)'),
        H298=(-479.712, 'kJ/mol'),
        S298=(-200.61, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 46,
    label = "C#X-R-C=XR",
    group=
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {5,D}
3 C  u0 p0 c0 {1,T} {4,S}
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,D} {4,S} {6,S}
6 R  u0 p0 c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.004, 5.764, 9.532, 11.978, 14.676, 15.929, 16.877], 'J/(mol*K)'),
        H298=(-440.244, 'kJ/mol'),
        S298=(-222.487, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 47,
    label = "C#X-R=C-XR",
    group=
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,T} {4,S}
4 R!H  u0 px c0 {3,S} {5,D}
5 C  u0 p0 c0 {2,S} {4,D} {6,S}
6 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.799, 11.404, 13.669, 14.882, 16.004, 16.449, 16.743], 'J/(mol*K)'),
        H298=(-376.018, 'kJ/mol'),
        S298=(-202.293, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 48,
    label = "C=X=R-C-XR2",
    group=
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,D} {4,D}
4 R!H  u0 px c0 {3,D} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6 R  u0 px c0 {5,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.015, 2.841, 6.845, 9.501, 12.496, 13.988, 15.496], 'J/(mol*K)'),
        H298=(-531.115, 'kJ/mol'),
        S298=(-217.923, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 49,
    label = "R2C-X-R-C-XR2",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6 R  u0 px c0 {5,S}
7 R  u0 px c0 {5,S}
8 R  u0 px c0 {3,S}
9 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.024, 3.612, 7.097, 9.667, 12.989, 14.82, 16.508], 'J/(mol*K)'),
        H298=(-426.768, 'kJ/mol'),
        S298=(-209.34, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 50,
    label = "RC-X=R-C-XR2",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 px c0 {3,D} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
8 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.123, 6.048, 9.544, 11.637, 13.776, 14.754, 15.729], 'J/(mol*K)'),
        H298=(-431.756, 'kJ/mol'),
        S298=(-227.783, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 51,
    label = "RC-X=R=C-XR",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 p0 c0 {3,D} {5,D}
5 C  u0 p0 c0 {2,S} {4,D} {7,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.013, 7.654, 10.526, 12.323, 14.255, 15.167, 16.031], 'J/(mol*K)'),
        H298=(-363.056, 'kJ/mol'),
        S298=(-196.347, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 52,
    label = "RC-X=R=C=X",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,D}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 p0 c0 {3,D} {5,D}
5 C  u0 p0 c0 {2,D} {4,D}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.349, -0.277, 2.079, 3.785, 5.883, 6.983, 8.012], 'J/(mol*K)'),
        H298=(-417.444, 'kJ/mol'),
        S298=(-188.069, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 53,
    label = "RC=X-R-C-XR2",
    group=
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,D} {4,S} {6,S}
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
8 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.326, 9.998, 11.71, 12.977, 14.703, 15.7, 16.623], 'J/(mol*K)'),
        H298=(-551.298, 'kJ/mol'),
        S298=(-196.129, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 54,
    label = "RC=X-R-C=XR",
    group=
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,D}
3 C  u0 p0 c0 {1,D} {4,S} {6,S}
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,D} {4,S} {7,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.897, 10.63, 13.334, 14.983, 16.737, 17.487, 17.796], 'J/(mol*K)'),
        H298=(-238.725, 'kJ/mol'),
        S298=(-203.938, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 55,
    label = "RC=X-R=C-XR",
    group=
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,D} {4,S} {6,S}
4 R!H  u0 px c0 {3,S} {5,D}
5 C  u0 p0 c0 {2,S} {4,D} {7,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-6.057, -1.103, 2.742, 5.566, 9.119, 11.137, 13.631], 'J/(mol*K)'),
        H298=(-615.735, 'kJ/mol'),
        S298=(-200.988, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 56,
    label = "CXROX",
    group=
"""
1 * X u0 {3,[S,D,T]}
2 X u0 {4,S}
3 C  u0 {1,[S,D,T]} {5,[S,D,T]}
4 O  u0 p2 {2,S} {5,S}
5 R!H  u0 px {3,[S,D,T]} {4,S}

""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.773, 6.687, 9.402, 11.279, 13.546, 14.748, 15.95], 'J/(mol*K)'),
        H298=(-416.791, 'kJ/mol'),
        S298=(-211.148, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 57,
    label = "RC-X=R-O-X",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 px c0 {3,D} {5,S}
5 O  u0 p2 c0 {2,S} {4,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.773, 6.687, 9.402, 11.279, 13.546, 14.748, 15.95], 'J/(mol*K)'),
        H298=(-416.791, 'kJ/mol'),
        S298=(-211.148, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 58,
    label = "OXROX",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 O  u0 p2 c0 {1,S} {5,S}
4 O  u0 p2 c0 {2,S} {5,S}
5 R!H  u0 px c0 {3,S} {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.33, 6.335, 8.029, 9.062, 10.207, 10.816, 11.564], 'J/(mol*K)'),
        H298=(-279.556, 'kJ/mol'),
        S298=(-179.723, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 59,
    label = "O-X-C-O-X",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 C  u0 p0 c0 {3,S} {5,S}
5 O  u0 p2 c0 {2,S} {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.33, 6.335, 8.029, 9.062, 10.207, 10.816, 11.564], 'J/(mol*K)'),
        H298=(-279.556, 'kJ/mol'),
        S298=(-179.723, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 60,
    label = "RXsingleChemisorbed",
    group=
"""
1 * X u0 {2,[S,D,T,Q]}
2 R  ux {1,[S,D,T,Q]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.736, 4.734, 6.575, 7.75, 9.067, 9.746, 10.516], 'J/(mol*K)'),
        H298=(-283.304, 'kJ/mol'),
        S298=(-167.699, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 61,
    label = "CX",
    group=
"""
1 * X u0 {2,[S,D,T,Q]}
2 C  ux {1,[S,D,T,Q]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.298, 3.393, 5.384, 6.7, 8.222, 9.017, 9.882], 'J/(mol*K)'),
        H298=(-341.801, 'kJ/mol'),
        S298=(-169.455, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 62,
    label = "C#XR",
    group=
"""
1 * X u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.337, 1.347, 3.717, 5.276, 7.07, 8.028, 9.212], 'J/(mol*K)'),
        H298=(-522.834, 'kJ/mol'),
        S298=(-175.05, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 63,
    label = "C#XCR2",
    group=
"""
1 * X u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,D}
3 C  u0 p0 c0 {1,T} {2,S}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-4.055, -1.187, 0.947, 2.528, 4.593, 5.79, 7.154], 'J/(mol*K)'),
        H298=(-534.717, 'kJ/mol'),
        S298=(-183.565, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 64,
    label = "C#XCR3",
    group=
"""
1 * X u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,T} {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.907, 1.584, 4.181, 6.073, 8.471, 9.861, 11.631], 'J/(mol*K)'),
        H298=(-587.019, 'kJ/mol'),
        S298=(-174.235, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 65,
    label = "C#XN",
    group=
"""
1 * X u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 N  u0 p1 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.513, 5.534, 6.472, 6.944, 7.314, 7.431, 7.609], 'J/(mol*K)'),
        H298=(-377.997, 'kJ/mol'),
        S298=(-161.835, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 66,
    label = "C#XOR",
    group=
"""
1 * X u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.833, 9.834, 11.905, 12.95, 13.691, 13.905, 14.428], 'J/(mol*K)'),
        H298=(-418.044, 'kJ/mol'),
        S298=(-187.544, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 67,
    label = "C-XR2",
    group=
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 R!H u0  px c0 {2,D}
4 R  u0  px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.308, 3.316, 5.308, 6.63, 8.118, 8.843, 9.538], 'J/(mol*K)'),
        H298=(-287.41, 'kJ/mol'),
        S298=(-166.429, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 68,
    label = "C-XRCR2",
    group=
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 C  u0  p0 c0 {2,D} {5,S} {6,S}
4 R  u0  px c0 {2,S}
5 R  u0  px c0 {3,S}
6 R  u0  px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.29, 4.859, 7.35, 9.038, 10.965, 11.917, 12.819], 'J/(mol*K)'),
        H298=(-296.349, 'kJ/mol'),
        S298=(-182.514, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 69,
    label = "C-XRN",
    group=
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {4,D} {3,S}
3 N  u0  p1 c0 {2,S}
4 R  u0  px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.317, 3.815, 5.358, 6.318, 7.274, 7.655, 7.964], 'J/(mol*K)'),
        H298=(-268.543, 'kJ/mol'),
        S298=(-153.59, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 70,
    label = "C-XRNR",
    group=
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 N  u0  p1 c0 {2,D} {5,S}
4 R  u0  px c0 {2,S}
5 R  u0  px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.138, 2.63, 4.403, 5.552, 6.796, 7.373, 7.911], 'J/(mol*K)'),
        H298=(-265.658, 'kJ/mol'),
        S298=(-151.565, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 71,
    label = "C-XRO",
    group=
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 O  u0  p2 c0 {2,D}
4 R  u0  px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.811, 1.985, 3.789, 4.994, 6.4, 7.127, 7.863], 'J/(mol*K)'),
        H298=(-299.07, 'kJ/mol'),
        S298=(-164.4, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 72,
    label = "C-XR3",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.942, 2.387, 4.712, 6.34, 8.353, 9.469, 10.669], 'J/(mol*K)'),
        H298=(-237.033, 'kJ/mol'),
        S298=(-177.467, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 73,
    label = "C-XR2CR3",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {3,S}
8 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.387, 3.924, 6.346, 8.022, 10.071, 11.199, 12.428], 'J/(mol*K)'),
        H298=(-242.376, 'kJ/mol'),
        S298=(-192.287, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 74,
    label = "C-XR2N",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.187, -0.519, 1.569, 3.139, 5.196, 6.372, 7.617], 'J/(mol*K)'),
        H298=(-240.088, 'kJ/mol'),
        S298=(-143.176, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 75,
    label = "C-XR2OR",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.141, -0.002, 2.2, 3.737, 5.638, 6.694, 7.8], 'J/(mol*K)'),
        H298=(-222.148, 'kJ/mol'),
        S298=(-157.564, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 76,
    label = "C=X(=R)",
    group=
"""
1 * X  u0  p0 c0 {2,D}
2 C   u0  p0 c0 {1,D} {3,D}
3 R!H u0  px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.636, 4.766, 6.547, 7.637, 8.832, 9.428, 10.027], 'J/(mol*K)'),
        H298=(-345.805, 'kJ/mol'),
        S298=(-170.526, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 77,
    label = "C=X(=C)",
    group=
"""
1 * X u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 C  u0  p0 c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.558, 4.879, 6.698, 7.792, 9.007, 9.649, 10.379], 'J/(mol*K)'),
        H298=(-403.547, 'kJ/mol'),
        S298=(-171.763, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 78,
    label = "C=X(=NR)",
    group=
"""
1 * X u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 N  u0  p1 c0 {2,D} {4,S}
4 R  u0  px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.872, 4.427, 6.095, 7.174, 8.304, 8.763, 8.972], 'J/(mol*K)'),
        H298=(-172.58, 'kJ/mol'),
        S298=(-166.816, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 79,
    label = "C=XR2",
    group=
"""
1 * X u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.584, 3.971, 6.027, 7.341, 8.844, 9.648, 10.583], 'J/(mol*K)'),
        H298=(-355.118, 'kJ/mol'),
        S298=(-165.599, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 80,
    label = "C=XRCR2",
    group=
"""
1 * X u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,D}
3 C  u0 p0 c0 {1,D} {2,S} {6,S}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {2,D}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.813, 4.083, 6.234, 7.704, 9.498, 10.486, 11.571], 'J/(mol*K)'),
        H298=(-369.621, 'kJ/mol'),
        S298=(-179.047, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 81,
    label = "C=XRCR3",
    group=
"""
1 * X u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,D} {2,S} {7,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
7 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.778, 4.719, 6.599, 7.86, 9.389, 10.262, 11.344], 'J/(mol*K)'),
        H298=(-393.27, 'kJ/mol'),
        S298=(-179.041, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 82,
    label = "C=XRN",
    group=
"""
1 * X u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 N  u0 p1 c0 {2,S}
4 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.001, 5.078, 6.087, 6.635, 7.154, 7.387, 7.694], 'J/(mol*K)'),
        H298=(-291.242, 'kJ/mol'),
        S298=(-144.277, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 83,
    label = "C=XROR",
    group=
"""
1 * X u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.049, 2.817, 4.477, 5.525, 6.776, 7.488, 8.236], 'J/(mol*K)'),
        H298=(-312.374, 'kJ/mol'),
        S298=(-146.569, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 84,
    label = "NX",
    group=
"""
1 * X u0 {2,[S,D,T]}
2 N  u0 {1,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.07, 7.28, 9.078, 10.127, 11.187, 11.695, 12.317], 'J/(mol*K)'),
        H298=(-205.842, 'kJ/mol'),
        S298=(-168.306, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 85,
    label = "N-XR",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 R  u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.702, 5.321, 6.757, 7.583, 8.38, 8.722, 9.069], 'J/(mol*K)'),
        H298=(-172.031, 'kJ/mol'),
        S298=(-165.284, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 86,
    label = "N-XCR",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 C  u0 p0 c0 {2,D} {4,D}
4 R!H  u0 px c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.421, 1.147, 1.86, 2.23, 2.65, 2.937, 3.411], 'J/(mol*K)'),
        H298=(-216.944, 'kJ/mol'),
        S298=(-145.417, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 87,
    label = "N-XCR2",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {1,S} {2,D}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.608, 9.954, 11.836, 12.985, 14.211, 14.819, 15.561], 'J/(mol*K)'),
        H298=(-197.787, 'kJ/mol'),
        S298=(-180.636, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 88,
    label = "N-XNR",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.46, 7.334, 9.012, 10.015, 11.003, 11.429, 11.874], 'J/(mol*K)'),
        H298=(-148.725, 'kJ/mol'),
        S298=(-164.071, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 89,
    label = "N-XR2",
    group=
"""
1 * X u0 p0 c0 {2,[S,D]}
2 N u0 px cx {1,[S,D]} {3,[S,D]} {4,S}
3 R u0 px c0 {2,[S,D]}
4 R u0 px cx {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.042, 8.56, 10.66, 11.961, 13.382, 14.111, 14.965], 'J/(mol*K)'),
        H298=(-187.658, 'kJ/mol'),
        S298=(-171.405, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 90,
    label = "N-XRCR",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 C  u0 p0 c0 {2,S} {5,D}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.987, 7.376, 9.536, 11.007, 12.778, 13.752, 14.963], 'J/(mol*K)'),
        H298=(-295.862, 'kJ/mol'),
        S298=(-216.907, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 91,
    label = "N-XRCR3",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,S} {2,S} {7,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
7 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([12.309, 16.976, 20.433, 23.081, 26.902, 29.654, 34.187], 'J/(mol*K)'),
        H298=(-363.723, 'kJ/mol'),
        S298=(-167.995, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 92,
    label = "N-XRNR",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,D}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([10.898, 13.865, 15.436, 16.236, 16.797, 16.876, 16.777], 'J/(mol*K)'),
        H298=(-218.6, 'kJ/mol'),
        S298=(-189.56, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 93,
    label = "N-XRNR2",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.129, 10.37, 12.332, 13.576, 14.975, 15.687, 16.376], 'J/(mol*K)'),
        H298=(-160.664, 'kJ/mol'),
        S298=(-188.5, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 94,
    label = "N-XROR",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.087, 11.692, 13.567, 14.63, 15.723, 16.248, 16.716], 'J/(mol*K)'),
        H298=(-150.726, 'kJ/mol'),
        S298=(-189.451, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 95,
    label = "N[+]-XR[-]R",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p0 c+1 {1,S} {3,S} {4,D}
3 R!H  u0 px c-1 {2,S}
4 R!H  u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.236, 9.867, 11.247, 11.962, 12.515, 12.65, 12.642], 'J/(mol*K)'),
        H298=(-147.197, 'kJ/mol'),
        S298=(-163.298, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 96,
    label = "N[+]=XR[-]R",
    group=
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p0 c+1 {1,D} {3,S} {4,S}
3 R!H  u0 px c-1 {2,S}
4 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.728, 5.688, 6.778, 7.398, 7.997, 8.253, 8.447], 'J/(mol*K)'),
        H298=(-112.622, 'kJ/mol'),
        S298=(-143.039, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 97,
    label = "N=XR",
    group=
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.509, 3.839, 6.171, 7.446, 8.598, 9.078, 9.714], 'J/(mol*K)'),
        H298=(-295.417, 'kJ/mol'),
        S298=(-168.676, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 98,
    label = "N=XC#R",
    group=
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 C  u0 p0 c0 {2,S} {4,T}
4 R  u0 px c0 {3,T}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-6.989, -4.603, -3.581, -3.072, -2.447, -1.961, -1.142], 'J/(mol*K)'),
        H298=(-277.45, 'kJ/mol'),
        S298=(-142.031, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 99,
    label = "N=XC-R",
    group=
"""
1 * X u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S}
3 N  u0 p1 c0 {1,D} {2,S}
4 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.614, 9.468, 11.121, 12.197, 13.469, 14.191, 15.174], 'J/(mol*K)'),
        H298=(-341.848, 'kJ/mol'),
        S298=(-176.565, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 100,
    label = "N=XN",
    group=
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 N  u0 p1 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([11.303, 15.422, 17.092, 17.515, 16.969, 16.192, 15.433], 'J/(mol*K)'),
        H298=(-218.159, 'kJ/mol'),
        S298=(-174.51, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 101,
    label = "N=XOR",
    group=
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([9.017, 13.03, 14.825, 15.531, 15.693, 15.491, 15.382], 'J/(mol*K)'),
        H298=(-239.997, 'kJ/mol'),
        S298=(-178.708, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 102,
    label = "OX",
    group=
"""
1 * X u0 {2,[S,D]}
2 O  ux {1,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.429, 6.188, 7.189, 7.815, 8.523, 8.912, 9.424], 'J/(mol*K)'),
        H298=(-153.381, 'kJ/mol'),
        S298=(-155.727, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 103,
    label = "O-XR",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.044, 4.902, 5.986, 6.67, 7.447, 7.867, 8.404], 'J/(mol*K)'),
        H298=(-156.503, 'kJ/mol'),
        S298=(-151.553, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 104,
    label = "O-XCR2",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,D}
3 O  u0 p2 c0 {1,S} {2,S}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([11.169, 13.366, 14.539, 15.213, 15.906, 16.227, 16.51], 'J/(mol*K)'),
        H298=(-169.296, 'kJ/mol'),
        S298=(-194.234, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 105,
    label = "O-XCR3",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.445, 2.24, 2.925, 3.538, 4.489, 5.184, 6.345], 'J/(mol*K)'),
        H298=(-164.517, 'kJ/mol'),
        S298=(-149.812, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 106,
    label = "O-XN",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 N  u0 p1 c0 {3,S}
3 O  u0 p2 c0 {1,S} {2,S}

""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.23, 4.154, 5.771, 6.686, 7.575, 7.955, 8.262], 'J/(mol*K)'),
        H298=(-106.856, 'kJ/mol'),
        S298=(-134.71, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 107,
    label = "O-XOR",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([10.207, 11.382, 11.381, 11.023, 10.193, 9.56, 8.77], 'J/(mol*K)'),
        H298=(-87.531, 'kJ/mol'),
        S298=(-120.712, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 108,
    label = "RXvdW",
    group=
"""
1 * X u0
2 R  u0
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.618, 6.887, 7.601, 8.033, 8.504, 8.745, 8.987], 'J/(mol*K)'),
        H298=(-63.668, 'kJ/mol'),
        S298=(-128.976, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 109,
    label = "(CR2)X",
    group=
"""
1 * X  u0
2 C   u0 {3,T} {4,S}
3 R!H u0 {2,T}
4 R   u0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.204, 2.484, 2.649, 2.795, 3.123, 3.488, 4.251], 'J/(mol*K)'),
        H298=(-63.462, 'kJ/mol'),
        S298=(-120.514, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 110,
    label = "(CRCR)X",
    group=
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {2,T} {5,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.391, -0.19, -0.063, 0.059, 0.385, 0.816, 1.884], 'J/(mol*K)'),
        H298=(-67.756, 'kJ/mol'),
        S298=(-119.645, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 111,
    label = "(CRN)X",
    group=
"""
1 * X u0  p0 c0
2 C  u0  p0 c0 {3,T} {4,S}
3 N  u0  p1 c0 {2,T}
4 R  u0  px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.394, 7.832, 8.074, 8.267, 8.599, 8.832, 8.985], 'J/(mol*K)'),
        H298=(-54.873, 'kJ/mol'),
        S298=(-122.254, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 112,
    label = "(CR3)X",
    group=
"""
1 * X  u0
2 C   u0 {3,D} {4,S} {5,S}
3 R!H u0 {2,D}
4 R   u0 {2,S}
5 R   u0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.176, 7.536, 8.289, 8.717, 9.118, 9.268, 9.344], 'J/(mol*K)'),
        H298=(-54.812, 'kJ/mol'),
        S298=(-130.966, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 113,
    label = "(CR2CR)X",
    group=
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 C  u0 p0 c0 {2,D} {6,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.429, 9.04, 9.921, 10.423, 10.896, 11.075, 11.173], 'J/(mol*K)'),
        H298=(-99.654, 'kJ/mol'),
        S298=(-143.863, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 114,
    label = "(CR2N)X",
    group=
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {2,D}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.299, 6.343, 7.876, 8.574, 8.928, 8.866, 8.608], 'J/(mol*K)'),
        H298=(-56.246, 'kJ/mol'),
        S298=(-135.288, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 115,
    label = "(CR2O)X",
    group=
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 O  u0 p2 c0 {2,D}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.999, 6.871, 7.393, 7.722, 8.089, 8.264, 8.393], 'J/(mol*K)'),
        H298=(-27.619, 'kJ/mol'),
        S298=(-122.364, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 116,
    label = "(CR4)X",
    group=
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.688, 8.694, 9.215, 9.504, 9.784, 9.904, 10.0], 'J/(mol*K)'),
        H298=(-52.605, 'kJ/mol'),
        S298=(-118.627, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 117,
    label = "(CR3CR3)X",
    group=
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
7 R  u0 px c0 {3,S}
8 R  u0 px c0 {3,S}
9 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([9.04, 9.934, 10.397, 10.672, 10.97, 11.108, 11.195], 'J/(mol*K)'),
        H298=(-52.163, 'kJ/mol'),
        S298=(-137.338, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 118,
    label = "(CR3N)X",
    group=
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.932, 3.145, 4.574, 5.506, 6.556, 7.095, 7.704], 'J/(mol*K)'),
        H298=(-124.618, 'kJ/mol'),
        S298=(-141.215, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 119,
    label = "(CR3OR)X",
    group=
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {2,S} {7,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
7 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.436, 9.528, 10.024, 10.252, 10.408, 10.449, 10.467], 'J/(mol*K)'),
        H298=(-43.023, 'kJ/mol'),
        S298=(-139.363, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 120,
    label = "(NR2)X",
    group=
"""
1 * X u0 p0 c0
2 N   u0 p1 c0 {3,D} {4,S}
3 R!H u0 px c0 {2,D}
4 R   u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.54, 7.091, 7.441, 7.69, 8.006, 8.18, 8.339], 'J/(mol*K)'),
        H298=(-71.36, 'kJ/mol'),
        S298=(-122.197, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 121,
    label = "(N=C)X",
    group=
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,D}
3 C  u0 p0 c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.54, 7.091, 7.441, 7.69, 8.006, 8.18, 8.339], 'J/(mol*K)'),
        H298=(-71.36, 'kJ/mol'),
        S298=(-122.197, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 122,
    label = "(NR3)X",
    group=
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.702, 6.186, 7.691, 8.647, 9.72, 10.261, 10.798], 'J/(mol*K)'),
        H298=(-93.36, 'kJ/mol'),
        S298=(-136.79, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 123,
    label = "(NC)X",
    group=
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S}
3 C  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.687, 6.032, 6.825, 7.329, 7.911, 8.22, 8.494], 'J/(mol*K)'),
        H298=(-72.533, 'kJ/mol'),
        S298=(-138.501, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 124,
    label = "(NN)X",
    group=
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S}
3 N  u0 p1 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.776, 4.013, 5.344, 6.178, 7.098, 7.552, 8.006], 'J/(mol*K)'),
        H298=(-131.568, 'kJ/mol'),
        S298=(-150.696, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 125,
    label = "(NO)X",
    group=
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S}
3 O  u0 p2 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.322, 5.152, 6.208, 6.849, 7.534, 7.863, 8.173], 'J/(mol*K)'),
        H298=(-58.224, 'kJ/mol'),
        S298=(-132.089, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 126,
    label = "(OR)X",
    group=
"""
1 * X u0 p0 c0
2 O u0 p2 c0 {3,D}
3 R u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.708, 6.011, 6.788, 7.301, 7.93, 8.274, 8.565], 'J/(mol*K)'),
        H298=(-92.095, 'kJ/mol'),
        S298=(-141.385, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 127,
    label = "(ONR)X",
    group=
"""
1 * X u0 p0 c0
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 R u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.708, 6.011, 6.788, 7.301, 7.93, 8.274, 8.565], 'J/(mol*K)'),
        H298=(-92.095, 'kJ/mol'),
        S298=(-141.385, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 128,
    label = "(ONN)X",
    group=
"""
1 * X u0 p0 c0
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 N u0 p2 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.682, 6.734, 7.311, 7.663, 8.05, 8.242, 8.401], 'J/(mol*K)'),
        H298=(-105.851, 'kJ/mol'),
        S298=(-139.884, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 129,
    label = "(ONOR)X",
    group=
"""
1 * X u0 p0 c0
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 R u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.761, 4.564, 5.742, 6.578, 7.689, 8.338, 8.892], 'J/(mol*K)'),
        H298=(-64.584, 'kJ/mol'),
        S298=(-144.387, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 130,
    label = "(OR2)X",
    group=
"""
1 * X u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 R  u0 p[0,1,2] c0 {2,S}
4 R  u0 p[0,1,2] c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.402, 6.003, 6.837, 7.327, 7.877, 8.177, 8.462], 'J/(mol*K)'),
        H298=(-13.802, 'kJ/mol'),
        S298=(-98.276, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 131,
    label = "(OROR)X",
    group=
"""
1 * X u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.316, 7.23, 7.68, 7.947, 8.291, 8.512, 8.707], 'J/(mol*K)'),
        H298=(-21.964, 'kJ/mol'),
        S298=(-110.352, 'J/(mol*K)'),
    ),
shortDesc=u"""""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

tree(
"""
L1: RX
    L2: RXbidentate
        L3: CXCX
            L4: C#XC-XR
            L4: C#XC-XR2
            L4: C#XC=XR
            L4: C-XC-X
            L4: C-XR2C-XR
            L4: C-XR2C-XR2
            L4: C-XR2C=XR
            L4: C-XRC-XR
            L4: C-XRC=X
            L4: C=XRC-XR
            L4: C=XRC=XR
        L3: CXNX
            L4: C-XR2N-XR
            L4: C-XR2N=X
            L4: C-XRN-X
            L4: C-XRN-XR
            L4: C-XRN=X
            L4: C=XRN-XR
            L4: C=XRN=X
        L3: CXOX
            L4: C-XR2O-X
            L4: C-XRO-X
            L4: C=XRO-X
        L3: NXCX
            L4: inv(C-XR2N-XR)
            L4: inv(C-XR2N=X)
            L4: inv(C-XRN-X)
            L4: inv(C-XRN-XR)
            L4: inv(C-XRN=X)
            L4: inv(C=XRN-XR)
            L4: inv(C=XRN=X)
        L3: NXNX
            L4: N-XRN-XR
            L4: N-XRN=X
        L3: NXOX
            L4: N-XRO-X
            L4: N[+]=XR[-]O-X
        L3: OXOX
    L2: RXbridgedBidentate
        L3: CXRCX
            L4: C#X-R-C#X
            L4: C#X-R-C-XR2
            L4: C#X-R-C=XR
            L4: C#X-R=C-XR
            L4: C=X=R-C-XR2
            L4: R2C-X-R-C-XR2
            L4: RC-X=R-C-XR2
            L4: RC-X=R=C-XR
            L4: RC-X=R=C=X
            L4: RC=X-R-C-XR2
            L4: RC=X-R-C=XR
            L4: RC=X-R=C-XR
        L3: CXROX
            L4: RC-X=R-O-X
        L3: OXROX
            L4: O-X-C-O-X
    L2: RXsingleChemisorbed
        L3: CX
            L4: C#XR
                L5: C#XCR2
                L5: C#XCR3
                L5: C#XN
                L5: C#XOR
            L4: C-XR2
                L5: C-XRCR2
                L5: C-XRN
                L5: C-XRNR
                L5: C-XRO
            L4: C-XR3
                L5: C-XR2CR3
                L5: C-XR2N
                L5: C-XR2OR
            L4: C=X(=R)
                L5: C=X(=C)
                L5: C=X(=NR)
            L4: C=XR2
                L5: C=XRCR2
                L5: C=XRCR3
                L5: C=XRN
                L5: C=XROR
        L3: NX
            L4: N-XR
                L5: N-XCR
                L5: N-XCR2
                L5: N-XNR
            L4: N-XR2
                L5: N-XRCR
                L5: N-XRCR3
                L5: N-XRNR
                L5: N-XRNR2
                L5: N-XROR
                L5: N[+]-XR[-]R
                L5: N[+]=XR[-]R
            L4: N=XR
                L5: N=XC#R
                L5: N=XC-R
                L5: N=XN
                L5: N=XOR
        L3: OX
            L4: O-XR
                L5: O-XCR2
                L5: O-XCR3
                L5: O-XN
                L5: O-XOR
    L2: RXvdW
        L3: (CR2)X
            L4: (CRCR)X
            L4: (CRN)X
        L3: (CR3)X
            L4: (CR2CR)X
            L4: (CR2N)X
            L4: (CR2O)X
        L3: (CR4)X
            L4: (CR3CR3)X
            L4: (CR3N)X
            L4: (CR3OR)X
        L3: (NR2)X
            L4: (N=C)X
        L3: (NR3)X
            L4: (NC)X
            L4: (NN)X
            L4: (NO)X
        L3: (OR)X
            L4: (ONR)X
                L5: (ONN)X
                L5: (ONOR)X
        L3: (OR2)X
            L4: (OROR)X
""",
)
