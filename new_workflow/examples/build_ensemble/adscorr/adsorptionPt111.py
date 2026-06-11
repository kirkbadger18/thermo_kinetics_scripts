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
        Cpdata=([-4.816, -0.605, 1.942, 3.481, 4.994, 5.592, 5.987], 'J/(mol*K)'),
        H298=(-196.429, 'kJ/mol'),
        S298=(-186.722, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCXCCH2', 'XCXCH2', 'XCXCHCH3', 'XCXCCH3', 'XCXC', 'XCH2XCCH2',
'XCH2XCH2', 'CH3XCHXCH2', 'XCH2XCH', 'XCH2XCOH', 'XCHXCHCH3', 'XCHXCCH3',
'XCHXC', 'XCHXCO', 'XCHXCH', 'XCH2XNH', 'XCH2XN', 'XCHXN', 'NHXCXNH', 'XNHXCO',
'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XCH2XO', 'XOXCNH',
'XCHXO', 'XCH2XNH', 'XCH2XN', 'XCHXN', 'NHXCXNH', 'XNHXCO', 'XNXCO', 'XNXCNH',
'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XNHXNH', 'CH3XNXNOH', 'XNHXN',
'XNXNCH3', 'XOXNH', 'XOXNO', 'XCXCCH2', 'XCXCH2', 'XCXCHCH3', 'XCXCCH3', 'XCXC',
'XCH2XCCH2', 'XCH2XCH2', 'CH3XCHXCH2', 'XCH2XCH', 'XCH2XCOH', 'XCHXCHCH3',
'XCHXCCH3', 'XCHXC', 'XCHXCO', 'XCHXCH', 'XCXCCH2', 'XCXCH2', 'XCXCHCH3',
'XCXCCH3', 'XCXC', 'XCH2XCCH2', 'XCH2XCH2', 'CH3XCHXCH2', 'XCH2XCH', 'XCH2XCOH',
'XCHXCHCH3', 'XCHXCCH3', 'XCHXC', 'XCHXCO', 'XCHXCH', 'XCH2XNH', 'XCH2XN',
'XCHXN', 'NHXCXNH', 'XNHXCO', 'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN',
'XNXCOH', 'XCH2XNH', 'XCH2XN', 'XCHXN', 'NHXCXNH', 'XNHXCO', 'XNXCO', 'XNXCNH',
'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XCH2XO', 'XOXCNH', 'XCHXO', 'XCH2XO',
'XOXCNH', 'XCHXO', 'XCH2XNH', 'XCH2XN', 'XCHXN', 'NHXCXNH', 'XNHXCO', 'XNXCO',
'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XCH2XNH', 'XCH2XN', 'XCHXN',
'NHXCXNH', 'XNHXCO', 'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH',
'XNHXNH', 'CH3XNXNOH', 'XNHXN', 'XNXNCH3', 'XNHXNH', 'CH3XNXNOH', 'XNHXN',
'XNXNCH3', 'XOXNH', 'XOXNO', 'XOXNH', 'XOXNO']""",
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
1 * X u0 p0 c0 {3,[S,D,T]}
2 X u0 p0 c0 {4,[S,D,T]}
3 C  u0 {1,[S,D,T]} {4,[S,D,T]}
4 C  u0 {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-8.884, -3.936, -0.796, 1.195, 3.346, 4.351, 5.233], 'J/(mol*K)'),
        H298=(-330.142, 'kJ/mol'),
        S298=(-195.899, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCXCCH2', 'XCXCH2', 'XCXCHCH3', 'XCXCCH3', 'XCXC', 'XCH2XCCH2',
'XCH2XCH2', 'CH3XCHXCH2', 'XCH2XCH', 'XCH2XCOH', 'XCHXCHCH3', 'XCHXCCH3',
'XCHXC', 'XCHXCO', 'XCHXCH', 'XCXCCH2', 'XCXCH2', 'XCXCHCH3', 'XCXCCH3', 'XCXC',
'XCH2XCCH2', 'XCH2XCH2', 'CH3XCHXCH2', 'XCH2XCH', 'XCH2XCOH', 'XCHXCHCH3',
'XCHXCCH3', 'XCHXC', 'XCHXCO', 'XCHXCH']""",
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
        Cpdata=([-5.908, -0.012, 3.286, 5.159, 6.913, 7.592, 8.093], 'J/(mol*K)'),
        H298=(-415.597, 'kJ/mol'),
        S298=(-204.353, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCXCCH2']""",
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
        Cpdata=([-9.216, -3.734, -0.103, 2.279, 4.931, 6.215, 7.45], 'J/(mol*K)'),
        H298=(-428.723, 'kJ/mol'),
        S298=(-201.882, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCXCH2', 'XCXCHCH3']""",
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
        Cpdata=([-10.312, -7.023, -5.043, -3.772, -2.346, -1.624, -0.832], 'J/(mol*K)'),
        H298=(-473.155, 'kJ/mol'),
        S298=(-152.622, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCXCCH3']""",
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
        Cpdata=([-9.162, -5.09, -2.937, -1.762, -0.711, -0.328, -0.071], 'J/(mol*K)'),
        H298=(-586.54, 'kJ/mol'),
        S298=(-172.682, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCXC']""",
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
        Cpdata=([-2.136, 2.224, 4.826, 6.423, 8.025, 8.636, 8.889], 'J/(mol*K)'),
        H298=(-173.935, 'kJ/mol'),
        S298=(-191.92, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XCCH2']""",
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
        Cpdata=([-2.371, 2.407, 5.145, 6.72, 8.221, 8.788, 9.01], 'J/(mol*K)'),
        H298=(-134.976, 'kJ/mol'),
        S298=(-192.345, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XCH2', 'CH3XCHXCH2']""",
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
        Cpdata=([-7.577, -2.139, 1.344, 3.558, 5.964, 7.098, 8.08], 'J/(mol*K)'),
        H298=(-322.414, 'kJ/mol'),
        S298=(-214.968, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XCH', 'XCH2XCOH', 'XCHXCHCH3']""",
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
        Cpdata=([-10.114, -6.494, -3.657, -1.632, 0.897, 2.463, 4.797], 'J/(mol*K)'),
        H298=(-221.524, 'kJ/mol'),
        S298=(-194.29, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXCCH3']""",
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
        Cpdata=([-14.003, -9.238, -6.324, -4.491, -2.471, -1.479, -0.526], 'J/(mol*K)'),
        H298=(-423.027, 'kJ/mol'),
        S298=(-193.307, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXC']""",
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
        Cpdata=([-17.837, -11.801, -7.788, -5.157, -2.221, -0.843, 0.222], 'J/(mol*K)'),
        H298=(-350.627, 'kJ/mol'),
        S298=(-211.081, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXCO']""",
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
        Cpdata=([-17.882, -12.533, -8.423, -5.514, -2.095, -0.445, 0.766], 'J/(mol*K)'),
        H298=(-213.089, 'kJ/mol'),
        S298=(-184.879, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXCH']""",
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
4 N u0 p1 c0 {2,[S,D]} {3,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.501, 0.376, 2.717, 4.144, 5.537, 6.052, 6.303], 'J/(mol*K)'),
        H298=(-144.194, 'kJ/mol'),
        S298=(-186.3, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XNH', 'XCH2XN', 'XCHXN', 'NHXCXNH', 'XNHXCO', 'XNXCO',
'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XCH2XNH', 'XCH2XN', 'XCHXN',
'NHXCXNH', 'XNHXCO', 'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH']""",
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
        Cpdata=([-1.909, 4.606, 7.698, 9.056, 9.742, 9.635, 9.11], 'J/(mol*K)'),
        H298=(-91.329, 'kJ/mol'),
        S298=(-197.829, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XNH']""",
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
        Cpdata=([-4.645, 0.277, 3.104, 4.734, 6.251, 6.853, 7.449], 'J/(mol*K)'),
        H298=(-191.952, 'kJ/mol'),
        S298=(-193.314, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XN']""",
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
5 N u0 p1 c0 {2,S} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-8.92, -5.628, -3.376, -1.842, -0.146, 0.563, 0.869], 'J/(mol*K)'),
        H298=(-64.271, 'kJ/mol'),
        S298=(-171.411, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXN']""",
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
        Cpdata=([-1.172, 2.134, 4.468, 6.071, 7.829, 8.56, 8.932], 'J/(mol*K)'),
        H298=(-68.078, 'kJ/mol'),
        S298=(-183.708, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['NHXCXNH', 'XNHXCO']""",
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
        Cpdata=([-2.472, 0.885, 2.64, 3.556, 4.264, 4.422, 4.376], 'J/(mol*K)'),
        H298=(-195.161, 'kJ/mol'),
        S298=(-188.758, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNXCO', 'XNXCNH']""",
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
        Cpdata=([-3.55, 0.349, 2.796, 4.377, 6.094, 6.89, 7.649], 'J/(mol*K)'),
        H298=(-276.737, 'kJ/mol'),
        S298=(-195.23, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXNH', 'OHXCXNH']""",
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
        Cpdata=([-4.321, -0.928, 1.329, 2.814, 4.344, 4.892, 4.999], 'J/(mol*K)'),
        H298=(-79.315, 'kJ/mol'),
        S298=(-175.675, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXN', 'XNXCOH']""",
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
1 * X u0 p0 c0 {3,[S,D,T]}
2 X u0 p0 c0 {4,S}
3 C  u0 {1,[S,D,T]} {4,S}
4 O  u0 p2 {2,S} {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.188, 4.19, 6.483, 7.719, 8.646, 8.809, 8.678], 'J/(mol*K)'),
        H298=(-77.447, 'kJ/mol'),
        S298=(-170.773, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XO', 'XOXCNH', 'XCHXO', 'XCH2XO', 'XOXCNH', 'XCHXO']""",
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
        Cpdata=([0.468, 5.286, 7.754, 8.883, 9.435, 9.309, 8.847], 'J/(mol*K)'),
        H298=(-38.646, 'kJ/mol'),
        S298=(-170.273, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XO']""",
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
        Cpdata=([2.502, 5.33, 7.166, 8.314, 9.366, 9.623, 9.407], 'J/(mol*K)'),
        H298=(12.768, 'kJ/mol'),
        S298=(-174.316, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOXCNH']""",
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
        Cpdata=([-2.405, 1.953, 4.528, 5.96, 7.136, 7.494, 7.781], 'J/(mol*K)'),
        H298=(-206.464, 'kJ/mol'),
        S298=(-167.729, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXO']""",
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
4 N u0 p1 c0 {2,[S,D]} {3,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.501, 0.376, 2.717, 4.144, 5.537, 6.052, 6.303], 'J/(mol*K)'),
        H298=(-144.194, 'kJ/mol'),
        S298=(-186.3, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XNH', 'XCH2XN', 'XCHXN', 'NHXCXNH', 'XNHXCO', 'XNXCO',
'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XCH2XNH', 'XCH2XN', 'XCHXN',
'NHXCXNH', 'XNHXCO', 'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH']""",
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
        Cpdata=([-1.909, 4.606, 7.698, 9.056, 9.742, 9.635, 9.11], 'J/(mol*K)'),
        H298=(-91.329, 'kJ/mol'),
        S298=(-197.829, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XNH']""",
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
        Cpdata=([-4.645, 0.277, 3.104, 4.734, 6.251, 6.853, 7.449], 'J/(mol*K)'),
        H298=(-191.952, 'kJ/mol'),
        S298=(-193.314, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XN']""",
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
5 N u0 p1 c0 {2,S} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-8.92, -5.628, -3.376, -1.842, -0.146, 0.563, 0.869], 'J/(mol*K)'),
        H298=(-64.271, 'kJ/mol'),
        S298=(-171.411, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXN']""",
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
        Cpdata=([-1.172, 2.134, 4.468, 6.071, 7.829, 8.56, 8.932], 'J/(mol*K)'),
        H298=(-68.078, 'kJ/mol'),
        S298=(-183.708, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['NHXCXNH', 'XNHXCO']""",
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
        Cpdata=([-2.472, 0.885, 2.64, 3.556, 4.264, 4.422, 4.376], 'J/(mol*K)'),
        H298=(-195.161, 'kJ/mol'),
        S298=(-188.758, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNXCO', 'XNXCNH']""",
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
        Cpdata=([-3.55, 0.349, 2.796, 4.377, 6.094, 6.89, 7.649], 'J/(mol*K)'),
        H298=(-276.737, 'kJ/mol'),
        S298=(-195.23, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXNH', 'OHXCXNH']""",
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
        Cpdata=([-4.321, -0.928, 1.329, 2.814, 4.344, 4.892, 4.999], 'J/(mol*K)'),
        H298=(-79.315, 'kJ/mol'),
        S298=(-175.675, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXN', 'XNXCOH']""",
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
1 * X u0 p0 c0 {3,[S,D]}
2 X u0 p0 c0 {4,[S,D]}
3 N  u0 {1,[S,D]} {4,[S,D]}
4 N  u0 {2,[S,D]} {3,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.208, 2.256, 4.13, 5.109, 5.838, 5.997, 6.042], 'J/(mol*K)'),
        H298=(-109.477, 'kJ/mol'),
        S298=(-177.885, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHXNH', 'CH3XNXNOH', 'XNHXN', 'XNXNCH3', 'XNHXNH',
'CH3XNXNOH', 'XNHXN', 'XNXNCH3']""",
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
        Cpdata=([0.311, 3.352, 4.726, 5.245, 5.299, 5.042, 4.566], 'J/(mol*K)'),
        H298=(-71.858, 'kJ/mol'),
        S298=(-159.55, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHXNH', 'CH3XNXNOH']""",
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
        Cpdata=([-2.727, 1.161, 3.532, 4.973, 6.377, 6.953, 7.518], 'J/(mol*K)'),
        H298=(-147.096, 'kJ/mol'),
        S298=(-196.22, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHXN', 'XNXNCH3']""",
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
        Cpdata=([-3.488, 0.667, 2.757, 3.716, 4.224, 4.19, 4.019], 'J/(mol*K)'),
        H298=(-120.538, 'kJ/mol'),
        S298=(-164.124, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOXNH', 'XOXNO', 'XOXNH', 'XOXNO']""",
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
        Cpdata=([-2.407, 3.152, 6.018, 7.336, 8.0, 7.929, 7.745], 'J/(mol*K)'),
        H298=(-110.054, 'kJ/mol'),
        S298=(-186.753, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOXNH']""",
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
5 R!H u0 p[1,2,3] c-1 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-4.568, -1.818, -0.504, 0.096, 0.447, 0.451, 0.292], 'J/(mol*K)'),
        H298=(-131.021, 'kJ/mol'),
        S298=(-141.494, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOXNO']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 41,
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
        Cpdata=([-7.399, -2.681, 0.326, 2.287, 4.517, 5.632, 6.689], 'J/(mol*K)'),
        H298=(-423.669, 'kJ/mol'),
        S298=(-205.343, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCH2XC', 'XCCH2XCH2', 'XCHCH2XC', 'XCHCHXC', 'XCCHXCH2',
'XCH2CH2XCH2', 'XCHCHXCH2', 'XCHCXCH', 'XCHCXC', 'XCHCH2XCH2', 'XCHCH2XCH',
'XCHCHXCH', 'XCHCHXO', 'XOC(O)XO', 'H2C(XO)XO', 'XCCH2XC', 'XCCH2XCH2',
'XCHCH2XC', 'XCHCHXC', 'XCCHXCH2', 'XCH2CH2XCH2', 'XCHCHXCH2', 'XCHCXCH',
'XCHCXC', 'XCHCH2XCH2', 'XCHCH2XCH', 'XCHCHXCH', 'XCCH2XC', 'XCCH2XCH2',
'XCHCH2XC', 'XCHCHXC', 'XCCHXCH2', 'XCH2CH2XCH2', 'XCHCHXCH2', 'XCHCXCH',
'XCHCXC', 'XCHCH2XCH2', 'XCHCH2XCH', 'XCHCHXCH', 'XCHCHXO', 'XCHCHXO',
'XOC(O)XO', 'H2C(XO)XO', 'XOC(O)XO', 'H2C(XO)XO']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 42,
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
        Cpdata=([-7.956, -2.886, 0.364, 2.487, 4.895, 6.087, 7.184], 'J/(mol*K)'),
        H298=(-448.755, 'kJ/mol'),
        S298=(-209.129, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCH2XC', 'XCCH2XCH2', 'XCHCH2XC', 'XCHCHXC', 'XCCHXCH2',
'XCH2CH2XCH2', 'XCHCHXCH2', 'XCHCXCH', 'XCHCXC', 'XCHCH2XCH2', 'XCHCH2XCH',
'XCHCHXCH', 'XCCH2XC', 'XCCH2XCH2', 'XCHCH2XC', 'XCHCHXC', 'XCCHXCH2',
'XCH2CH2XCH2', 'XCHCHXCH2', 'XCHCXCH', 'XCHCXC', 'XCHCH2XCH2', 'XCHCH2XCH',
'XCHCHXCH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 43,
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
        Cpdata=([-13.199, -3.559, 1.86, 4.867, 7.501, 8.36, 8.712], 'J/(mol*K)'),
        H298=(-646.481, 'kJ/mol'),
        S298=(-243.646, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCH2XC']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 44,
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
        Cpdata=([-8.845, -4.501, -1.425, 0.824, 3.748, 5.415, 7.189], 'J/(mol*K)'),
        H298=(-471.143, 'kJ/mol'),
        S298=(-200.61, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCH2XCH2']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 45,
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
        Cpdata=([-8.318, -2.551, 1.217, 3.663, 6.362, 7.614, 8.562], 'J/(mol*K)'),
        H298=(-441.934, 'kJ/mol'),
        S298=(-222.487, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCH2XC']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 46,
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
        Cpdata=([-1.515, 3.089, 5.355, 6.567, 7.69, 8.134, 8.428], 'J/(mol*K)'),
        H298=(-377.647, 'kJ/mol'),
        S298=(-202.293, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCHXC']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 47,
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
        Cpdata=([-11.329, -5.473, -1.47, 1.186, 4.182, 5.673, 7.181], 'J/(mol*K)'),
        H298=(-527.876, 'kJ/mol'),
        S298=(-217.923, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCHXCH2']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 48,
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
        Cpdata=([-9.338, -4.702, -1.218, 1.353, 4.674, 6.506, 8.194], 'J/(mol*K)'),
        H298=(-401.709, 'kJ/mol'),
        S298=(-209.34, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2CH2XCH2']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 49,
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
        Cpdata=([-8.191, -2.267, 1.229, 3.323, 5.462, 6.44, 7.415], 'J/(mol*K)'),
        H298=(-420.692, 'kJ/mol'),
        S298=(-227.783, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCHXCH2']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 50,
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
        Cpdata=([-5.301, -0.66, 2.211, 4.009, 5.941, 6.852, 7.716], 'J/(mol*K)'),
        H298=(-346.102, 'kJ/mol'),
        S298=(-196.347, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCXCH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 51,
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
        Cpdata=([-11.663, -8.592, -6.236, -4.529, -2.431, -1.331, -0.302], 'J/(mol*K)'),
        H298=(-400.176, 'kJ/mol'),
        S298=(-188.069, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCXC']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 52,
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
        Cpdata=([-0.988, 1.684, 3.396, 4.662, 6.389, 7.386, 8.308], 'J/(mol*K)'),
        H298=(-529.783, 'kJ/mol'),
        S298=(-196.129, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCH2XCH2']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 53,
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
        Cpdata=([-2.417, 2.316, 5.02, 6.669, 8.422, 9.172, 9.482], 'J/(mol*K)'),
        H298=(-223.966, 'kJ/mol'),
        S298=(-203.938, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCH2XCH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 54,
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
        Cpdata=([-14.372, -9.417, -5.572, -2.749, 0.804, 2.822, 5.317], 'J/(mol*K)'),
        H298=(-597.546, 'kJ/mol'),
        S298=(-200.988, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCHXCH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 55,
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
        Cpdata=([-5.542, -1.627, 1.088, 2.965, 5.232, 6.433, 7.636], 'J/(mol*K)'),
        H298=(-408.836, 'kJ/mol'),
        S298=(-211.148, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCHXO', 'XCHCHXO']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 56,
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
        Cpdata=([-5.542, -1.627, 1.088, 2.965, 5.232, 6.433, 7.636], 'J/(mol*K)'),
        H298=(-408.836, 'kJ/mol'),
        S298=(-211.148, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCHXO']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 57,
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
        Cpdata=([-4.984, -1.979, -0.285, 0.747, 1.892, 2.502, 3.249], 'J/(mol*K)'),
        H298=(-280.57, 'kJ/mol'),
        S298=(-179.723, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOC(O)XO', 'H2C(XO)XO', 'XOC(O)XO', 'H2C(XO)XO']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 58,
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
        Cpdata=([-4.984, -1.979, -0.285, 0.747, 1.892, 2.502, 3.249], 'J/(mol*K)'),
        H298=(-280.57, 'kJ/mol'),
        S298=(-179.723, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOC(O)XO', 'H2C(XO)XO']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 59,
    label = "RXsingleChemisorbed",
    group=
"""
1 * X u0 {2,[S,D,T,Q]}
2 R  ux {1,[S,D,T,Q]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-6.437, -3.459, -1.628, -0.459, 0.853, 1.529, 2.296], 'J/(mol*K)'),
        H298=(-268.979, 'kJ/mol'),
        S298=(-167.851, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCN', 'XCH', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3',
'XCCH2OH', 'XCNO', 'XCNH2', 'XCOH', 'XCHCO', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2',
'XCHCH2', 'XCHCHCH3', 'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO',
'XCOOH', 'CH3XCO', 'CH3CH2XCO', 'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3',
'CH3XCHCH3', 'CH3XCHOH', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCCO', 'XCCCH2',
'XCCH2', 'XCNH', 'XCH2', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH',
'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH',
'XNO', 'XNCNH', 'XNCO', 'XNCH2', 'XNNH', 'XNNCH3', 'XNH2', 'XNHCHO', 'XNHCH3',
'XNHNO', 'XNHNH2', 'XNHOH', 'XNO2', 'OXNNH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH',
'XNH', 'XNCN', 'XNCH3', 'XNNH2', 'XNOH', 'XOH', 'XOCHCH2', 'HC(O)XO',
'XOC(OH)O', 'XOCH3', 'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XOOH', 'XCN', 'XCH',
'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3', 'XCCH2OH', 'XCNO', 'XCNH2', 'XCOH',
'XCHCO', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3', 'OXCNH2',
'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH', 'CH3XCO', 'CH3CH2XCO',
'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH', 'XCH2NH2',
'XCH2OH', 'CH3XCHOH', 'XCCO', 'XCCCH2', 'XCCH2', 'XCNH', 'XCH2', 'XCHCHCH2',
'XCHCHO', 'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2',
'NH2XCNH2', 'XCHOH', 'CH3XCOH', 'XCH', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3',
'XCCH2OH', 'XCNO', 'XCNH2', 'XCOH', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3',
'XCCH2OH', 'XCNO', 'XCNH2', 'XCOH', 'XCHCO', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2',
'XCHCH2', 'XCHCHCH3', 'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO',
'XCOOH', 'CH3XCO', 'CH3CH2XCO', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2',
'XCHCHCH3', 'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH',
'CH3XCO', 'CH3CH2XCO', 'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3',
'CH3XCHOH', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCH2CH2CH3', 'XCH2CH2OH',
'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCCO',
'XCCCH2', 'XCCH2', 'XCNH', 'XCCO', 'XCCCH2', 'XCCH2', 'XCNH', 'XCH2',
'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3', 'XCHNH2',
'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3',
'CH3XCOH', 'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH',
'CH3XCOH', 'XNO', 'XNCNH', 'XNCO', 'XNCH2', 'XNNH', 'XNNCH3', 'XNH2', 'XNHCHO',
'XNHCH3', 'XNHNO', 'XNHNH2', 'XNHOH', 'XNO2', 'OXNNH', 'HXNO', 'CH3NXNOH',
'CH3XNNOH', 'XNH', 'XNCN', 'XNCH3', 'XNNH2', 'XNOH', 'XNO', 'XNCNH', 'XNCO',
'XNCH2', 'XNNH', 'XNNCH3', 'XNCNH', 'XNCO', 'XNCH2', 'XNNH', 'XNNCH3', 'XNH2',
'XNHCHO', 'XNHCH3', 'XNHNO', 'XNHNH2', 'XNHOH', 'XNO2', 'OXNNH', 'HXNO',
'CH3NXNOH', 'CH3XNNOH', 'XNHCHO', 'XNHCH3', 'XNHNO', 'XNHNH2', 'XNHOH', 'XNO2',
'OXNNH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH', 'XNH', 'XNCN', 'XNCH3', 'XNNH2',
'XNOH', 'XNCN', 'XNCH3', 'XNNH2', 'XNOH', 'XOH', 'XOCHCH2', 'HC(O)XO',
'XOC(OH)O', 'XOCH3', 'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XOOH', 'XOH', 'XOCHCH2',
'HC(O)XO', 'XOC(OH)O', 'XOCH3', 'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XOOH',
'XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCH3', 'XOCH2CH3', 'XOCH2OH', 'XONH2',
'XOOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 60,
    label = "CX",
    group=
"""
1 * X u0 {2,[S,D,T,Q]}
2 C  ux {1,[S,D,T,Q]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-8.059, -4.93, -2.911, -1.575, -0.025, 0.787, 1.674], 'J/(mol*K)'),
        H298=(-324.771, 'kJ/mol'),
        S298=(-169.93, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCN', 'XCH', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3',
'XCCH2OH', 'XCNO', 'XCNH2', 'XCOH', 'XCHCO', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2',
'XCHCH2', 'XCHCHCH3', 'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO',
'XCOOH', 'CH3XCO', 'CH3CH2XCO', 'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3',
'CH3XCHCH3', 'CH3XCHOH', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCCO', 'XCCCH2',
'XCCH2', 'XCNH', 'XCH2', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH',
'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH',
'XCH', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3', 'XCCH2OH', 'XCNO', 'XCNH2',
'XCOH', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3', 'XCCH2OH', 'XCNO', 'XCNH2',
'XCOH', 'XCHCO', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3',
'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH', 'CH3XCO',
'CH3CH2XCO', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3', 'OXCNH2',
'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH', 'CH3XCO', 'CH3CH2XCO',
'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH', 'XCH2NH2',
'XCH2OH', 'CH3XCHOH', 'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3',
'CH3XCHOH', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCCO', 'XCCCH2', 'XCCH2', 'XCNH',
'XCCO', 'XCCCH2', 'XCCH2', 'XCNH', 'XCH2', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3',
'CH3XCOH', 'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH',
'CH3XCOH', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3',
'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 61,
    label = "C#XR",
    group=
"""
1 * X u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-9.096, -5.869, -3.758, -2.343, -0.685, 0.216, 1.352], 'J/(mol*K)'),
        H298=(-509.334, 'kJ/mol'),
        S298=(-177.185, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3', 'XCCH2OH',
'XCNO', 'XCNH2', 'XCOH', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3', 'XCCH2OH',
'XCNO', 'XCNH2', 'XCOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 62,
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
        Cpdata=([-12.369, -9.501, -7.368, -5.786, -3.722, -2.526, -1.16], 'J/(mol*K)'),
        H298=(-534.575, 'kJ/mol'),
        S298=(-183.565, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCHCH2', 'XCCHO']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 63,
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
        Cpdata=([-10.246, -6.744, -4.142, -2.248, 0.153, 1.544, 3.315], 'J/(mol*K)'),
        H298=(-586.617, 'kJ/mol'),
        S298=(-180.123, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCH3', 'XCCH2CH3', 'XCCH2OH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 64,
    label = "C#XN",
    group=
"""
1 * X u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 N  u0 p1 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-4.802, -2.782, -1.842, -1.37, -1.0, -0.884, -0.705], 'J/(mol*K)'),
        H298=(-380.005, 'kJ/mol'),
        S298=(-161.835, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCNO', 'XCNH2']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 65,
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
        Cpdata=([-2.481, 1.519, 3.59, 4.636, 5.376, 5.591, 6.114], 'J/(mol*K)'),
        H298=(-431.789, 'kJ/mol'),
        S298=(-187.544, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 66,
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
        Cpdata=([-7.788, -4.718, -2.682, -1.337, 0.163, 0.885, 1.572], 'J/(mol*K)'),
        H298=(-257.443, 'kJ/mol'),
        S298=(-166.062, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCO', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3',
'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH', 'CH3XCO',
'CH3CH2XCO', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3', 'OXCNH2',
'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH', 'CH3XCO', 'CH3CH2XCO']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 67,
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
        Cpdata=([-7.024, -3.455, -0.964, 0.723, 2.651, 3.602, 4.504], 'J/(mol*K)'),
        H298=(-280.708, 'kJ/mol'),
        S298=(-182.514, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 68,
    label = "C-XRN",
    group=
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {4,D} {3,S}
3 N  u0  p1 c0 {2,S}
4 R!H  u0  p[1,2,3] c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-6.998, -4.5, -2.956, -1.997, -1.04, -0.66, -0.35], 'J/(mol*K)'),
        H298=(-248.886, 'kJ/mol'),
        S298=(-153.59, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['OXCNH2', 'NH2XCNH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 69,
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
        Cpdata=([-8.453, -5.685, -3.912, -2.763, -1.518, -0.942, -0.403], 'J/(mol*K)'),
        H298=(-246.762, 'kJ/mol'),
        S298=(-151.565, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHNH', 'OHXCNH', 'NH2XCNH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 70,
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
        Cpdata=([-6.986, -4.107, -2.256, -1.046, 0.308, 0.975, 1.636], 'J/(mol*K)'),
        H298=(-240.5, 'kJ/mol'),
        S298=(-163.124, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHO', 'XCOOH', 'CH3XCO', 'CH3CH2XCO']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 71,
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
        Cpdata=([-9.256, -5.928, -3.602, -1.974, 0.039, 1.155, 2.354], 'J/(mol*K)'),
        H298=(-220.933, 'kJ/mol'),
        S298=(-177.467, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH',
'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3',
'CH3XCHCH3', 'CH3XCHOH', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 72,
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
        Cpdata=([-7.927, -4.391, -1.968, -0.293, 1.756, 2.884, 4.113], 'J/(mol*K)'),
        H298=(-223.034, 'kJ/mol'),
        S298=(-192.287, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 73,
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
        Cpdata=([-11.501, -8.834, -6.746, -5.175, -3.118, -1.943, -0.697], 'J/(mol*K)'),
        H298=(-223.941, 'kJ/mol'),
        S298=(-143.176, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2NH2']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 74,
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
        Cpdata=([-11.456, -8.317, -6.115, -4.578, -2.676, -1.621, -0.516], 'J/(mol*K)'),
        H298=(-214.176, 'kJ/mol'),
        S298=(-157.564, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2OH', 'CH3XCHOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 75,
    label = "C=X(=R)",
    group=
"""
1 * X  u0  p0 c0 {2,D}
2 C   u0  p0 c0 {1,D} {3,D}
3 R!H u0  px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-6.678, -3.549, -1.767, -0.677, 0.517, 1.114, 1.713], 'J/(mol*K)'),
        H298=(-342.815, 'kJ/mol'),
        S298=(-170.526, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCO', 'XCCCH2', 'XCCH2', 'XCNH', 'XCCO', 'XCCCH2', 'XCCH2',
'XCNH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 76,
    label = "C=X(=C)",
    group=
"""
1 * X u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 C  u0  p0 c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-6.756, -3.436, -1.616, -0.523, 0.693, 1.335, 2.065], 'J/(mol*K)'),
        H298=(-400.072, 'kJ/mol'),
        S298=(-171.763, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCO', 'XCCCH2', 'XCCH2']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 77,
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
        Cpdata=([-6.443, -3.888, -2.219, -1.141, -0.01, 0.449, 0.658], 'J/(mol*K)'),
        H298=(-171.042, 'kJ/mol'),
        S298=(-166.816, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCNH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 78,
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
        Cpdata=([-6.999, -4.068, -2.302, -1.166, 0.157, 0.879, 1.725], 'J/(mol*K)'),
        H298=(-334.667, 'kJ/mol'),
        S298=(-164.206, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH',
'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH',
'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3', 'XCHNH2',
'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 79,
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
        Cpdata=([-7.502, -4.231, -2.08, -0.611, 1.184, 2.171, 3.256], 'J/(mol*K)'),
        H298=(-357.316, 'kJ/mol'),
        S298=(-179.047, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCHCH2', 'XCHCHO']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 80,
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
        Cpdata=([-6.536, -3.596, -1.716, -0.454, 1.074, 1.948, 3.03], 'J/(mol*K)'),
        H298=(-376.057, 'kJ/mol'),
        S298=(-179.041, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 81,
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
        Cpdata=([-5.314, -3.237, -2.228, -1.679, -1.161, -0.928, -0.62], 'J/(mol*K)'),
        H298=(-273.721, 'kJ/mol'),
        S298=(-144.277, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHNH2', 'OHXCNH2', 'NH2XCNH2']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 82,
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
        Cpdata=([-8.363, -5.498, -3.838, -2.79, -1.538, -0.826, -0.079], 'J/(mol*K)'),
        H298=(-305.179, 'kJ/mol'),
        S298=(-146.569, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHOH', 'CH3XCOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 83,
    label = "NX",
    group=
"""
1 * X u0 {2,[S,D,T]}
2 N  u0 {1,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.842, -0.733, 0.996, 2.001, 3.013, 3.5, 4.107], 'J/(mol*K)'),
        H298=(-190.59, 'kJ/mol'),
        S298=(-168.016, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNO', 'XNCNH', 'XNCO', 'XNCH2', 'XNNH', 'XNNCH3', 'XNH2',
'XNHCHO', 'XNHCH3', 'XNHNO', 'XNHNH2', 'XNHOH', 'XNO2', 'OXNNH', 'HXNO',
'CH3NXNOH', 'CH3XNNOH', 'XNH', 'XNCN', 'XNCH3', 'XNNH2', 'XNOH', 'XNO', 'XNCNH',
'XNCO', 'XNCH2', 'XNNH', 'XNNCH3', 'XNCNH', 'XNCO', 'XNCH2', 'XNNH', 'XNNCH3',
'XNH2', 'XNHCHO', 'XNHCH3', 'XNHNO', 'XNHNH2', 'XNHOH', 'XNO2', 'OXNNH', 'HXNO',
'CH3NXNOH', 'CH3XNNOH', 'XNHCHO', 'XNHCH3', 'XNHNO', 'XNHNH2', 'XNHOH', 'XNO2',
'OXNNH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH', 'XNH', 'XNCN', 'XNCH3', 'XNNH2',
'XNOH', 'XNCN', 'XNCH3', 'XNNH2', 'XNOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 84,
    label = "N-XR",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 R!H u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-5.452, -2.951, -1.585, -0.791, 0.014, 0.399, 0.862], 'J/(mol*K)'),
        H298=(-164.777, 'kJ/mol'),
        S298=(-161.628, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNO', 'XNCNH', 'XNCO', 'XNCH2', 'XNNH', 'XNNCH3', 'XNCNH',
'XNCO', 'XNCH2', 'XNNH', 'XNNCH3']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 85,
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
        Cpdata=([-8.735, -7.168, -6.454, -6.084, -5.664, -5.378, -4.904], 'J/(mol*K)'),
        H298=(-203.369, 'kJ/mol'),
        S298=(-145.417, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNCNH', 'XNCO']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 86,
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
        Cpdata=([-1.707, 1.64, 3.521, 4.671, 5.896, 6.505, 7.246], 'J/(mol*K)'),
        H298=(-187.169, 'kJ/mol'),
        S298=(-180.636, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNCH2']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 87,
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
        Cpdata=([-3.854, -0.981, 0.698, 1.7, 2.689, 3.114, 3.559], 'J/(mol*K)'),
        H298=(-121.56, 'kJ/mol'),
        S298=(-164.071, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNNH', 'XNNCH3']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 88,
    label = "N-XR2",
    group=
"""
1 * X u0 p0 c0 {2,[S,D]}
2 N u0 px cx {1,[S,D]} {3,[S,D]} {4,[S,D]}
3 R!H u0 px cx {2,[S,D]}
4 R u0 px c0 {2,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.012, 1.065, 2.884, 4.006, 5.238, 5.88, 6.65], 'J/(mol*K)'),
        H298=(-167.045, 'kJ/mol'),
        S298=(-170.982, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNH2', 'XNHCHO', 'XNHCH3', 'XNHNO', 'XNHNH2', 'XNHOH', 'XNO2',
'OXNNH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH', 'XNHCHO', 'XNHCH3', 'XNHNO', 'XNHNH2',
'XNHOH', 'XNO2', 'OXNNH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 89,
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
        Cpdata=([-4.328, -0.938, 1.222, 2.693, 4.463, 5.437, 6.648], 'J/(mol*K)'),
        H298=(-279.769, 'kJ/mol'),
        S298=(-216.907, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHCHO']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 90,
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
        Cpdata=([3.994, 8.661, 12.118, 14.767, 18.588, 21.339, 25.873], 'J/(mol*K)'),
        H298=(-349.285, 'kJ/mol'),
        S298=(-167.995, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHCH3']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 91,
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
        Cpdata=([2.584, 5.55, 7.122, 7.922, 8.483, 8.562, 8.462], 'J/(mol*K)'),
        H298=(-193.938, 'kJ/mol'),
        S298=(-189.56, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHNO']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 92,
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
        Cpdata=([-1.185, 2.056, 4.018, 5.261, 6.661, 7.372, 8.062], 'J/(mol*K)'),
        H298=(-142.183, 'kJ/mol'),
        S298=(-188.5, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHNH2']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 93,
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
        Cpdata=([-0.228, 3.377, 5.253, 6.315, 7.409, 7.934, 8.402], 'J/(mol*K)'),
        H298=(-145.504, 'kJ/mol'),
        S298=(-189.451, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 94,
    label = "N[+]-XR[-]R",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p0 c+1 {1,S} {3,S} {4,D}
3 R!H  u0 p[1,2,3] c-1 {2,S}
4 R!H  u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.078, 1.553, 2.933, 3.648, 4.201, 4.335, 4.328], 'J/(mol*K)'),
        H298=(-137.214, 'kJ/mol'),
        S298=(-163.298, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNO2', 'OXNNH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 95,
    label = "N[+]=XR[-]R",
    group=
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p0 c+1 {1,D} {3,S} {4,S}
3 R!H  u0 p[1,2,3] c-1 {2,S}
4 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-4.586, -2.627, -1.537, -0.917, -0.317, -0.061, 0.133], 'J/(mol*K)'),
        H298=(-88.105, 'kJ/mol'),
        S298=(-143.039, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['HXNO', 'CH3NXNOH', 'CH3XNNOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 96,
    label = "N=XR",
    group=
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-5.16, -1.482, 0.319, 1.196, 1.832, 2.031, 2.398], 'J/(mol*K)'),
        H298=(-272.432, 'kJ/mol'),
        S298=(-168.194, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNH', 'XNCN', 'XNCH3', 'XNNH2', 'XNOH', 'XNCN', 'XNCH3',
'XNNH2', 'XNOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 97,
    label = "N=XC#R",
    group=
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 C  u0 p0 c0 {2,S} {4,T}
4 R!H u0 px c0 {3,T}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-15.304, -12.918, -11.895, -11.386, -10.762, -10.276, -9.457], 'J/(mol*K)'),
        H298=(-258.062, 'kJ/mol'),
        S298=(-142.031, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNCN']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 98,
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
        Cpdata=([-1.701, 1.153, 2.807, 3.883, 5.154, 5.877, 6.86], 'J/(mol*K)'),
        H298=(-336.733, 'kJ/mol'),
        S298=(-176.565, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNCH3']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 99,
    label = "N=XN",
    group=
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 N  u0 p1 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.988, 7.107, 8.778, 9.2, 8.654, 7.878, 7.118], 'J/(mol*K)'),
        H298=(-210.104, 'kJ/mol'),
        S298=(-174.51, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNNH2']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 100,
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
        Cpdata=([0.702, 4.715, 6.511, 7.217, 7.378, 7.177, 7.067], 'J/(mol*K)'),
        H298=(-246.238, 'kJ/mol'),
        S298=(-178.708, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 101,
    label = "OX",
    group=
"""
1 * X u0 {2,[S,D]}
2 O  ux {1,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.311, -1.586, -0.606, 0.006, 0.702, 1.083, 1.573], 'J/(mol*K)'),
        H298=(-150.355, 'kJ/mol'),
        S298=(-156.463, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOH', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCH3', 'XOCH2CH3',
'XOCH2OH', 'XONH2', 'XOOH', 'XOH', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCH3',
'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XOOH', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O',
'XOCH3', 'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XOOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 102,
    label = "O-XR",
    group=
"""
1 * X u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.029, -1.323, -0.36, 0.241, 0.923, 1.297, 1.782], 'J/(mol*K)'),
        H298=(-149.633, 'kJ/mol'),
        S298=(-157.296, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOH', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCH3', 'XOCH2CH3',
'XOCH2OH', 'XONH2', 'XOOH', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCH3',
'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XOOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 103,
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
        Cpdata=([2.854, 5.052, 6.224, 6.899, 7.592, 7.912, 8.196], 'J/(mol*K)'),
        H298=(-169.226, 'kJ/mol'),
        S298=(-194.234, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOCHCH2', 'HC(O)XO', 'XOC(OH)O']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 104,
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
        Cpdata=([-6.75, -5.939, -5.225, -4.586, -3.596, -2.889, -1.766], 'J/(mol*K)'),
        H298=(-163.2, 'kJ/mol'),
        S298=(-147.3, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOCH3', 'XOCH2CH3', 'XOCH2OH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 105,
    label = "O-XN",
    group=
"""
1 * X u0 p0 c0 {3,S}
2 N  u0 p1 c0 {3,S}
3 O  u0 p2 c0 {1,S} {2,S}

""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.084, -4.161, -2.544, -1.628, -0.739, -0.36, -0.052], 'J/(mol*K)'),
        H298=(-91.643, 'kJ/mol'),
        S298=(-134.71, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XONH2']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 106,
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
        Cpdata=([1.892, 3.068, 3.066, 2.708, 1.879, 1.245, 0.455], 'J/(mol*K)'),
        H298=(-89.371, 'kJ/mol'),
        S298=(-120.712, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOOH']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 107,
    label = "RXvdW",
    group=
"""
1 * X u0
2 R  u0
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.739, -1.476, -0.766, -0.337, 0.132, 0.372, 0.613], 'J/(mol*K)'),
        H298=(-55.017, 'kJ/mol'),
        S298=(-130.866, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CHCHX', 'CHCCH3X', 'NCOHX', 'CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X',
'CH2NHX', 'CH2COX', 'CH2OX', 'OC(OH)OHX', 'CH3CHOX', 'HCOOHX', 'OCHNH2X',
'CH4X', 'CH3CH3X', 'CH3CH2CH3X', 'CH3CH2OHX', 'CH3NH2X', 'CH3OHX', 'CH3OCH3X',
'CH3OCH2OHX', 'H2C(OH)OHX', 'OCNHX', 'NHCNHX', 'NH3X', 'NH2NH2X', 'NH2NCH3CH3X',
'H2NOHX', 'ONNH2X', 'ONNCH3CH3X', 'ONOHX', 'H2OX', 'HOOHX', 'CHCHX', 'CHCCH3X',
'NCOHX', 'CHCHX', 'CHCCH3X', 'NCOHX', 'CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X',
'CH2NHX', 'CH2COX', 'CH2OX', 'OC(OH)OHX', 'CH3CHOX', 'HCOOHX', 'OCHNH2X',
'CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X', 'CH2NHX', 'CH2COX', 'CH2OX', 'OC(OH)OHX',
'CH3CHOX', 'HCOOHX', 'OCHNH2X', 'CH4X', 'CH3CH3X', 'CH3CH2CH3X', 'CH3CH2OHX',
'CH3NH2X', 'CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX', 'H2C(OH)OHX', 'CH3CH3X',
'CH3CH2CH3X', 'CH3CH2OHX', 'CH3NH2X', 'CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX',
'H2C(OH)OHX', 'OCNHX', 'NHCNHX', 'NH3X', 'NH2NH2X', 'NH2NCH3CH3X', 'H2NOHX',
'NH2NH2X', 'NH2NCH3CH3X', 'H2NOHX', 'ONNH2X', 'ONNCH3CH3X', 'ONOHX', 'ONNH2X',
'ONNCH3CH3X', 'ONOHX', 'ONNH2X', 'ONNCH3CH3X', 'ONOHX', 'H2OX', 'HOOHX',
'HOOHX']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 108,
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
        Cpdata=([-6.11, -5.831, -5.665, -5.52, -5.191, -4.827, -4.063], 'J/(mol*K)'),
        H298=(-47.085, 'kJ/mol'),
        S298=(-120.514, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CHCHX', 'CHCCH3X', 'NCOHX', 'CHCHX', 'CHCCH3X', 'NCOHX']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 109,
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
        Cpdata=([-8.706, -8.504, -8.378, -8.256, -7.93, -7.499, -6.43], 'J/(mol*K)'),
        H298=(-52.462, 'kJ/mol'),
        S298=(-119.645, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CHCHX', 'CHCCH3X']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 110,
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
        Cpdata=([-0.92, -0.483, -0.241, -0.047, 0.285, 0.517, 0.671], 'J/(mol*K)'),
        H298=(-36.329, 'kJ/mol'),
        S298=(-122.254, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['NCOHX']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 111,
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
        Cpdata=([-2.288, -0.929, -0.172, 0.264, 0.683, 0.849, 0.944], 'J/(mol*K)'),
        H298=(-50.097, 'kJ/mol'),
        S298=(-131.72, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X', 'CH2NHX', 'CH2COX', 'CH2OX',
'OC(OH)OHX', 'CH3CHOX', 'HCOOHX', 'OCHNH2X', 'CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X',
'CH2NHX', 'CH2COX', 'CH2OX', 'OC(OH)OHX', 'CH3CHOX', 'HCOOHX', 'OCHNH2X']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 112,
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
        Cpdata=([-0.886, 0.725, 1.607, 2.108, 2.582, 2.761, 2.858], 'J/(mol*K)'),
        H298=(-81.979, 'kJ/mol'),
        S298=(-143.863, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 113,
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
        Cpdata=([-5.016, -1.971, -0.438, 0.26, 0.613, 0.552, 0.294], 'J/(mol*K)'),
        H298=(-41.944, 'kJ/mol'),
        S298=(-135.288, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH2NHX']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 114,
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
        Cpdata=([-2.534, -1.583, -1.016, -0.658, -0.255, -0.058, 0.095], 'J/(mol*K)'),
        H298=(-35.515, 'kJ/mol'),
        S298=(-125.054, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH2COX', 'CH2OX', 'OC(OH)OHX', 'CH3CHOX', 'HCOOHX', 'OCHNH2X']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 115,
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
        Cpdata=([-0.601, 0.513, 1.09, 1.41, 1.719, 1.853, 1.964], 'J/(mol*K)'),
        H298=(-51.612, 'kJ/mol'),
        S298=(-132.892, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH4X', 'CH3CH3X', 'CH3CH2CH3X', 'CH3CH2OHX', 'CH3NH2X',
'CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX', 'H2C(OH)OHX', 'CH3CH3X', 'CH3CH2CH3X',
'CH3CH2OHX', 'CH3NH2X', 'CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX', 'H2C(OH)OHX']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 116,
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
        Cpdata=([0.725, 1.62, 2.083, 2.358, 2.656, 2.793, 2.88], 'J/(mol*K)'),
        H298=(-49.146, 'kJ/mol'),
        S298=(-137.338, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH3CH3X', 'CH3CH2CH3X', 'CH3CH2OHX']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 117,
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
        Cpdata=([-7.383, -5.169, -3.741, -2.808, -1.758, -1.219, -0.61], 'J/(mol*K)'),
        H298=(-108.02, 'kJ/mol'),
        S298=(-141.215, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH3NH2X']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 118,
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
        Cpdata=([0.121, 1.214, 1.71, 1.937, 2.093, 2.135, 2.153], 'J/(mol*K)'),
        H298=(-41.365, 'kJ/mol'),
        S298=(-139.363, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX', 'H2C(OH)OHX']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 119,
    label = "(N=C)X",
    group=
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,D} {4,S}
3 C  u0 p0 c0 {2,D} {5,D}
4 R  u0 p0 c0 {2,S}
5 R!H u0 p[1,2] c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.774, -1.224, -0.874, -0.625, -0.309, -0.136, 0.025], 'J/(mol*K)'),
        H298=(-50.28, 'kJ/mol'),
        S298=(-122.197, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['OCNHX', 'NHCNHX']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 120,
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
        Cpdata=([-5.59, -3.27, -1.885, -1.016, -0.058, 0.418, 0.889], 'J/(mol*K)'),
        H298=(-83.564, 'kJ/mol'),
        S298=(-141.62, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['NH3X', 'NH2NH2X', 'NH2NCH3CH3X', 'H2NOHX', 'NH2NH2X',
'NH2NCH3CH3X', 'H2NOHX']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 121,
    label = "(NN)X",
    group=
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-6.538, -4.302, -2.97, -2.136, -1.218, -0.762, -0.308], 'J/(mol*K)'),
        H298=(-101.101, 'kJ/mol'),
        S298=(-150.696, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['NH2NH2X', 'NH2NCH3CH3X']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 122,
    label = "(NO)X",
    group=
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-4.993, -3.162, -2.106, -1.465, -0.78, -0.451, -0.141], 'J/(mol*K)'),
        H298=(-53.372, 'kJ/mol'),
        S298=(-132.089, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['H2NOHX']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 123,
    label = "(OR)X",
    group=
"""
1 * X u0 p0 c0
2 O u0 p2 c0 {3,D}
3 R!H u0 p1 c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.606, -2.304, -1.526, -1.013, -0.385, -0.041, 0.25], 'J/(mol*K)'),
        H298=(-70.962, 'kJ/mol'),
        S298=(-141.385, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['ONNH2X', 'ONNCH3CH3X', 'ONOHX', 'ONNH2X', 'ONNCH3CH3X',
'ONOHX', 'ONNH2X', 'ONNCH3CH3X', 'ONOHX']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 124,
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
        Cpdata=([-3.606, -2.304, -1.526, -1.013, -0.385, -0.041, 0.25], 'J/(mol*K)'),
        H298=(-70.962, 'kJ/mol'),
        S298=(-141.385, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['ONNH2X', 'ONNCH3CH3X', 'ONOHX', 'ONNH2X', 'ONNCH3CH3X',
'ONOHX']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 125,
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
        Cpdata=([-2.633, -1.581, -1.003, -0.651, -0.264, -0.073, 0.086], 'J/(mol*K)'),
        H298=(-78.738, 'kJ/mol'),
        S298=(-139.884, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['ONNH2X', 'ONNCH3CH3X']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 126,
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
        Cpdata=([-5.553, -3.751, -2.573, -1.736, -0.625, 0.024, 0.577], 'J/(mol*K)'),
        H298=(-55.41, 'kJ/mol'),
        S298=(-144.387, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['ONOHX']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 127,
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
        Cpdata=([-2.956, -1.698, -1.056, -0.677, -0.23, 0.029, 0.27], 'J/(mol*K)'),
        H298=(-22.787, 'kJ/mol'),
        S298=(-104.314, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['H2OX', 'HOOHX', 'HOOHX']""",
longDesc=u"""
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 128,
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
        Cpdata=([-1.999, -1.084, -0.634, -0.367, -0.023, 0.197, 0.393], 'J/(mol*K)'),
        H298=(-27.657, 'kJ/mol'),
        S298=(-110.352, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['HOOHX']""",
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
        L3: (N=C)X
        L3: (NR3)X
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
