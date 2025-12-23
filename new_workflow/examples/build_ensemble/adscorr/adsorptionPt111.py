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
        Cpdata=([3.517, 7.712, 10.239, 11.76, 13.248, 13.831, 14.211], 'J/(mol*K)'),
        H298=(-191.523, 'kJ/mol'),
        S298=(-186.544, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCXCCH2', 'XCXCH2', 'XCXCHCH3', 'XCXCCH3', 'XCXC', 'XCH2XCCH2',
'XCH2XCH2', 'CH3XCHXCH2', 'XCH2XCH', 'XCH2XCOH', 'XCHXCHCH3', 'XCHXCCH3',
'XCHXC', 'XCHXCO', 'XCHXCH', 'XCH2XNH', 'XCH2XN', 'XCHXN', 'NHXCXNH', 'XNHXCO',
'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XCH2XO', 'XOXCNH',
'XCHXO', 'XCH2XNH', 'XCH2XN', 'XCHXN', 'NHXCXNH', 'XNHXCO', 'XNXCO', 'XNXCNH',
'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XNHXNH', 'CH3XNXNOH', 'XNHXN',
'XNXNCH3', 'XOXNH', 'XOXNO', 'XOXO', 'XCXCCH2', 'XCXCH2', 'XCXCHCH3', 'XCXCCH3',
'XCXC', 'XCH2XCCH2', 'XCH2XCH2', 'CH3XCHXCH2', 'XCH2XCH', 'XCH2XCOH',
'XCHXCHCH3', 'XCHXCCH3', 'XCHXC', 'XCHXCO', 'XCHXCH', 'XCH2XNH', 'XCH2XN',
'XCHXN', 'NHXCXNH', 'XNHXCO', 'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN',
'XNXCOH', 'XCH2XO', 'XOXCNH', 'XCHXO', 'XCH2XNH', 'XCH2XN', 'XCHXN', 'NHXCXNH',
'XNHXCO', 'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XNHXNH',
'CH3XNXNOH', 'XNHXN', 'XNXNCH3', 'XOXNH', 'XOXNO', 'XOXO', 'XCXCCH2', 'XCXCH2',
'XCXCHCH3', 'XCXCCH3', 'XCXC', 'XCH2XCCH2', 'XCH2XCH2', 'CH3XCHXCH2', 'XCH2XCH',
'XCH2XCOH', 'XCHXCHCH3', 'XCHXCCH3', 'XCHXC', 'XCHXCO', 'XCHXCH', 'XCXCCH2',
'XCXCCH2', 'XCXCH2', 'XCXCHCH3', 'XCXCH2', 'XCXCHCH3', 'XCXCCH3', 'XCXCCH3',
'XCXC', 'XCXC', 'XCH2XCCH2', 'XCH2XCCH2', 'XCH2XCH2', 'CH3XCHXCH2', 'XCH2XCH2',
'CH3XCHXCH2', 'XCH2XCH', 'XCH2XCOH', 'XCHXCHCH3', 'XCH2XCH', 'XCH2XCOH',
'XCHXCHCH3', 'XCHXCCH3', 'XCHXCCH3', 'XCHXC', 'XCHXC', 'XCHXCO', 'XCHXCO',
'XCHXCH', 'XCHXCH', 'XCH2XNH', 'XCH2XN', 'XCHXN', 'NHXCXNH', 'XNHXCO', 'XNXCO',
'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XCH2XNH', 'XCH2XNH',
'XCH2XN', 'XCH2XN', 'XCHXN', 'XCHXN', 'NHXCXNH', 'XNHXCO', 'NHXCXNH', 'XNHXCO',
'XNXCO', 'XNXCNH', 'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXNH', 'OHXCXNH',
'XCHXN', 'XNXCOH', 'XCHXN', 'XNXCOH', 'XCH2XO', 'XOXCNH', 'XCHXO', 'XCH2XO',
'XCH2XO', 'XOXCNH', 'XOXCNH', 'XCHXO', 'XCHXO', 'XCH2XNH', 'XCH2XN', 'XCHXN',
'NHXCXNH', 'XNHXCO', 'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH',
'XCH2XNH', 'XCH2XNH', 'XCH2XN', 'XCH2XN', 'XCHXN', 'XCHXN', 'NHXCXNH', 'XNHXCO',
'NHXCXNH', 'XNHXCO', 'XNXCO', 'XNXCNH', 'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH',
'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XCHXN', 'XNXCOH', 'XNHXNH',
'CH3XNXNOH', 'XNHXN', 'XNXNCH3', 'XNHXNH', 'CH3XNXNOH', 'XNHXNH', 'CH3XNXNOH',
'XNHXN', 'XNXNCH3', 'XNHXN', 'XNXNCH3', 'XOXNH', 'XOXNO', 'XOXNH', 'XOXNH',
'XOXNO', 'XOXNO', 'XOXO', 'XOXO']""",
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
        H298=(-327.663, 'kJ/mol'),
        S298=(-195.899, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCXCCH2', 'XCXCH2', 'XCXCHCH3', 'XCXCCH3', 'XCXC', 'XCH2XCCH2',
'XCH2XCH2', 'CH3XCHXCH2', 'XCH2XCH', 'XCH2XCOH', 'XCHXCHCH3', 'XCHXCCH3',
'XCHXC', 'XCHXCO', 'XCHXCH', 'XCXCCH2', 'XCXCH2', 'XCXCHCH3', 'XCXCCH3', 'XCXC',
'XCH2XCCH2', 'XCH2XCH2', 'CH3XCHXCH2', 'XCH2XCH', 'XCH2XCOH', 'XCHXCHCH3',
'XCHXCCH3', 'XCHXC', 'XCHXCO', 'XCHXCH', 'XCXCCH2', 'XCXCCH2', 'XCXCH2',
'XCXCHCH3', 'XCXCH2', 'XCXCHCH3', 'XCXCCH3', 'XCXCCH3', 'XCXC', 'XCXC',
'XCH2XCCH2', 'XCH2XCCH2', 'XCH2XCH2', 'CH3XCHXCH2', 'XCH2XCH2', 'CH3XCHXCH2',
'XCH2XCH', 'XCH2XCOH', 'XCHXCHCH3', 'XCH2XCH', 'XCH2XCOH', 'XCHXCHCH3',
'XCHXCCH3', 'XCHXCCH3', 'XCHXC', 'XCHXC', 'XCHXCO', 'XCHXCO', 'XCHXCH',
'XCHXCH']""",
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
        H298=(-413.118, 'kJ/mol'),
        S298=(-204.353, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCXCCH2', 'XCXCCH2', 'XCXCCH2', 'XCXCCH2']""",
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
        H298=(-426.244, 'kJ/mol'),
        S298=(-201.882, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCXCH2', 'XCXCHCH3', 'XCXCH2', 'XCXCHCH3', 'XCXCH2',
'XCXCHCH3', 'XCXCH2', 'XCXCHCH3']""",
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
        H298=(-470.676, 'kJ/mol'),
        S298=(-152.622, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCXCCH3', 'XCXCCH3', 'XCXCCH3', 'XCXCCH3']""",
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
        H298=(-584.061, 'kJ/mol'),
        S298=(-172.682, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCXC', 'XCXC', 'XCXC', 'XCXC']""",
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
        H298=(-171.456, 'kJ/mol'),
        S298=(-191.92, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XCCH2', 'XCH2XCCH2', 'XCH2XCCH2', 'XCH2XCCH2']""",
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
        H298=(-132.497, 'kJ/mol'),
        S298=(-192.345, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XCH2', 'CH3XCHXCH2', 'XCH2XCH2', 'CH3XCHXCH2', 'XCH2XCH2',
'CH3XCHXCH2', 'XCH2XCH2', 'CH3XCHXCH2']""",
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
        H298=(-319.935, 'kJ/mol'),
        S298=(-214.968, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XCH', 'XCH2XCOH', 'XCHXCHCH3', 'XCH2XCH', 'XCH2XCOH',
'XCHXCHCH3', 'XCH2XCH', 'XCH2XCOH', 'XCHXCHCH3', 'XCH2XCH', 'XCH2XCOH',
'XCHXCHCH3']""",
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
        H298=(-219.045, 'kJ/mol'),
        S298=(-194.29, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXCCH3', 'XCHXCCH3', 'XCHXCCH3', 'XCHXCCH3']""",
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
        H298=(-420.548, 'kJ/mol'),
        S298=(-193.307, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXC', 'XCHXC', 'XCHXC', 'XCHXC']""",
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
        H298=(-348.148, 'kJ/mol'),
        S298=(-211.081, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXCO', 'XCHXCO', 'XCHXCO', 'XCHXCO']""",
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
        H298=(-210.61, 'kJ/mol'),
        S298=(-184.879, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXCH', 'XCHXCH', 'XCHXCH', 'XCHXCH']""",
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
        H298=(-141.715, 'kJ/mol'),
        S298=(-186.3, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XNH', 'XCH2XN', 'XCHXN', 'NHXCXNH', 'XNHXCO', 'XNXCO',
'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XCH2XNH', 'XCH2XN', 'XCHXN',
'NHXCXNH', 'XNHXCO', 'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH',
'XCH2XNH', 'XCH2XNH', 'XCH2XN', 'XCH2XN', 'XCHXN', 'XCHXN', 'NHXCXNH', 'XNHXCO',
'NHXCXNH', 'XNHXCO', 'XNXCO', 'XNXCNH', 'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH',
'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XCHXN', 'XNXCOH']""",
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
        H298=(-88.85, 'kJ/mol'),
        S298=(-197.829, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XNH', 'XCH2XNH', 'XCH2XNH', 'XCH2XNH']""",
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
        H298=(-189.473, 'kJ/mol'),
        S298=(-193.314, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XN', 'XCH2XN', 'XCH2XN', 'XCH2XN']""",
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
        H298=(-61.792, 'kJ/mol'),
        S298=(-171.411, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXN', 'XCHXN', 'XCHXN', 'XCHXN']""",
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
        H298=(-65.599, 'kJ/mol'),
        S298=(-183.708, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['NHXCXNH', 'XNHXCO', 'NHXCXNH', 'XNHXCO', 'NHXCXNH', 'XNHXCO',
'NHXCXNH', 'XNHXCO']""",
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
        H298=(-192.682, 'kJ/mol'),
        S298=(-188.758, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNXCO', 'XNXCNH', 'XNXCO', 'XNXCNH', 'XNXCO', 'XNXCNH',
'XNXCO', 'XNXCNH']""",
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
        H298=(-274.258, 'kJ/mol'),
        S298=(-195.23, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXNH', 'OHXCXNH', 'XCHXNH', 'OHXCXNH', 'XCHXNH', 'OHXCXNH',
'XCHXNH', 'OHXCXNH']""",
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
        H298=(-76.836, 'kJ/mol'),
        S298=(-175.675, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXN', 'XNXCOH', 'XCHXN', 'XNXCOH', 'XCHXN', 'XNXCOH',
'XCHXN', 'XNXCOH']""",
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
        H298=(-74.968, 'kJ/mol'),
        S298=(-170.773, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XO', 'XOXCNH', 'XCHXO', 'XCH2XO', 'XOXCNH', 'XCHXO',
'XCH2XO', 'XCH2XO', 'XOXCNH', 'XOXCNH', 'XCHXO', 'XCHXO']""",
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
        H298=(-36.167, 'kJ/mol'),
        S298=(-170.273, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XO', 'XCH2XO', 'XCH2XO', 'XCH2XO']""",
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
        H298=(15.247, 'kJ/mol'),
        S298=(-174.316, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOXCNH', 'XOXCNH', 'XOXCNH', 'XOXCNH']""",
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
        H298=(-203.985, 'kJ/mol'),
        S298=(-167.729, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXO', 'XCHXO', 'XCHXO', 'XCHXO']""",
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
        H298=(-141.715, 'kJ/mol'),
        S298=(-186.3, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XNH', 'XCH2XN', 'XCHXN', 'NHXCXNH', 'XNHXCO', 'XNXCO',
'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XCH2XNH', 'XCH2XN', 'XCHXN',
'NHXCXNH', 'XNHXCO', 'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH',
'XCH2XNH', 'XCH2XNH', 'XCH2XN', 'XCH2XN', 'XCHXN', 'XCHXN', 'NHXCXNH', 'XNHXCO',
'NHXCXNH', 'XNHXCO', 'XNXCO', 'XNXCNH', 'XNXCO', 'XNXCNH', 'XCHXNH', 'OHXCXNH',
'XCHXNH', 'OHXCXNH', 'XCHXN', 'XNXCOH', 'XCHXN', 'XNXCOH']""",
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
        H298=(-88.85, 'kJ/mol'),
        S298=(-197.829, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XNH', 'XCH2XNH', 'XCH2XNH', 'XCH2XNH']""",
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
        H298=(-189.473, 'kJ/mol'),
        S298=(-193.314, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2XN', 'XCH2XN', 'XCH2XN', 'XCH2XN']""",
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
        H298=(-61.792, 'kJ/mol'),
        S298=(-171.411, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXN', 'XCHXN', 'XCHXN', 'XCHXN']""",
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
        H298=(-65.599, 'kJ/mol'),
        S298=(-183.708, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['NHXCXNH', 'XNHXCO', 'NHXCXNH', 'XNHXCO', 'NHXCXNH', 'XNHXCO',
'NHXCXNH', 'XNHXCO']""",
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
        H298=(-192.682, 'kJ/mol'),
        S298=(-188.758, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNXCO', 'XNXCNH', 'XNXCO', 'XNXCNH', 'XNXCO', 'XNXCNH',
'XNXCO', 'XNXCNH']""",
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
        H298=(-274.258, 'kJ/mol'),
        S298=(-195.23, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXNH', 'OHXCXNH', 'XCHXNH', 'OHXCXNH', 'XCHXNH', 'OHXCXNH',
'XCHXNH', 'OHXCXNH']""",
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
        H298=(-76.836, 'kJ/mol'),
        S298=(-175.675, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHXN', 'XNXCOH', 'XCHXN', 'XNXCOH', 'XCHXN', 'XNXCOH',
'XCHXN', 'XNXCOH']""",
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
        H298=(-106.998, 'kJ/mol'),
        S298=(-177.885, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHXNH', 'CH3XNXNOH', 'XNHXN', 'XNXNCH3', 'XNHXNH',
'CH3XNXNOH', 'XNHXN', 'XNXNCH3', 'XNHXNH', 'CH3XNXNOH', 'XNHXNH', 'CH3XNXNOH',
'XNHXN', 'XNXNCH3', 'XNHXN', 'XNXNCH3']""",
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
        Cpdata=([8.625, 11.667, 13.041, 13.56, 13.614, 13.356, 12.881], 'J/(mol*K)'),
        H298=(-69.379, 'kJ/mol'),
        S298=(-159.55, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHXNH', 'CH3XNXNOH', 'XNHXNH', 'CH3XNXNOH', 'XNHXNH',
'CH3XNXNOH', 'XNHXNH', 'CH3XNXNOH']""",
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
        H298=(-144.617, 'kJ/mol'),
        S298=(-196.22, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHXN', 'XNXNCH3', 'XNHXN', 'XNXNCH3', 'XNHXN', 'XNXNCH3',
'XNHXN', 'XNXNCH3']""",
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
        H298=(-118.059, 'kJ/mol'),
        S298=(-164.124, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOXNH', 'XOXNO', 'XOXNH', 'XOXNO', 'XOXNH', 'XOXNH', 'XOXNO',
'XOXNO']""",
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
        H298=(-107.575, 'kJ/mol'),
        S298=(-186.753, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOXNH', 'XOXNH', 'XOXNH', 'XOXNH']""",
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
        H298=(-128.542, 'kJ/mol'),
        S298=(-141.494, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOXNO', 'XOXNO', 'XOXNO', 'XOXNO']""",
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
        H298=(-51.985, 'kJ/mol'),
        S298=(-176.349, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOXO', 'XOXO', 'XOXO', 'XOXO']""",
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
        H298=(-421.19, 'kJ/mol'),
        S298=(-205.343, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCH2XC', 'XCCH2XCH2', 'XCHCH2XC', 'XCHCHXC', 'XCCHXCH2',
'XCH2CH2XCH2', 'XCHCHXCH2', 'XCHCXCH', 'XCHCXC', 'XCHCH2XCH2', 'XCHCH2XCH',
'XCHCHXCH', 'XCHCHXO', 'XOC(O)XO', 'H2C(XO)XO', 'XCCH2XC', 'XCCH2XCH2',
'XCHCH2XC', 'XCHCHXC', 'XCCHXCH2', 'XCH2CH2XCH2', 'XCHCHXCH2', 'XCHCXCH',
'XCHCXC', 'XCHCH2XCH2', 'XCHCH2XCH', 'XCHCHXCH', 'XCHCHXO', 'XOC(O)XO',
'H2C(XO)XO', 'XCCH2XC', 'XCCH2XCH2', 'XCHCH2XC', 'XCHCHXC', 'XCCHXCH2',
'XCH2CH2XCH2', 'XCHCHXCH2', 'XCHCXCH', 'XCHCXC', 'XCHCH2XCH2', 'XCHCH2XCH',
'XCHCHXCH', 'XCCH2XC', 'XCCH2XC', 'XCCH2XCH2', 'XCCH2XCH2', 'XCHCH2XC',
'XCHCH2XC', 'XCHCHXC', 'XCHCHXC', 'XCCHXCH2', 'XCCHXCH2', 'XCH2CH2XCH2',
'XCH2CH2XCH2', 'XCHCHXCH2', 'XCHCHXCH2', 'XCHCXCH', 'XCHCXCH', 'XCHCXC',
'XCHCXC', 'XCHCH2XCH2', 'XCHCH2XCH2', 'XCHCH2XCH', 'XCHCH2XCH', 'XCHCHXCH',
'XCHCHXCH', 'XCHCHXO', 'XCHCHXO', 'XCHCHXO', 'XOC(O)XO', 'H2C(XO)XO',
'XOC(O)XO', 'H2C(XO)XO', 'XOC(O)XO', 'H2C(XO)XO']""",
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
        H298=(-446.276, 'kJ/mol'),
        S298=(-209.129, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCH2XC', 'XCCH2XCH2', 'XCHCH2XC', 'XCHCHXC', 'XCCHXCH2',
'XCH2CH2XCH2', 'XCHCHXCH2', 'XCHCXCH', 'XCHCXC', 'XCHCH2XCH2', 'XCHCH2XCH',
'XCHCHXCH', 'XCCH2XC', 'XCCH2XCH2', 'XCHCH2XC', 'XCHCHXC', 'XCCHXCH2',
'XCH2CH2XCH2', 'XCHCHXCH2', 'XCHCXCH', 'XCHCXC', 'XCHCH2XCH2', 'XCHCH2XCH',
'XCHCHXCH', 'XCCH2XC', 'XCCH2XC', 'XCCH2XCH2', 'XCCH2XCH2', 'XCHCH2XC',
'XCHCH2XC', 'XCHCHXC', 'XCHCHXC', 'XCCHXCH2', 'XCCHXCH2', 'XCH2CH2XCH2',
'XCH2CH2XCH2', 'XCHCHXCH2', 'XCHCHXCH2', 'XCHCXCH', 'XCHCXCH', 'XCHCXC',
'XCHCXC', 'XCHCH2XCH2', 'XCHCH2XCH2', 'XCHCH2XCH', 'XCHCH2XCH', 'XCHCHXCH',
'XCHCHXCH']""",
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
        H298=(-644.002, 'kJ/mol'),
        S298=(-243.646, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCH2XC', 'XCCH2XC', 'XCCH2XC', 'XCCH2XC']""",
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
        H298=(-468.664, 'kJ/mol'),
        S298=(-200.61, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCH2XCH2', 'XCCH2XCH2', 'XCCH2XCH2', 'XCCH2XCH2']""",
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
        H298=(-439.455, 'kJ/mol'),
        S298=(-222.487, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCH2XC', 'XCHCH2XC', 'XCHCH2XC', 'XCHCH2XC']""",
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
        H298=(-375.168, 'kJ/mol'),
        S298=(-202.293, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCHXC', 'XCHCHXC', 'XCHCHXC', 'XCHCHXC']""",
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
        H298=(-525.397, 'kJ/mol'),
        S298=(-217.923, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCHXCH2', 'XCCHXCH2', 'XCCHXCH2', 'XCCHXCH2']""",
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
        H298=(-399.23, 'kJ/mol'),
        S298=(-209.34, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2CH2XCH2', 'XCH2CH2XCH2', 'XCH2CH2XCH2', 'XCH2CH2XCH2']""",
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
        H298=(-418.213, 'kJ/mol'),
        S298=(-227.783, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCHXCH2', 'XCHCHXCH2', 'XCHCHXCH2', 'XCHCHXCH2']""",
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
        H298=(-343.623, 'kJ/mol'),
        S298=(-196.347, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCXCH', 'XCHCXCH', 'XCHCXCH', 'XCHCXCH']""",
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
        H298=(-397.697, 'kJ/mol'),
        S298=(-188.069, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCXC', 'XCHCXC', 'XCHCXC', 'XCHCXC']""",
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
        H298=(-527.304, 'kJ/mol'),
        S298=(-196.129, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCH2XCH2', 'XCHCH2XCH2', 'XCHCH2XCH2', 'XCHCH2XCH2']""",
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
        H298=(-221.487, 'kJ/mol'),
        S298=(-203.938, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCH2XCH', 'XCHCH2XCH', 'XCHCH2XCH', 'XCHCH2XCH']""",
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
        H298=(-595.067, 'kJ/mol'),
        S298=(-200.988, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCHXCH', 'XCHCHXCH', 'XCHCHXCH', 'XCHCHXCH']""",
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
        H298=(-406.357, 'kJ/mol'),
        S298=(-211.148, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCHXO', 'XCHCHXO', 'XCHCHXO', 'XCHCHXO']""",
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
        H298=(-406.357, 'kJ/mol'),
        S298=(-211.148, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCHXO', 'XCHCHXO', 'XCHCHXO', 'XCHCHXO']""",
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
        H298=(-278.091, 'kJ/mol'),
        S298=(-179.723, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOC(O)XO', 'H2C(XO)XO', 'XOC(O)XO', 'H2C(XO)XO', 'XOC(O)XO',
'H2C(XO)XO', 'XOC(O)XO', 'H2C(XO)XO']""",
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
        H298=(-278.091, 'kJ/mol'),
        S298=(-179.723, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOC(O)XO', 'H2C(XO)XO', 'XOC(O)XO', 'H2C(XO)XO', 'XOC(O)XO',
'H2C(XO)XO', 'XOC(O)XO', 'H2C(XO)XO']""",
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
        Cpdata=([1.825, 4.8, 6.627, 7.794, 9.104, 9.781, 10.55], 'J/(mol*K)'),
        H298=(-270.088, 'kJ/mol'),
        S298=(-167.765, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCN', 'XCH', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3',
'XCCH2OH', 'XCNO', 'XCNH2', 'XCOH', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2',
'XCHCHCH3', 'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH',
'CH3XCO', 'XCCHO', 'CH3CH2XCO', 'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3',
'CH3XCHCH3', 'CH3XCHOH', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCCO', 'XCCCH2',
'XCCH2', 'XCNH', 'XCH2', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH',
'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH',
'XNO', 'XNCNH', 'XNCO', 'XNCH2', 'XNNH', 'XNNCH3', 'XNH2', 'XNHCHO', 'XNHCH3',
'XNHNO', 'XNHNH2', 'XNHOH', 'XNO2', 'OXNNH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH',
'XNH', 'XNCN', 'XNCH3', 'XNNH2', 'XNOH', 'XOH', 'XOCHCH2', 'HC(O)XO',
'XOC(OH)O', 'XOCH3', 'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XOOH', 'XCN', 'XCH',
'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3', 'XCCH2OH', 'XCNO', 'XCNH2', 'XCOH',
'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3', 'OXCNH2', 'NH2XCNH',
'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH', 'CH3XCO', 'XCCHO', 'CH3CH2XCO',
'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH', 'XCH2NH2',
'XCH2OH', 'CH3XCHOH', 'XCCO', 'XCCCH2', 'XCCH2', 'XCNH', 'XCH2', 'XCHCHCH2',
'XCHCHO', 'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2',
'NH2XCNH2', 'XCHOH', 'CH3XCOH', 'XNO', 'XNCNH', 'XNCO', 'XNCH2', 'XNNH',
'XNNCH3', 'XNH2', 'XNHCHO', 'XNHCH3', 'XNHNO', 'XNHNH2', 'XNHOH', 'XNO2',
'OXNNH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH', 'XNH', 'XNCN', 'XNCH3', 'XNNH2',
'XNOH', 'XOH', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCH3', 'XOCH2CH3', 'XOCH2OH',
'XONH2', 'XOOH', 'XCN', 'XCN', 'XCH', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3',
'XCCH2OH', 'XCNO', 'XCNH2', 'XCOH', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2',
'XCHCHCH3', 'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH',
'CH3XCO', 'XCCHO', 'CH3CH2XCO', 'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3',
'CH3XCHCH3', 'CH3XCHOH', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCCO', 'XCCCH2',
'XCCH2', 'XCNH', 'XCH2', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH',
'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH',
'XCH', 'XCH', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3', 'XCCH2OH', 'XCNO',
'XCNH2', 'XCOH', 'XCCHCH2', 'XCCHO', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3',
'XCCH2OH', 'XCCH3', 'XCCH2CH3', 'XCCH2OH', 'XCNO', 'XCNH2', 'XCNO', 'XCNH2',
'XCOH', 'XCOH', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3',
'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH', 'CH3XCO',
'XCCHO', 'CH3CH2XCO', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3',
'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3', 'OXCNH2', 'NH2XCNH',
'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH',
'XCHO', 'XCOOH', 'CH3XCO', 'XCCHO', 'CH3CH2XCO', 'XCHO', 'XCOOH', 'CH3XCO',
'XCCHO', 'CH3CH2XCO', 'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3',
'CH3XCHOH', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCH2CH2CH3', 'XCH2CH2OH',
'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH', 'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3',
'CH3XCHCH3', 'CH3XCHOH', 'XCH2NH2', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCH2OH',
'CH3XCHOH', 'XCCO', 'XCCCH2', 'XCCH2', 'XCNH', 'XCCO', 'XCCCH2', 'XCCH2',
'XCCO', 'XCCCH2', 'XCCH2', 'XCNH', 'XCNH', 'XCH2', 'XCH2', 'XCHCHCH2', 'XCHCHO',
'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2',
'XCHOH', 'CH3XCOH', 'XCHCHCH2', 'XCHCHO', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3',
'CH3XCOH', 'XCHCH2CH3', 'XCHCH3', 'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3',
'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH',
'CH3XCOH', 'XCHOH', 'CH3XCOH', 'XNO', 'XNCNH', 'XNCO', 'XNCH2', 'XNNH',
'XNNCH3', 'XNH2', 'XNHCHO', 'XNHCH3', 'XNHNO', 'XNHNH2', 'XNHOH', 'XNO2',
'OXNNH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH', 'XNH', 'XNCN', 'XNCH3', 'XNNH2',
'XNOH', 'XNO', 'XNO', 'XNCNH', 'XNCO', 'XNCH2', 'XNNH', 'XNNCH3', 'XNCNH',
'XNCO', 'XNCNH', 'XNCO', 'XNCH2', 'XNCH2', 'XNNH', 'XNNCH3', 'XNNH', 'XNNCH3',
'XNH2', 'XNH2', 'XNHCHO', 'XNHCH3', 'XNHNO', 'XNHNH2', 'XNHOH', 'XNO2', 'OXNNH',
'HXNO', 'CH3NXNOH', 'CH3XNNOH', 'XNHCHO', 'XNHCHO', 'XNHCH3', 'XNHCH3', 'XNHNO',
'XNHNO', 'XNHNH2', 'XNHNH2', 'XNHOH', 'XNHOH', 'XNO2', 'OXNNH', 'XNO2', 'OXNNH',
'HXNO', 'CH3NXNOH', 'CH3XNNOH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH', 'XNH', 'XNH',
'XNCN', 'XNCH3', 'XNNH2', 'XNOH', 'XNCN', 'XNCN', 'XNCH3', 'XNCH3', 'XNNH2',
'XNNH2', 'XNOH', 'XNOH', 'XOH', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCH3',
'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XOOH', 'XOH', 'XOH', 'XOCHCH2', 'HC(O)XO',
'XOC(OH)O', 'XOCH3', 'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XOOH', 'XOCHCH2',
'HC(O)XO', 'XOC(OH)O', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCH3', 'XOCH2CH3',
'XOCH2OH', 'XOCH3', 'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XONH2', 'XOOH', 'XOOH']""",
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
        Cpdata=([0.241, 3.349, 5.352, 6.678, 8.217, 9.024, 9.906], 'J/(mol*K)'),
        H298=(-328.216, 'kJ/mol'),
        S298=(-169.612, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCN', 'XCN', 'XCH', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3',
'XCCH2OH', 'XCNO', 'XCNH2', 'XCOH', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2',
'XCHCHCH3', 'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH',
'CH3XCO', 'XCCHO', 'CH3CH2XCO', 'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3',
'CH3XCHCH3', 'CH3XCHOH', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCCO', 'XCCCH2',
'XCCH2', 'XCNH', 'XCH2', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH',
'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH',
'XCN', 'XCN', 'XCH', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3', 'XCCH2OH', 'XCNO',
'XCNH2', 'XCOH', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3',
'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH', 'CH3XCO',
'XCCHO', 'CH3CH2XCO', 'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3',
'CH3XCHOH', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCCO', 'XCCCH2', 'XCCH2', 'XCNH',
'XCH2', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3',
'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH', 'XCH', 'XCH', 'XCCHCH2',
'XCCHO', 'XCCH3', 'XCCH2CH3', 'XCCH2OH', 'XCNO', 'XCNH2', 'XCOH', 'XCCHCH2',
'XCCHO', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3', 'XCCH2OH', 'XCCH3',
'XCCH2CH3', 'XCCH2OH', 'XCNO', 'XCNH2', 'XCNO', 'XCNH2', 'XCOH', 'XCOH',
'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3', 'OXCNH2', 'NH2XCNH',
'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH', 'CH3XCO', 'XCCHO', 'CH3CH2XCO',
'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3', 'CH2XCCH3', 'CH2XCOH',
'XCHCCH2', 'XCHCH2', 'XCHCHCH3', 'OXCNH2', 'NH2XCNH', 'OXCNH2', 'NH2XCNH',
'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH',
'CH3XCO', 'XCCHO', 'CH3CH2XCO', 'XCHO', 'XCOOH', 'CH3XCO', 'XCCHO', 'CH3CH2XCO',
'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH', 'XCH2NH2',
'XCH2OH', 'CH3XCHOH', 'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3',
'CH3XCHOH', 'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH',
'XCH2NH2', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCH2OH', 'CH3XCHOH', 'XCCO',
'XCCCH2', 'XCCH2', 'XCNH', 'XCCO', 'XCCCH2', 'XCCH2', 'XCCO', 'XCCCH2', 'XCCH2',
'XCNH', 'XCNH', 'XCH2', 'XCH2', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH',
'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH',
'XCHCHCH2', 'XCHCHO', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3',
'XCHCH3', 'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2',
'NH2XCNH2', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH', 'XCHOH',
'CH3XCOH']""",
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
        Cpdata=([-1.352, 2.042, 4.247, 5.715, 7.423, 8.345, 9.498], 'J/(mol*K)'),
        H298=(-512.804, 'kJ/mol'),
        S298=(-175.086, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH', 'XCH', 'XCCHCH2', 'XCCHO', 'XCCH3', 'XCCH2CH3',
'XCCH2OH', 'XCNO', 'XCNH2', 'XCOH', 'XCH', 'XCH', 'XCCHCH2', 'XCCHO', 'XCCH3',
'XCCH2CH3', 'XCCH2OH', 'XCNO', 'XCNH2', 'XCOH', 'XCCHCH2', 'XCCHO', 'XCCHCH2',
'XCCHO', 'XCCH3', 'XCCH2CH3', 'XCCH2OH', 'XCCH3', 'XCCH2CH3', 'XCCH2OH', 'XCNO',
'XCNH2', 'XCNO', 'XCNH2', 'XCOH', 'XCOH']""",
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
        H298=(-532.096, 'kJ/mol'),
        S298=(-183.565, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCHCH2', 'XCCHO', 'XCCHCH2', 'XCCHO', 'XCCHCH2', 'XCCHO',
'XCCHCH2', 'XCCHO']""",
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
        H298=(-584.026, 'kJ/mol'),
        S298=(-174.235, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCH3', 'XCCH2CH3', 'XCCH2OH', 'XCCH3', 'XCCH2CH3', 'XCCH2OH',
'XCCH3', 'XCCH2CH3', 'XCCH2OH', 'XCCH3', 'XCCH2CH3', 'XCCH2OH']""",
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
        H298=(-377.526, 'kJ/mol'),
        S298=(-161.835, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCNO', 'XCNH2', 'XCNO', 'XCNH2', 'XCNO', 'XCNH2', 'XCNO',
'XCNH2']""",
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
        H298=(-429.31, 'kJ/mol'),
        S298=(-187.544, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCOH', 'XCOH', 'XCOH', 'XCOH']""",
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
        H298=(-272.139, 'kJ/mol'),
        S298=(-166.429, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3',
'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH', 'CH3XCO',
'XCCHO', 'CH3CH2XCO', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3',
'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHO', 'XCOOH', 'CH3XCO',
'XCCHO', 'CH3CH2XCO', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3',
'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3', 'OXCNH2', 'NH2XCNH',
'OXCNH2', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH',
'XCHO', 'XCOOH', 'CH3XCO', 'XCCHO', 'CH3CH2XCO', 'XCHO', 'XCOOH', 'CH3XCO',
'XCCHO', 'CH3CH2XCO']""",
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
        H298=(-278.229, 'kJ/mol'),
        S298=(-182.514, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3',
'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3', 'CH2XCCH3', 'CH2XCOH',
'XCHCCH2', 'XCHCH2', 'XCHCHCH3', 'CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2',
'XCHCHCH3']""",
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
        H298=(-246.407, 'kJ/mol'),
        S298=(-153.59, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['OXCNH2', 'NH2XCNH', 'OXCNH2', 'NH2XCNH', 'OXCNH2', 'NH2XCNH',
'OXCNH2', 'NH2XCNH']""",
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
        H298=(-244.283, 'kJ/mol'),
        S298=(-151.565, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH',
'XCHNH', 'OHXCNH', 'NH2XCNH', 'XCHNH', 'OHXCNH', 'NH2XCNH']""",
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
        H298=(-293.055, 'kJ/mol'),
        S298=(-164.4, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHO', 'XCOOH', 'CH3XCO', 'XCCHO', 'CH3CH2XCO', 'XCHO',
'XCOOH', 'CH3XCO', 'XCCHO', 'CH3CH2XCO', 'XCHO', 'XCOOH', 'CH3XCO', 'XCCHO',
'CH3CH2XCO', 'XCHO', 'XCOOH', 'CH3XCO', 'XCCHO', 'CH3CH2XCO']""",
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
        H298=(-218.454, 'kJ/mol'),
        S298=(-177.467, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH',
'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3',
'CH3XCHCH3', 'CH3XCHOH', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH', 'XCH2CH2CH3',
'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH', 'XCH2CH2CH3', 'XCH2CH2OH',
'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH', 'XCH2NH2', 'XCH2NH2', 'XCH2OH', 'CH3XCHOH',
'XCH2OH', 'CH3XCHOH']""",
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
        H298=(-220.555, 'kJ/mol'),
        S298=(-192.287, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH',
'XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH', 'XCH2CH2CH3',
'XCH2CH2OH', 'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH', 'XCH2CH2CH3', 'XCH2CH2OH',
'XCH2CH3', 'CH3XCHCH3', 'CH3XCHOH']""",
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
        H298=(-221.462, 'kJ/mol'),
        S298=(-143.176, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2NH2', 'XCH2NH2', 'XCH2NH2', 'XCH2NH2']""",
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
        H298=(-211.697, 'kJ/mol'),
        S298=(-157.564, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2OH', 'CH3XCHOH', 'XCH2OH', 'CH3XCHOH', 'XCH2OH',
'CH3XCHOH', 'XCH2OH', 'CH3XCHOH']""",
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
        H298=(-340.336, 'kJ/mol'),
        S298=(-170.526, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCO', 'XCCCH2', 'XCCH2', 'XCNH', 'XCCO', 'XCCCH2', 'XCCH2',
'XCNH', 'XCCO', 'XCCCH2', 'XCCH2', 'XCCO', 'XCCCH2', 'XCCH2', 'XCNH', 'XCNH']""",
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
        H298=(-397.593, 'kJ/mol'),
        S298=(-171.763, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCCO', 'XCCCH2', 'XCCH2', 'XCCO', 'XCCCH2', 'XCCH2', 'XCCO',
'XCCCH2', 'XCCH2', 'XCCO', 'XCCCH2', 'XCCH2']""",
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
        H298=(-168.564, 'kJ/mol'),
        S298=(-166.816, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCNH', 'XCNH', 'XCNH', 'XCNH']""",
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
        Cpdata=([1.051, 4.147, 6.018, 7.218, 8.606, 9.358, 10.236], 'J/(mol*K)'),
        H298=(-334.767, 'kJ/mol'),
        S298=(-164.709, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCH2', 'XCH2', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH',
'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH',
'XCH2', 'XCH2', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3',
'XCHCH3', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH', 'XCHCHCH2',
'XCHCHO', 'XCHCHCH2', 'XCHCHO', 'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3',
'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2',
'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHOH', 'CH3XCOH', 'XCHOH', 'CH3XCOH']""",
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
        H298=(-354.837, 'kJ/mol'),
        S298=(-179.047, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHCHCH2', 'XCHCHO', 'XCHCHCH2', 'XCHCHO', 'XCHCHCH2',
'XCHCHO', 'XCHCHCH2', 'XCHCHO']""",
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
        H298=(-373.578, 'kJ/mol'),
        S298=(-179.041, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3', 'CH3XCCH3',
'CH3XCOH', 'XCHCH2CH3', 'XCHCH3', 'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3',
'CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3']""",
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
        H298=(-271.242, 'kJ/mol'),
        S298=(-144.277, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHNH2', 'OHXCNH2',
'NH2XCNH2', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2', 'XCHNH2', 'OHXCNH2', 'NH2XCNH2']""",
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
        H298=(-302.7, 'kJ/mol'),
        S298=(-146.569, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XCHOH', 'CH3XCOH', 'XCHOH', 'CH3XCOH', 'XCHOH', 'CH3XCOH',
'XCHOH', 'CH3XCOH']""",
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
        Cpdata=([4.307, 7.457, 9.215, 10.238, 11.27, 11.766, 12.379], 'J/(mol*K)'),
        H298=(-188.893, 'kJ/mol'),
        S298=(-168.135, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNO', 'XNCNH', 'XNCO', 'XNCH2', 'XNNH', 'XNNCH3', 'XNH2',
'XNHCHO', 'XNHCH3', 'XNHNO', 'XNHNH2', 'XNHOH', 'XNO2', 'OXNNH', 'HXNO',
'CH3NXNOH', 'CH3XNNOH', 'XNH', 'XNCN', 'XNCH3', 'XNNH2', 'XNOH', 'XNO', 'XNCNH',
'XNCO', 'XNCH2', 'XNNH', 'XNNCH3', 'XNH2', 'XNHCHO', 'XNHCH3', 'XNHNO',
'XNHNH2', 'XNHOH', 'XNO2', 'OXNNH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH', 'XNH',
'XNCN', 'XNCH3', 'XNNH2', 'XNOH', 'XNO', 'XNO', 'XNCNH', 'XNCO', 'XNCH2',
'XNNH', 'XNNCH3', 'XNCNH', 'XNCO', 'XNCNH', 'XNCO', 'XNCH2', 'XNCH2', 'XNNH',
'XNNCH3', 'XNNH', 'XNNCH3', 'XNH2', 'XNH2', 'XNHCHO', 'XNHCH3', 'XNHNO',
'XNHNH2', 'XNHOH', 'XNO2', 'OXNNH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH', 'XNHCHO',
'XNHCHO', 'XNHCH3', 'XNHCH3', 'XNHNO', 'XNHNO', 'XNHNH2', 'XNHNH2', 'XNHOH',
'XNHOH', 'XNO2', 'OXNNH', 'XNO2', 'OXNNH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH',
'HXNO', 'CH3NXNOH', 'CH3XNNOH', 'XNH', 'XNH', 'XNCN', 'XNCH3', 'XNNH2', 'XNOH',
'XNCN', 'XNCN', 'XNCH3', 'XNCH3', 'XNNH2', 'XNNH2', 'XNOH', 'XNOH']""",
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
        Cpdata=([2.8, 5.347, 6.74, 7.547, 8.348, 8.717, 9.135], 'J/(mol*K)'),
        H298=(-160.108, 'kJ/mol'),
        S298=(-163.05, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNO', 'XNO', 'XNCNH', 'XNCO', 'XNCH2', 'XNNH', 'XNNCH3', 'XNO',
'XNO', 'XNCNH', 'XNCO', 'XNCH2', 'XNNH', 'XNNCH3', 'XNCNH', 'XNCO', 'XNCNH',
'XNCO', 'XNCH2', 'XNCH2', 'XNNH', 'XNNCH3', 'XNNH', 'XNNCH3']""",
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
        H298=(-200.89, 'kJ/mol'),
        S298=(-145.417, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNCNH', 'XNCO', 'XNCNH', 'XNCO', 'XNCNH', 'XNCO', 'XNCNH',
'XNCO']""",
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
        H298=(-184.69, 'kJ/mol'),
        S298=(-180.636, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNCH2', 'XNCH2', 'XNCH2', 'XNCH2']""",
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
        H298=(-119.081, 'kJ/mol'),
        S298=(-164.071, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNNH', 'XNNCH3', 'XNNH', 'XNNCH3', 'XNNH', 'XNNCH3', 'XNNH',
'XNNCH3']""",
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
        Cpdata=([5.844, 9.082, 11.002, 12.19, 13.49, 14.164, 14.965], 'J/(mol*K)'),
        H298=(-166.478, 'kJ/mol'),
        S298=(-171.136, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNH2', 'XNH2', 'XNHCHO', 'XNHCH3', 'XNHNO', 'XNHNH2', 'XNHOH',
'XNO2', 'OXNNH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH', 'XNH2', 'XNH2', 'XNHCHO',
'XNHCH3', 'XNHNO', 'XNHNH2', 'XNHOH', 'XNO2', 'OXNNH', 'HXNO', 'CH3NXNOH',
'CH3XNNOH', 'XNHCHO', 'XNHCHO', 'XNHCH3', 'XNHCH3', 'XNHNO', 'XNHNO', 'XNHNH2',
'XNHNH2', 'XNHOH', 'XNHOH', 'XNO2', 'OXNNH', 'XNO2', 'OXNNH', 'HXNO',
'CH3NXNOH', 'CH3XNNOH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH']""",
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
        H298=(-277.29, 'kJ/mol'),
        S298=(-216.907, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHCHO', 'XNHCHO', 'XNHCHO', 'XNHCHO']""",
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
        H298=(-346.806, 'kJ/mol'),
        S298=(-167.995, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHCH3', 'XNHCH3', 'XNHCH3', 'XNHCH3']""",
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
        H298=(-191.459, 'kJ/mol'),
        S298=(-189.56, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHNO', 'XNHNO', 'XNHNO', 'XNHNO']""",
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
        H298=(-139.705, 'kJ/mol'),
        S298=(-188.5, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHNH2', 'XNHNH2', 'XNHNH2', 'XNHNH2']""",
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
        H298=(-143.025, 'kJ/mol'),
        S298=(-189.451, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNHOH', 'XNHOH', 'XNHOH', 'XNHOH']""",
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
        H298=(-134.735, 'kJ/mol'),
        S298=(-163.298, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNO2', 'OXNNH', 'XNO2', 'OXNNH', 'XNO2', 'OXNNH', 'XNO2',
'OXNNH']""",
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
        H298=(-85.626, 'kJ/mol'),
        S298=(-143.039, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['HXNO', 'CH3NXNOH', 'CH3XNNOH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH',
'HXNO', 'CH3NXNOH', 'CH3XNNOH', 'HXNO', 'CH3NXNOH', 'CH3XNNOH']""",
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
        Cpdata=([1.689, 5.635, 7.648, 8.685, 9.527, 9.838, 10.313], 'J/(mol*K)'),
        H298=(-277.671, 'kJ/mol'),
        S298=(-168.387, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNH', 'XNH', 'XNCN', 'XNCH3', 'XNNH2', 'XNOH', 'XNH', 'XNH',
'XNCN', 'XNCH3', 'XNNH2', 'XNOH', 'XNCN', 'XNCN', 'XNCH3', 'XNCH3', 'XNNH2',
'XNNH2', 'XNOH', 'XNOH']""",
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
        H298=(-255.583, 'kJ/mol'),
        S298=(-142.031, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNCN', 'XNCN', 'XNCN', 'XNCN']""",
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
        H298=(-334.254, 'kJ/mol'),
        S298=(-176.565, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNCH3', 'XNCH3', 'XNCH3', 'XNCH3']""",
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
        H298=(-207.626, 'kJ/mol'),
        S298=(-174.51, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNNH2', 'XNNH2', 'XNNH2', 'XNNH2']""",
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
        H298=(-243.759, 'kJ/mol'),
        S298=(-178.708, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XNOH', 'XNOH', 'XNOH', 'XNOH']""",
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
        Cpdata=([4.744, 6.48, 7.463, 8.075, 8.768, 9.15, 9.656], 'J/(mol*K)'),
        H298=(-147.748, 'kJ/mol'),
        S298=(-156.676, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOH', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCH3', 'XOCH2CH3',
'XOCH2OH', 'XONH2', 'XOOH', 'XOH', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCH3',
'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XOOH', 'XOH', 'XOH', 'XOCHCH2', 'HC(O)XO',
'XOC(OH)O', 'XOCH3', 'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XOOH', 'XOCHCH2',
'HC(O)XO', 'XOC(OH)O', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCH3', 'XOCH2CH3',
'XOCH2OH', 'XOCH3', 'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XONH2', 'XOOH', 'XOOH']""",
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
        Cpdata=([4.429, 6.188, 7.189, 7.815, 8.523, 8.912, 9.424], 'J/(mol*K)'),
        H298=(-148.569, 'kJ/mol'),
        S298=(-155.727, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOH', 'XOH', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCH3',
'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XOOH', 'XOH', 'XOH', 'XOCHCH2', 'HC(O)XO',
'XOC(OH)O', 'XOCH3', 'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XOOH', 'XOCHCH2',
'HC(O)XO', 'XOC(OH)O', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCH3', 'XOCH2CH3',
'XOCH2OH', 'XOCH3', 'XOCH2CH3', 'XOCH2OH', 'XONH2', 'XONH2', 'XOOH', 'XOOH']""",
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
        H298=(-166.747, 'kJ/mol'),
        S298=(-194.234, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCHCH2', 'HC(O)XO',
'XOC(OH)O', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O', 'XOCHCH2', 'HC(O)XO', 'XOC(OH)O']""",
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
        H298=(-158.708, 'kJ/mol'),
        S298=(-149.812, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOCH3', 'XOCH2CH3', 'XOCH2OH', 'XOCH3', 'XOCH2CH3', 'XOCH2OH',
'XOCH3', 'XOCH2CH3', 'XOCH2OH', 'XOCH3', 'XOCH2CH3', 'XOCH2OH']""",
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
        H298=(-89.164, 'kJ/mol'),
        S298=(-134.71, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XONH2', 'XONH2', 'XONH2', 'XONH2']""",
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
        H298=(-86.892, 'kJ/mol'),
        S298=(-120.712, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['XOOH', 'XOOH', 'XOOH', 'XOOH']""",
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
        Cpdata=([5.604, 6.861, 7.568, 7.996, 8.464, 8.704, 8.944], 'J/(mol*K)'),
        H298=(-52.076, 'kJ/mol'),
        S298=(-130.005, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CHCHX', 'CHCCH3X', 'NCOHX', 'CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X',
'CH2NHX', 'CH2COX', 'CH2OX', 'OC(OH)OHX', 'CH3CHOX', 'HCOOHX', 'CH4X',
'CH3CH3X', 'CH3CH2CH3X', 'CH3CH2OHX', 'CH3NH2X', 'CH3OHX', 'CH3OCH3X',
'CH3OCH2OHX', 'H2C(OH)OHX', 'OCNHX', 'NHCNHX', 'NH3X', 'OCHNH2X', 'NH2NH2X',
'NH2NCH3CH3X', 'H2NOHX', 'ONNH2X', 'ONNCH3CH3X', 'ONOHX', 'H2OX', 'HOOHX',
'CHCHX', 'CHCCH3X', 'NCOHX', 'CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X', 'CH2NHX',
'CH2COX', 'CH2OX', 'OC(OH)OHX', 'CH3CHOX', 'HCOOHX', 'CH4X', 'CH3CH3X',
'CH3CH2CH3X', 'CH3CH2OHX', 'CH3NH2X', 'CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX',
'H2C(OH)OHX', 'OCNHX', 'NHCNHX', 'NH3X', 'OCHNH2X', 'NH2NH2X', 'NH2NCH3CH3X',
'H2NOHX', 'ONNH2X', 'ONNCH3CH3X', 'ONOHX', 'H2OX', 'HOOHX', 'CHCHX', 'CHCCH3X',
'NCOHX', 'CHCHX', 'CHCCH3X', 'CHCHX', 'CHCCH3X', 'NCOHX', 'NCOHX', 'CH2CH2X',
'CH3CHCH2X', 'CH2CCH2X', 'CH2NHX', 'CH2COX', 'CH2OX', 'OC(OH)OHX', 'CH3CHOX',
'HCOOHX', 'CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X', 'CH2CH2X', 'CH3CHCH2X',
'CH2CCH2X', 'CH2NHX', 'CH2NHX', 'CH2COX', 'CH2OX', 'OC(OH)OHX', 'CH3CHOX',
'HCOOHX', 'CH2COX', 'CH2OX', 'OC(OH)OHX', 'CH3CHOX', 'HCOOHX', 'CH4X', 'CH4X',
'CH3CH3X', 'CH3CH2CH3X', 'CH3CH2OHX', 'CH3NH2X', 'CH3OHX', 'CH3OCH3X',
'CH3OCH2OHX', 'H2C(OH)OHX', 'CH3CH3X', 'CH3CH2CH3X', 'CH3CH2OHX', 'CH3CH3X',
'CH3CH2CH3X', 'CH3CH2OHX', 'CH3NH2X', 'CH3NH2X', 'CH3OHX', 'CH3OCH3X',
'CH3OCH2OHX', 'H2C(OH)OHX', 'CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX', 'H2C(OH)OHX',
'OCNHX', 'NHCNHX', 'OCNHX', 'NHCNHX', 'OCNHX', 'NHCNHX', 'NH3X', 'NH3X',
'OCHNH2X', 'NH2NH2X', 'NH2NCH3CH3X', 'H2NOHX', 'OCHNH2X', 'OCHNH2X', 'NH2NH2X',
'NH2NCH3CH3X', 'NH2NH2X', 'NH2NCH3CH3X', 'H2NOHX', 'H2NOHX', 'ONNH2X',
'ONNCH3CH3X', 'ONOHX', 'ONNH2X', 'ONNCH3CH3X', 'ONOHX', 'ONNH2X', 'ONNCH3CH3X',
'ONNH2X', 'ONNCH3CH3X', 'ONOHX', 'ONOHX', 'H2OX', 'H2OX', 'HOOHX', 'HOOHX',
'HOOHX']""",
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
        H298=(-44.606, 'kJ/mol'),
        S298=(-120.514, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CHCHX', 'CHCCH3X', 'NCOHX', 'CHCHX', 'CHCCH3X', 'NCOHX',
'CHCHX', 'CHCCH3X', 'CHCHX', 'CHCCH3X', 'NCOHX', 'NCOHX']""",
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
        H298=(-49.983, 'kJ/mol'),
        S298=(-119.645, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CHCHX', 'CHCCH3X', 'CHCHX', 'CHCCH3X', 'CHCHX', 'CHCCH3X',
'CHCHX', 'CHCCH3X']""",
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
        H298=(-33.85, 'kJ/mol'),
        S298=(-122.254, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['NCOHX', 'NCOHX', 'NCOHX', 'NCOHX']""",
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
        H298=(-46.937, 'kJ/mol'),
        S298=(-130.966, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X', 'CH2NHX', 'CH2COX', 'CH2OX',
'OC(OH)OHX', 'CH3CHOX', 'HCOOHX', 'CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X', 'CH2NHX',
'CH2COX', 'CH2OX', 'OC(OH)OHX', 'CH3CHOX', 'HCOOHX', 'CH2CH2X', 'CH3CHCH2X',
'CH2CCH2X', 'CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X', 'CH2NHX', 'CH2NHX', 'CH2COX',
'CH2OX', 'OC(OH)OHX', 'CH3CHOX', 'HCOOHX', 'CH2COX', 'CH2OX', 'OC(OH)OHX',
'CH3CHOX', 'HCOOHX']""",
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
        H298=(-79.5, 'kJ/mol'),
        S298=(-143.863, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X', 'CH2CH2X', 'CH3CHCH2X',
'CH2CCH2X', 'CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X', 'CH2CH2X', 'CH3CHCH2X',
'CH2CCH2X']""",
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
        H298=(-39.465, 'kJ/mol'),
        S298=(-135.288, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH2NHX', 'CH2NHX', 'CH2NHX', 'CH2NHX']""",
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
        H298=(-28.893, 'kJ/mol'),
        S298=(-122.364, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH2COX', 'CH2OX', 'OC(OH)OHX', 'CH3CHOX', 'HCOOHX', 'CH2COX',
'CH2OX', 'OC(OH)OHX', 'CH3CHOX', 'HCOOHX', 'CH2COX', 'CH2OX', 'OC(OH)OHX',
'CH3CHOX', 'HCOOHX', 'CH2COX', 'CH2OX', 'OC(OH)OHX', 'CH3CHOX', 'HCOOHX']""",
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
        Cpdata=([7.704, 8.778, 9.334, 9.643, 9.941, 10.07, 10.175], 'J/(mol*K)'),
        H298=(-48.241, 'kJ/mol'),
        S298=(-127.608, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH4X', 'CH4X', 'CH3CH3X', 'CH3CH2CH3X', 'CH3CH2OHX', 'CH3NH2X',
'CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX', 'H2C(OH)OHX', 'CH4X', 'CH4X', 'CH3CH3X',
'CH3CH2CH3X', 'CH3CH2OHX', 'CH3NH2X', 'CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX',
'H2C(OH)OHX', 'CH3CH3X', 'CH3CH2CH3X', 'CH3CH2OHX', 'CH3CH3X', 'CH3CH2CH3X',
'CH3CH2OHX', 'CH3NH2X', 'CH3NH2X', 'CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX',
'H2C(OH)OHX', 'CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX', 'H2C(OH)OHX']""",
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
        H298=(-46.667, 'kJ/mol'),
        S298=(-137.338, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH3CH3X', 'CH3CH2CH3X', 'CH3CH2OHX', 'CH3CH3X', 'CH3CH2CH3X',
'CH3CH2OHX', 'CH3CH3X', 'CH3CH2CH3X', 'CH3CH2OHX', 'CH3CH3X', 'CH3CH2CH3X',
'CH3CH2OHX']""",
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
        H298=(-105.541, 'kJ/mol'),
        S298=(-141.215, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH3NH2X', 'CH3NH2X', 'CH3NH2X', 'CH3NH2X']""",
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
        H298=(-38.886, 'kJ/mol'),
        S298=(-139.363, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX', 'H2C(OH)OHX', 'CH3OHX',
'CH3OCH3X', 'CH3OCH2OHX', 'H2C(OH)OHX', 'CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX',
'H2C(OH)OHX', 'CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX', 'H2C(OH)OHX']""",
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
        H298=(-47.801, 'kJ/mol'),
        S298=(-122.197, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['OCNHX', 'NHCNHX', 'OCNHX', 'NHCNHX', 'OCNHX', 'NHCNHX',
'OCNHX', 'NHCNHX']""",
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
        H298=(-47.801, 'kJ/mol'),
        S298=(-122.197, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['OCNHX', 'NHCNHX', 'OCNHX', 'NHCNHX', 'OCNHX', 'NHCNHX',
'OCNHX', 'NHCNHX']""",
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
        Cpdata=([3.377, 5.633, 6.987, 7.841, 8.796, 9.275, 9.747], 'J/(mol*K)'),
        H298=(-74.642, 'kJ/mol'),
        S298=(-139.272, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['NH3X', 'NH3X', 'OCHNH2X', 'NH2NH2X', 'NH2NCH3CH3X', 'H2NOHX',
'NH3X', 'NH3X', 'OCHNH2X', 'NH2NH2X', 'NH2NCH3CH3X', 'H2NOHX', 'OCHNH2X',
'OCHNH2X', 'NH2NH2X', 'NH2NCH3CH3X', 'NH2NH2X', 'NH2NCH3CH3X', 'H2NOHX',
'H2NOHX']""",
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
        H298=(-53.75, 'kJ/mol'),
        S298=(-138.501, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['OCHNH2X', 'OCHNH2X', 'OCHNH2X', 'OCHNH2X']""",
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
        H298=(-98.622, 'kJ/mol'),
        S298=(-150.696, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['NH2NH2X', 'NH2NCH3CH3X', 'NH2NH2X', 'NH2NCH3CH3X', 'NH2NH2X',
'NH2NCH3CH3X', 'NH2NH2X', 'NH2NCH3CH3X']""",
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
        H298=(-50.894, 'kJ/mol'),
        S298=(-132.089, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['H2NOHX', 'H2NOHX', 'H2NOHX', 'H2NOHX']""",
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
        H298=(-68.483, 'kJ/mol'),
        S298=(-141.385, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['ONNH2X', 'ONNCH3CH3X', 'ONOHX', 'ONNH2X', 'ONNCH3CH3X',
'ONOHX', 'ONNH2X', 'ONNCH3CH3X', 'ONOHX', 'ONNH2X', 'ONNCH3CH3X', 'ONNH2X',
'ONNCH3CH3X', 'ONOHX', 'ONOHX']""",
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
        H298=(-68.483, 'kJ/mol'),
        S298=(-141.385, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['ONNH2X', 'ONNCH3CH3X', 'ONOHX', 'ONNH2X', 'ONNCH3CH3X',
'ONOHX', 'ONNH2X', 'ONNCH3CH3X', 'ONNH2X', 'ONNCH3CH3X', 'ONOHX', 'ONOHX']""",
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
        Cpdata=([5.682, 6.734, 7.312, 7.663, 8.05, 8.242, 8.401], 'J/(mol*K)'),
        H298=(-76.259, 'kJ/mol'),
        S298=(-139.884, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['ONNH2X', 'ONNCH3CH3X', 'ONNH2X', 'ONNCH3CH3X', 'ONNH2X',
'ONNCH3CH3X', 'ONNH2X', 'ONNCH3CH3X']""",
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
        H298=(-52.931, 'kJ/mol'),
        S298=(-144.387, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['ONOHX', 'ONOHX', 'ONOHX', 'ONOHX']""",
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
        Cpdata=([4.88, 6.31, 7.047, 7.482, 7.98, 8.26, 8.524], 'J/(mol*K)'),
        H298=(-17.874, 'kJ/mol'),
        S298=(-101.295, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['H2OX', 'H2OX', 'HOOHX', 'H2OX', 'H2OX', 'HOOHX', 'HOOHX',
'HOOHX']""",
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
        H298=(-25.178, 'kJ/mol'),
        S298=(-110.352, 'J/(mol*K)'),
    ),
shortDesc=u"""Averaged from: ['HOOHX', 'HOOHX', 'HOOHX', 'HOOHX']""",
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
