import textwrap

group_data = {
    'RX': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 R  ux
        2 * X ux
        """,)
    },
    'RXbridgedBidentate': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X  u0 {3,[S,D,T]}
        2 X  u0 {4,[S,D,T]}
        3 R!H ux {1,[S,D,T]} {5,[S,D,T]}
        4 R!H ux {2,[S,D,T]} {5,[S,D,T]}
        5 R!H ux {3,[S,D,T]} {4,[S,D,T]}
        """,)
    },
    'CXRCX': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 {3,[S,D,T]}
        2 X u0 {4,[S,D,T]}
        3 C  u0 {1,[S,D,T]} {5,[S,D,T]}
        4 C  u0 {2,[S,D,T]} {5,[S,D,T]}
        5 R!H  u0 {3,[S,D,T]} {4,[S,D,T]}
        """,)
    },
    'C=X=R-C-XR2': {
        'gas_precursors': ['CCHCH2'],
        'adsorbates': ['XCCHXCH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,D}
        2 X u0 p0 c0 {5,S}
        3 C  u0 p0 c0 {1,D} {4,D}
        4 R!H  u0 px c0 {3,D} {5,S}
        5 C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
        6 R  u0 px c0 {5,S}
        7 R  u0 px c0 {5,S}
        """,)
    },
    'R2C-X-R-C-XR2': {
        'gas_precursors': ['CH2CH2CH2'],
        'adsorbates': ['XCH2CH2XCH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {5,S}
        3 C  u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        4 R!H  u0 px c0 {3,S} {5,S}
        5 C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
        6 R  u0 px c0 {5,S}
        7 R  u0 px c0 {5,S}
        8 R  u0 px c0 {3,S}
        9 R  u0 px c0 {3,S}
        """,)
    },
    'RC=X-R=C-XR': {
        'gas_precursors': ['CHCHCH'],
        'adsorbates': ['XCHCHXCH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,D}
        2 X u0 p0 c0 {5,S}
        3 C  u0 p0 c0 {1,D} {4,S} {6,S}
        4 R!H  u0 px c0 {3,S} {5,D}
        5 C  u0 p0 c0 {2,S} {4,D} {7,S}
        6 R  u0 px c0 {3,S}
        7 R  u0 px c0 {5,S}
        """,)
    },
    'RC-X=R-C-XR2': {
        'gas_precursors': ['CHCHCH2'],
        'adsorbates': ['XCHCHXCH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {5,S}
        3 C  u0 p0 c0 {1,S} {4,D} {6,S}
        4 R!H  u0 px c0 {3,D} {5,S}
        5 C  u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
        6 R  u0 px c0 {3,S}
        7 R  u0 px c0 {5,S}
        8 R  u0 px c0 {5,S}
        """,)
    },
    'RC=X-R-C-XR2': {
        'gas_precursors': ['CHCH2CH2'],
        'adsorbates': ['XCHCH2XCH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,D}
        2 X u0 p0 c0 {5,S}
        3 C  u0 p0 c0 {1,D} {4,S} {6,S}
        4 R!H  u0 px c0 {3,S} {5,S}
        5 C  u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
        6 R  u0 px c0 {3,S}
        7 R  u0 px c0 {5,S}
        8 R  u0 px c0 {5,S}
        """,)
    },
    'RC-X=R=C-XR': {
        'gas_precursors': ['CHCCH'],
        'adsorbates': ['XCHCXCH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {5,S}
        3 C  u0 p0 c0 {1,S} {4,D} {6,S}
        4 R!H  u0 p0 c0 {3,D} {5,D}
        5 C  u0 p0 c0 {2,S} {4,D} {7,S}
        6 R  u0 px c0 {3,S}
        7 R  u0 px c0 {5,S}
        """,)
    },
    'RC-X=R=C=X': {
        'gas_precursors': ['CHCC'],
        'adsorbates': ['XCHCXC'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {5,D}
        3 C  u0 p0 c0 {1,S} {4,D} {6,S}
        4 R!H  u0 p0 c0 {3,D} {5,D}
        5 C  u0 p0 c0 {2,D} {4,D}
        6 R  u0 px c0 {3,S}
        """,)
    },
    'C#X-R-C-XR2': {
        'gas_precursors': ['CCH2CH2'],
        'adsorbates': ['XCCH2XCH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,T}
        2 X u0 p0 c0 {5,S}
        3 C  u0 p0 c0 {1,T} {4,S}
        4 R!H  u0 px c0 {3,S} {5,S}
        5 C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
        6 R  u0 px c0 {5,S}
        7 R  u0 px c0 {5,S}
        """,)
    },
    'C#X-R=C-XR': {
        'gas_precursors': ['CHCHC'],
        'adsorbates': ['XCHCHXC'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,T}
        2 X u0 p0 c0 {5,S}
        3 C  u0 p0 c0 {1,T} {4,S}
        4 R!H  u0 px c0 {3,S} {5,D}
        5 C  u0 p0 c0 {2,S} {4,D} {6,S}
        6 R  u0 px c0 {5,S}
        """,)
    },
    'C#X-R-C#X': {
        'gas_precursors': ['CCH2C'],
        'adsorbates': ['XCCH2XC'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,T}
        2 X u0 p0 c0 {5,T}
        3 C  u0 p0 c0 {1,T} {4,S}
        4 R!H  u0 px c0 {3,S} {5,S}
        5 C  u0 p0 c0 {2,T} {4,S}
        """,)
    },
    'RC=X-R-C=XR': {
        'gas_precursors': ['CHCH2CH'],
        'adsorbates': ['XCHCH2XCH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,D}
        2 X u0 p0 c0 {5,D}
        3 C  u0 p0 c0 {1,D} {4,S} {6,S}
        4 R!H  u0 px c0 {3,S} {5,S}
        5 C  u0 p0 c0 {2,D} {4,S} {7,S}
        6 R  u0 px c0 {3,S}
        7 R  u0 px c0 {5,S}
        """,)
    },
    'C#X-R-C=XR': {
        'gas_precursors': ['CHCH2C'],
        'adsorbates': ['XCHCH2XC'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,T}
        2 X u0 p0 c0 {5,D}
        3 C  u0 p0 c0 {1,T} {4,S}
        4 R!H  u0 px c0 {3,S} {5,S}
        5 C  u0 p0 c0 {2,D} {4,S} {6,S}
        6 R  u0 p0 c0 {5,S}
        """,)
    },
    'CXROX': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 {3,[S,D,T]}
        2 X u0 {4,S}
        3 C  u0 {1,[S,D,T]} {5,[S,D,T]}
        4 O  u0 p2 {2,S} {5,S}
        5 R!H  u0 px {3,[S,D,T]} {4,S}

        """,)
    },
    'RC-X=R-O-X': {
        'gas_precursors': ['CHCHO'],
        'adsorbates': ['XCHCHXO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {5,S}
        3 C  u0 p0 c0 {1,S} {4,D} {6,S}
        4 R!H  u0 px c0 {3,D} {5,S}
        5 O  u0 p2 c0 {2,S} {4,S}
        6 R  u0 px c0 {3,S}
        """,)
    },
    'OXROX': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {4,S}
        3 O  u0 p2 c0 {1,S} {5,S}
        4 O  u0 p2 c0 {2,S} {5,S}
        5 R!H  u0 px c0 {3,S} {4,S}
        """,)
    },
    'O-X-C-O-X': {
        'gas_precursors': ['CO3', 'H2CO2'],
        'adsorbates': ['XOC(O)XO', 'H2C(XO)XO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {5,S}
        3 O  u0 p2 c0 {1,S} {4,S}
        4 C  u0 p0 c0 {3,S} {5,S}
        5 O  u0 p2 c0 {2,S} {4,S}
        """,)
    },
    'RXbidentate': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X  u0 p0 c0 {3,[S,D,T]}
        2 X  u0 p0 c0 {4,[S,D,T]}
        3 R!H u0 {1,[S,D,T]} {4,[S,D,T]}
        4 R!H u0 {2,[S,D,T]} {3,[S,D,T]}
        """,)
    },
    'CXCX': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 {3,[S,D,T]}
        2 X u0 {4,[S,D,T]}
        3 C  u0 {1,[S,D,T]} {4,[S,D,T]}
        4 C  u0 {2,[S,D,T]} {3,[S,D,T]}
        """,)
    },
    'C-XC-X': {
        'gas_precursors': ['CC'],
        'adsorbates': ['XCXC'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0  p0 c0 {3,D}
        2 X u0  p0 c0 {4,D}
        3 C  u0  p0 c0 {1,D} {4,D}
        4 C  u0  p0 c0 {2,D} {3,D}
        """,)
    },
    'C=XRC=XR': {
        'gas_precursors': ['CHCH'],
        'adsorbates': ['XCHXCH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,D}
        2 X u0 p0 c0 {4,D}
        3 C  u0 p0 c0 {1,D} {4,S} {5,S}
        4 C  u0 p0 c0 {2,D} {3,S} {6,S}
        5 R  u0 px c0 {3,S}
        6 R  u0 px c0 {4,S}
        """,)
    },
    'C-XR2C-XR2': {
        'gas_precursors': ['C2H4', 'CH3CHCH2'],
        'adsorbates': ['XCH2XCH2', 'CH3XCHXCH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {4,S}
        3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
        4 C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        5 R  u0 px c0 {3,S}
        6 R  u0 px c0 {3,S}
        7 R  u0 px c0 {4,S}
        8 R  u0 px c0 {4,S}
        """,)
    },
    'C-XR2C=XR': {
        'gas_precursors': ['CH2CH', 'CH2COH', 'CHCHCH3'],
        'adsorbates': ['XCH2XCH', 'XCH2XCOH', 'XCHXCHCH3'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {4,D}
        3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
        4 C  u0 p0 c0 {2,D} {3,S} {7,S}
        5 R  u0 px c0 {3,S}
        6 R  u0 px c0 {3,S}
        7 R  u0 px c0 {4,S}
        """,)
    },
    'C-XRC=X': {
        'gas_precursors': ['CHC'],
        'adsorbates': ['XCHXC'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0  p0 c0 {3,S}
        2 X u0  p0 c0 {4,D}
        3 C  u0  p0 c0 {1,S} {4,D} {5,S}
        4 C  u0  p0 c0 {2,D} {3,D}
        5 R  u0  px c0 {3,S}
        """,)
    },
    'C=XRC-XR': {
        'gas_precursors': ['CHCO'],
        'adsorbates': ['XCHXCO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,D}
        2 X u0 p0 c0 {4,S}
        3 C  u0 p0 c0 {1,D} {4,S} {5,S}
        4 C  u0 p0 c0 {2,S} {3,S} {6,D}
        5 R  u0 px c0 {3,S}
        6 R!H  u0 px c0 {4,D}
        """,)
    },
    'C#XC-XR': {
        'gas_precursors': ['CCCH2'],
        'adsorbates': ['XCXCCH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,T}
        2 X u0 p0 c0 {4,S}
        3 C  u0 p0 c0 {1,T} {4,S}
        4 C  u0 p0 c0 {2,S} {3,S} {5,D}
        5 R!H  u0 px c0 {4,D}
        """,)
    },
    'C#XC-XR2': {
        'gas_precursors': ['CCH2', 'CCHCH3'],
        'adsorbates': ['XCXCH2', 'XCXCHCH3'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,T}
        2 X u0 p0 c0 {4,S}
        3 C  u0 p0 c0 {1,T} {4,S}
        4 C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        5 R  u0 px c0 {4,S}
        6 R  u0 px c0 {4,S}
        """,)
    },
    'C#XC=XR': {
        'gas_precursors': ['CCCH3'],
        'adsorbates': ['XCXCCH3'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,T}
        2 X u0 p0 c0 {4,D}
        3 C  u0 p0 c0 {1,T} {4,S}
        4 C  u0 p0 c0 {2,D} {3,S} {5,S}
        5 R  u0 px c0 {4,S}
        """,)
    },
    'C-XR2C-XR': {
        'gas_precursors': ['CH2CCH2'],
        'adsorbates': ['XCH2XCCH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {4,S}
        3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
        4 C  u0 p0 c0 {2,S} {3,S} {7,D}
        5 R  u0 px c0 {3,S}
        6 R  u0 px c0 {3,S}
        7 R!H  u0 px c0 {4,D}
        """,)
    },
    'C-XRC-XR': {
        'gas_precursors': ['CHCCH3'],
        'adsorbates': ['XCHXCCH3'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {4,S}
        3 C  u0 p0 c0 {1,S} {4,D} {5,S}
        4 C  u0 p0 c0 {2,S} {3,D} {6,S}
        5 R  u0 px c0 {3,S}
        6 R  u0 px c0 {4,S}
        """,)
    },
    'NXCX': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,[S,D,T]}
        2 X u0 p0 c0 {4,[S,D]}
        3 C u0 p0 c0 {1,[S,D,T]} {4,[S,D]}
        4 N u0 p[0,1] c[0,+1] {2,[S,D]} {3,[S,D]}
        """,)
    },
    'inv(C=XRN=X)': {
        'gas_precursors': ['CHN', 'OHCN'],
        'adsorbates': ['XCHXN', 'XNXCOH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,D}
        2 X u0 p0 c0 {4,D}
        3 C  u0 p0 c0 {1,D} {4,S} {5,S}
        4 N  u0 p1 c0 {2,D} {3,S}
        5 R  u0 p0 c0 {3,S}
        """,)
    },
    'inv(C-XR2N=X)': {
        'gas_precursors': ['CH2N'],
        'adsorbates': ['XCH2XN'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {4,D}
        3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
        4 N  u0 p1 c0 {2,D} {3,S}
        5 R  u0 p0 c0 {3,S}
        6 R  u0 p0 c0 {3,S}
        """,)
    },
    'inv(C-XR2N-XR)': {
        'gas_precursors': ['CH2NH'],
        'adsorbates': ['XCH2XNH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {4,S}
        3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
        4 N  u0 p1 c0 {2,S} {3,S} {7,S}
        5 R  u0 p0 c0 {3,S}
        6 R  u0 p0 c0 {3,S}
        7 R  u0 p0 c0 {4,S}
        """,)
    },
    'inv(C=XRN-XR)': {
        'gas_precursors': ['CHNH', 'OHCNH'],
        'adsorbates': ['XCHXNH', 'OHXCXNH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,D}
        2 X u0 p0 c0 {4,S}
        3 C  u0 p0 c0 {1,D} {4,S} {5,S}
        4 N  u0 p1 c0 {2,S} {3,S} {6,S}
        5 R  u0 p0 c0 {3,S}
        6 R  u0 p0 c0 {4,S}
        """,)
    },
    'inv(C-XRN-X)': {
        'gas_precursors': ['CHN'],
        'adsorbates': ['XCHXN'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {5,S}
        3 C u0 p0 c0 {1,S} {4,S} {5,D}
        4 R u0 px c0 {3,S}
        5 N u0 p2 c0 {2,S} {3,D}
        """,)
    },
    'inv(C-XRN=X)': {
        'gas_precursors': ['OCN', 'NCNH'],
        'adsorbates': ['XNXCO', 'XNXCNH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0  p0 c0 {3,S}
        2 X u0  p0 c0 {4,D}
        3 C  u0  p0 c0 {1,S} {4,S} {5,D}
        4 N  u0  p1 c0 {2,D} {3,S}
        5 R!H u0 px c0 {3,D}
        """,)
    },
    'inv(C-XRN-XR)': {
        'gas_precursors': ['NHCNH', 'OCNH'],
        'adsorbates': ['NHXCXNH', 'XNHXCO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0  p0 c0 {3,S}
        2 X u0  p0 c0 {4,S}
        3 C  u0  p0 c0 {1,S} {4,S} {5,D}
        4 N  u0  p1 c0 {2,S} {3,S} {6,S}
        5 R!H u0 px c0 {3,D}
        6 R u0 px c0 {4,S}
        """,)
    },
    'CXNX': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 X u0 p0 c0 {3,[S,D,T]}
        2 * X u0 p0 c0 {4,[S,D]}
        3 C u0 p0 c0 {1,[S,D,T]} {4,[S,D]}
        4 N u0 p[0,1] c[0,+1] {2,[S,D]} {3,[S,D]}
        """,)
    },
    'C=XRN=X': {
        'gas_precursors': ['CHN', 'OHCN'],
        'adsorbates': ['XCHXN', 'XNXCOH'],
        'connectivity_string': textwrap.dedent("""
        1 X u0 p0 c0 {3,D}
        2 * X u0 p0 c0 {4,D}
        3 C  u0 p0 c0 {1,D} {4,S} {5,S}
        4 N  u0 p1 c0 {2,D} {3,S}
        5 R  u0 p0 c0 {3,S}
        """,)
    },
    'C-XR2N=X': {
        'gas_precursors': ['CH2N'],
        'adsorbates': ['XCH2XN'],
        'connectivity_string': textwrap.dedent("""
        1 X u0 p0 c0 {3,S}
        2 * X u0 p0 c0 {4,D}
        3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
        4 N  u0 p1 c0 {2,D} {3,S}
        5 R  u0 p0 c0 {3,S}
        6 R  u0 p0 c0 {3,S}
        """,)
    },
    'C-XR2N-XR': {
        'gas_precursors': ['CH2NH'],
        'adsorbates': ['XCH2XNH'],
        'connectivity_string': textwrap.dedent("""
        1 X u0 p0 c0 {3,S}
        2 * X u0 p0 c0 {4,S}
        3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
        4 N  u0 p1 c0 {2,S} {3,S} {7,S}
        5 R  u0 p0 c0 {3,S}
        6 R  u0 p0 c0 {3,S}
        7 R  u0 p0 c0 {4,S}
        """,)
    },
    'C=XRN-XR': {
        'gas_precursors': ['CHNH', 'OHCNH'],
        'adsorbates': ['XCHXNH', 'OHXCXNH'],
        'connectivity_string': textwrap.dedent("""
        1 X u0 p0 c0 {3,D}
        2 * X u0 p0 c0 {4,S}
        3 C  u0 p0 c0 {1,D} {4,S} {5,S}
        4 N  u0 p1 c0 {2,S} {3,S} {6,S}
        5 R  u0 p0 c0 {3,S}
        6 R  u0 p0 c0 {4,S}
        """,)
    },
    'C-XRN-X': {
        'gas_precursors': ['CHN'],
        'adsorbates': ['XCHXN'],
        'connectivity_string': textwrap.dedent("""
        1 X u0 p0 c0 {3,S}
        2 * X u0 p0 c0 {5,S}
        3 C u0 p0 c0 {1,S} {4,S} {5,D}
        4 R u0 px c0 {3,S}
        5 N u0 p2 c0 {2,S} {3,D}
        """,)
    },
    'C-XRN=X': {
        'gas_precursors': ['OCN', 'NCNH'],
        'adsorbates': ['XNXCO', 'XNXCNH'],
        'connectivity_string': textwrap.dedent("""
        1 X u0  p0 c0 {3,S}
        2 * X u0  p0 c0 {4,D}
        3 C  u0  p0 c0 {1,S} {4,S} {5,D}
        4 N  u0  p1 c0 {2,D} {3,S}
        5 R!H u0 px c0 {3,D}
        """,)
    },
    'C-XRN-XR': {
        'gas_precursors': ['NHCNH', 'OCNH'],
        'adsorbates': ['NHXCXNH', 'XNHXCO'],
        'connectivity_string': textwrap.dedent("""
        1 X u0  p0 c0 {3,S}
        2 * X u0  p0 c0 {4,S}
        3 C  u0  p0 c0 {1,S} {4,S} {5,D}
        4 N  u0  p1 c0 {2,S} {3,S} {6,S}
        5 R!H u0 px c0 {3,D}
        6 R u0 px c0 {4,S}
        """,)
    },
    'CXOX': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 {3,[S,D,T]}
        2 X u0 {4,S}
        3 C  u0 {1,[S,D,T]} {4,S}
        4 O  u0 p2 {2,S} {3,S}
        """,)
    },
    'C=XRO-X': {
        'gas_precursors': ['HCO'],
        'adsorbates': ['XCHXO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,D}
        2 X u0 p0 c0 {4,S}
        3 C  u0 p0 c0 {1,D} {4,S} {5,S}
        4 O  u0 p2 c0 {2,S} {3,S}
        5 R  u0 px c0 {3,S}
        """,)
    },
    'C-XR2O-X': {
        'gas_precursors': ['H2CO'],
        'adsorbates': ['XCH2XO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {4,S}
        3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
        4 O  u0 p2 c0 {2,S} {3,S}
        5 R  u0 px c0 {3,S}
        6 R  u0 px c0 {3,S}
        """,)
    },
    'C-XRO-X': {
        'gas_precursors': ['OCNH'],
        'adsorbates': ['XOXCNH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0  p0 c0 {3,S}
        2 X u0  p0 c0 {4,S}
        3 C  u0  p0 c0 {1,S} {4,S} {5,D}
        4 O  u0  p2 c0 {2,S} {3,S}
        5 R!H u0 px c0 {3,D}
        """,)
    },
    'NXNX': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 {3,[S,D]}
        2 X u0 {4,[S,D]}
        3 N  u0 {1,[S,D]} {4,[S,D]}
        4 N  u0 {2,[S,D]} {3,[S,D]}
        """,)
    },
    'N-XRN-XR': {
        'gas_precursors': ['NHNH', 'CH3NNOH'],
        'adsorbates': ['XNHXNH', 'CH3XNXNOH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {4,S}
        3 N  u0 p1 c0 {1,S} {4,S} {5,S}
        4 N  u0 p1 c0 {2,S} {3,S} {6,S}
        5 R  u0 p0 c0 {3,S}
        6 R  u0 p0 c0 {4,S}
        """,)
    },
    'N-XRN=X': {
        'gas_precursors': ['NNH', 'NNCH3'],
        'adsorbates': ['XNHXN', 'XNXNCH3'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {4,D}
        3 N  u0 p1 c0 {1,S} {4,S} {5,S}
        4 N  u0 p1 c0 {2,D} {3,S}
        5 R  u0 p0 c0 {3,S}
        """,)
    },
    'NXOX': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,[S,D]}
        2 X u0 p0 c0 {4,S}
        3 N  u0 px cx {1,[S,D]} {4,[S,D]}
        4 O  u0 p2 c0 {2,S} {3,[S,D]}
        """,)
    },
    'N-XRO-X': {
        'gas_precursors': ['HNO'],
        'adsorbates': ['XOXNH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {4,S}
        3 N  u0 p1 c0 {1,S} {4,S} {5,S}
        4 O  u0 p2 c0 {2,S} {3,S}
        5 R u0 px c0 {3,S}
        """,)
    },
    'N[+]=XR[-]O-X': {
        'gas_precursors': ['NO2'],
        'adsorbates': ['XOXNO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,D}
        2 X u0 p0 c0 {4,S}
        3 N  u0 p0 c+1 {1,D} {4,S} {5,S}
        4 O  u0 p2 c0 {2,S} {3,S}
        5 R u0 px c-1 {3,S}
        """,)
    },
    'OXOX': {
        'gas_precursors': ['O2'],
        'adsorbates': ['XOXO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 X u0 p0 c0 {4,S}
        3 O  u0 p2 c0 {1,S} {4,S}
        4 O  u0 p2 c0 {2,S} {3,S}
        """,)
    },
    'RXsingleChemisorbed': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 {2,[S,D,T,Q]}
        2 R  ux {1,[S,D,T,Q]}
        """,)
    },
    'CX': {
        'gas_precursors': ['CN'],
        'adsorbates': ['XCN'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 {2,[S,D,T,Q]}
        2 C  ux {1,[S,D,T,Q]}
        """,)
    },
    'C#XR': {
        'gas_precursors': ['CH'],
        'adsorbates': ['XCH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,T}
        2 C  u0 p0 c0 {1,T} {3,S}
        3 R  u0 px c0 {2,S}
        """,)
    },
    'C#XCR3': {
        'gas_precursors': ['CCH3', 'CCH2CH3', 'CCH2OH'],
        'adsorbates': ['XCCH3', 'XCCH2CH3', 'XCCH2OH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,T}
        2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
        3 C  u0 p0 c0 {1,T} {2,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        6 R  u0 px c0 {2,S}
        """,)
    },
    'C#XN': {
        'gas_precursors': ['CNO', 'CNH2'],
        'adsorbates': ['XCNO', 'XCNH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,T}
        2 C  u0 p0 c0 {1,T} {3,S}
        3 N  u0 p1 c0 {2,S}
        """,)
    },
    'C#XOR': {
        'gas_precursors': ['COH'],
        'adsorbates': ['XCOH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,T}
        2 C  u0 p0 c0 {1,T} {3,S}
        3 O  u0 p2 c0 {2,S} {4,S}
        4 R  u0 px c0 {3,S}
        """,)
    },
    'C#XCR2': {
        'gas_precursors': ['CCHCH2', 'CCHO'],
        'adsorbates': ['XCCHCH2', 'XCCHO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,T}
        2 C  u0 p0 c0 {3,S} {4,S} {5,D}
        3 C  u0 p0 c0 {1,T} {2,S}
        4 R  u0 px c0 {2,S}
        5 R!H  u0 px c0 {2,D}
        """,)
    },
    'C=XR2': {
        'gas_precursors': ['CH2'],
        'adsorbates': ['XCH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,D}
        2 C  u0 p0 c0 {1,D} {3,S} {4,S}
        3 R  u0 px c0 {2,S}
        4 R  u0 px c0 {2,S}
        """,)
    },
    'C=XRCR3': {
        'gas_precursors': ['CH3CCH3', 'CH3COH', 'CHCH2CH3', 'CH3CH'],
        'adsorbates': ['CH3XCCH3', 'CH3XCOH', 'XCHCH2CH3', 'XCHCH3'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,D}
        2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
        3 C  u0 p0 c0 {1,D} {2,S} {7,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        6 R  u0 px c0 {2,S}
        7 R  u0 px c0 {3,S}
        """,)
    },
    'C=XROR': {
        'gas_precursors': ['HCOH', 'CH3COH'],
        'adsorbates': ['XCHOH', 'CH3XCOH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,D}
        2 C  u0 p0 c0 {1,D} {3,S} {4,S}
        3 O  u0 p2 c0 {2,S} {5,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {3,S}
        """,)
    },
    'C=XRN': {
        'gas_precursors': ['CHNH2', 'OHCNH2', 'NH2CNH2'],
        'adsorbates': ['XCHNH2', 'OHXCNH2', 'NH2XCNH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,D}
        2 C  u0 p0 c0 {1,D} {3,S} {4,S}
        3 N  u0 p1 c0 {2,S}
        4 R  u0 p0 c0 {2,S}
        """,)
    },
    'C=XRCR2': {
        'gas_precursors': ['CHCHCH2', 'CHCHO'],
        'adsorbates': ['XCHCHCH2', 'XCHCHO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,D}
        2 C  u0 p0 c0 {3,S} {4,S} {5,D}
        3 C  u0 p0 c0 {1,D} {2,S} {6,S}
        4 R  u0 px c0 {2,S}
        5 R!H  u0 px c0 {2,D}
        6 R  u0 px c0 {3,S}
        """,)
    },
    'C=X(=R)': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X  u0  p0 c0 {2,D}
        2 C   u0  p0 c0 {1,D} {3,D}
        3 R!H u0  px c0 {2,D}
        """,)
    },
    'C=X(=C)': {
        'gas_precursors': ['CCO', 'CCCH2', 'CCH2'],
        'adsorbates': ['XCCO', 'XCCCH2', 'XCCH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0  p0 c0 {2,D}
        2 C  u0  p0 c0 {1,D} {3,D}
        3 C  u0  p0 c0 {2,D}
        """,)
    },
    'C=X(=NR)': {
        'gas_precursors': ['CNH'],
        'adsorbates': ['XCNH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0  p0 c0 {2,D}
        2 C  u0  p0 c0 {1,D} {3,D}
        3 N  u0  p1 c0 {2,D} {4,S}
        4 R  u0  px c0 {3,S}
        """,)
    },
    'C-XR3': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,S}
        2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
        3 R  u0 px c0 {2,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        """,)
    },
    'C-XR2CR3': {
        'gas_precursors': ['CH2CH2CH3', 'CH2CH2OH', 'CH2CH3',
                           'CH3CHCH3', 'CH3CHOH'],
        'adsorbates': ['XCH2CH2CH3', 'XCH2CH2OH', 'XCH2CH3',
                       'CH3XCHCH3', 'CH3XCHOH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,S}
        2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
        3 C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        6 R  u0 px c0 {3,S}
        7 R  u0 px c0 {3,S}
        8 R  u0 px c0 {3,S}
        """,)
    },
    'C-XR2N': {
        'gas_precursors': ['CH2NH2'],
        'adsorbates': ['XCH2NH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,S}
        2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
        3 N  u0 p1 c0 {2,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        """,)
    },
    'C-XR2OR': {
        'gas_precursors': ['H2COH', 'CH3CHOH'],
        'adsorbates': ['XCH2OH', 'CH3XCHOH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,S}
        2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
        3 O  u0 p2 c0 {2,S} {6,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        6 R  u0 px c0 {3,S}
        """,)
    },
    'C-XR2': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0  p0 c0 {2,S}
        2 C  u0  p0 c0 {1,S} {3,D} {4,S}
        3 R!H u0  px c0 {2,D}
        4 R  u0  px c0 {2,S}
        """,)
    },
    'C-XRO': {
        'gas_precursors': ['HCO', 'COOH', 'CH3CO', 'CCHO', 'CH3CH2CO'],
        'adsorbates': ['XCHO', 'XCOOH', 'CH3XCO', 'XCCHO', 'CH3CH2XCO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0  p0 c0 {2,S}
        2 C  u0  p0 c0 {1,S} {3,D} {4,S}
        3 O  u0  p2 c0 {2,D}
        4 R  u0  px c0 {2,S}
        """,)
    },
    'C-XRCR2': {
        'gas_precursors': ['CH2CCH3', 'CH2COH', 'CHCCH2', 'CH2CH', 'CHCHCH3'],
        'adsorbates': ['CH2XCCH3', 'CH2XCOH', 'XCHCCH2', 'XCHCH2', 'XCHCHCH3'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0  p0 c0 {2,S}
        2 C  u0  p0 c0 {1,S} {3,D} {4,S}
        3 C  u0  p0 c0 {2,D} {5,S} {6,S}
        4 R  u0  px c0 {2,S}
        5 R  u0  px c0 {3,S}
        6 R  u0  px c0 {3,S}
        """,)
    },
    'C-XRNR': {
        'gas_precursors': ['CHNH', 'OHCNH', 'NH2CNH'],
        'adsorbates': ['XCHNH', 'OHXCNH', 'NH2XCNH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0  p0 c0 {2,S}
        2 C  u0  p0 c0 {1,S} {3,D} {4,S}
        3 N  u0  p1 c0 {2,D} {5,S}
        4 R  u0  px c0 {2,S}
        5 R  u0  px c0 {3,S}
        """,)
    },
    'C-XRN': {
        'gas_precursors': ['OCNH2', 'NH2CNH'],
        'adsorbates': ['OXCNH2', 'NH2XCNH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0  p0 c0 {2,S}
        2 C  u0  p0 c0 {1,S} {4,D} {3,S}
        3 N  u0  p1 c0 {2,S}
        4 R  u0  px c0 {2,D}
        """,)
    },
    'NX': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 {2,[S,D,T]}
        2 N  u0 {1,[S,D,T]}
        """,)
    },
    'N=XR': {
        'gas_precursors': ['NH'],
        'adsorbates': ['XNH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,D}
        2 N  u0 p1 c0 {1,D} {3,S}
        3 R  u0 px c0 {2,S}
        """,)
    },
    'N=XC-R': {
        'gas_precursors': ['NCH3'],
        'adsorbates': ['XNCH3'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,D}
        2 C  u0 p0 c0 {3,S} {4,S}
        3 N  u0 p1 c0 {1,D} {2,S}
        4 R  u0 px c0 {2,S}
        """,)
    },
    'N=XN': {
        'gas_precursors': ['NNH2'],
        'adsorbates': ['XNNH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,D}
        2 N  u0 p1 c0 {1,D} {3,S}
        3 N  u0 p1 c0 {2,S}
        """,)
    },
    'N=XOR': {
        'gas_precursors': ['NOH'],
        'adsorbates': ['XNOH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,D}
        2 N  u0 p1 c0 {1,D} {3,S}
        3 O  u0 p2 c0 {2,S} {4,S}
        4 R  u0 px c0 {3,S}
        """,)
    },
    'N=XC#R': {
        'gas_precursors': ['NCN'],
        'adsorbates': ['XNCN'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,D}
        2 N  u0 p1 c0 {1,D} {3,S}
        3 C  u0 p0 c0 {2,S} {4,T}
        4 R  u0 px c0 {3,T}
        """,)
    },
    'N-XR2': {
        'gas_precursors': ['NH2'],
        'adsorbates': ['XNH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,[S,D]}
        2 N u0 px cx {1,[S,D]} {3,[S,D]} {4,S}
        3 R u0 px c0 {2,[S,D]}
        4 R u0 px cx {2,S}
        """,)
    },
    'N-XRCR3': {
        'gas_precursors': ['NCH3'],
        'adsorbates': ['XNHCH3'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
        3 N  u0 p1 c0 {1,S} {2,S} {7,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        6 R  u0 px c0 {2,S}
        7 R  u0 px c0 {3,S}
        """,)
    },
    'N-XRNR2': {
        'gas_precursors': ['NHNH2'],
        'adsorbates': ['XNHNH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,S}
        2 N  u0 p1 c0 {1,S} {3,S} {4,S}
        3 N  u0 p1 c0 {2,S} {5,S} {6,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {3,S}
        6 R  u0 px c0 {3,S}
        """,)
    },
    'N-XROR': {
        'gas_precursors': ['NHOH'],
        'adsorbates': ['XNHOH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,S}
        2 N  u0 p1 c0 {1,S} {3,S} {4,S}
        3 O  u0 p2 c0 {2,S} {5,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {3,S}
        """,)
    },
    'N-XRNR': {
        'gas_precursors': ['ONNH'],
        'adsorbates': ['XNHNO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,S}
        2 N  u0 p1 c0 {1,S} {3,S} {4,S}
        3 N  u0 p1 c0 {2,S} {5,D}
        4 R  u0 px c0 {2,S}
        5 R!H  u0 px c0 {3,D}
        """,)
    },
    'N-XRCR': {
        'gas_precursors': ['OCHNH'],
        'adsorbates': ['XNHCHO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,S}
        2 N  u0 p1 c0 {1,S} {3,S} {4,S}
        3 C  u0 p0 c0 {2,S} {5,D}
        4 R  u0 px c0 {2,S}
        5 R!H  u0 px c0 {3,D}
        """,)
    },
    'N[+]-XR[-]R': {
        'gas_precursors': ['NO2', 'ONNH'],
        'adsorbates': ['XNO2', 'OXNNH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,S}
        2 N  u0 p0 c+1 {1,S} {3,S} {4,D}
        3 R!H  u0 px c-1 {2,S}
        4 R!H  u0 px c0 {2,D}
        """,)
    },
    'N[+]=XR[-]R': {
        'gas_precursors': ['HNO', 'CH3NNOH', 'CH3NNOH'],
        'adsorbates': ['HXNO', 'CH3NXNOH', 'CH3XNNOH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,D}
        2 N  u0 p0 c+1 {1,D} {3,S} {4,S}
        3 R!H  u0 px c-1 {2,S}
        4 R  u0 px c0 {2,S}
        """,)
    },
    'N-XR': {
        'gas_precursors': ['NO'],
        'adsorbates': ['XNO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,S}
        2 N  u0 p1 c0 {1,S} {3,D}
        3 R  u0 px c0 {2,D}
        """,)
    },
    'N-XCR2': {
        'gas_precursors': ['NCH2'],
        'adsorbates': ['XNCH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 C  u0 p0 c0 {3,D} {4,S} {5,S}
        3 N  u0 p1 c0 {1,S} {2,D}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        """,)
    },
    'N-XNR': {
        'gas_precursors': ['NNH', 'NNCH3'],
        'adsorbates': ['XNNH', 'XNNCH3'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,S}
        2 N  u0 p1 c0 {1,S} {3,D}
        3 N  u0 p1 c0 {2,D} {4,S}
        4 R  u0 px c0 {3,S}
        """,)
    },
    'N-XCR': {
        'gas_precursors': ['NCNH', 'OCN'],
        'adsorbates': ['XNCNH', 'XNCO'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,S}
        2 N  u0 p1 c0 {1,S} {3,D}
        3 C  u0 p0 c0 {2,D} {4,D}
        4 R!H  u0 px c0 {3,D}
        """,)
    },
    'OX': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 {2,[S,D]}
        2 O  ux {1,[S,D]}
        """,)
    },
    'O-XR': {
        'gas_precursors': ['OH'],
        'adsorbates': ['XOH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,S}
        2 O  u0 p2 c0 {1,S} {3,S}
        3 R  u0 px c0 {2,S}
        """,)
    },
    'O-XCR3': {
        'gas_precursors': ['OCH3', 'OCH2CH3', 'OCH2OH'],
        'adsorbates': ['XOCH3', 'XOCH2CH3', 'XOCH2OH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
        3 O  u0 p2 c0 {1,S} {2,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        6 R  u0 px c0 {2,S}
        """,)
    },
    'O-XCR2': {
        'gas_precursors': ['OCHCH2', 'HCOO', 'HCO3'],
        'adsorbates': ['XOCHCH2', 'HC(O)XO', 'XOC(OH)O'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 C  u0 p0 c0 {3,S} {4,S} {5,D}
        3 O  u0 p2 c0 {1,S} {2,S}
        4 R  u0 px c0 {2,S}
        5 R!H  u0 px c0 {2,D}
        """,)
    },
    'O-XN': {
        'gas_precursors': ['ONH2'],
        'adsorbates': ['XONH2'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {3,S}
        2 N  u0 p1 c0 {3,S}
        3 O  u0 p2 c0 {1,S} {2,S}

        """,)
    },
    'O-XOR': {
        'gas_precursors': ['OOH'],
        'adsorbates': ['XOOH'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0 {2,S}
        2 O  u0 p2 c0 {1,S} {3,S}
        3 O  u0 p2 c0 {2,S} {4,S}
        4 R  u0 p0 c0 {3,S}
        """,)
    },
    'RXvdW': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0
        2 R  u0
        """,)
    },
    '(CR4)X': {
        'gas_precursors': ['CH4'],
        'adsorbates': ['CH4X'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
        3 R  u0 px c0 {2,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        6 R  u0 px c0 {2,S}
        """,)
    },
    '(CR3CR3)X': {
        'gas_precursors': ['C2H6', 'CH3CH2CH3', 'CH3CH2OH'],
        'adsorbates': ['CH3CH3X', 'CH3CH2CH3X', 'CH3CH2OHX'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
        3 C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        6 R  u0 px c0 {2,S}
        7 R  u0 px c0 {3,S}
        8 R  u0 px c0 {3,S}
        9 R  u0 px c0 {3,S}
        """,)
    },
    '(CR3N)X': {
        'gas_precursors': ['CH3NH2'],
        'adsorbates': ['CH3NH2X'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
        3 N  u0 p1 c0 {2,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        6 R  u0 px c0 {2,S}
        """,)
    },
    '(CR3OR)X': {
        'gas_precursors': ['CH3OH', 'CH3OCH3', 'CH3OCH2OH', 'H2CO2H2'],
        'adsorbates': ['CH3OHX', 'CH3OCH3X', 'CH3OCH2OHX', 'H2C(OH)OHX'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
        3 O  u0 p2 c0 {2,S} {7,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        6 R  u0 px c0 {2,S}
        7 R  u0 p0 c0 {3,S}
        """,)
    },
    '(CR3)X': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X  u0
        2 C   u0 {3,D} {4,S} {5,S}
        3 R!H u0 {2,D}
        4 R   u0 {2,S}
        5 R   u0 {2,S}
        """,)
    },
    '(CR2N)X': {
        'gas_precursors': ['CH2NH'],
        'adsorbates': ['CH2NHX'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 C  u0 p0 c0 {3,D} {4,S} {5,S}
        3 N  u0 p1 c0 {2,D}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        """,)
    },
    '(CR2CR)X': {
        'gas_precursors': ['C2H4', 'CH3CHCH2', 'CH2CCH2'],
        'adsorbates': ['CH2CH2X', 'CH3CHCH2X', 'CH2CCH2X'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 C  u0 p0 c0 {3,D} {4,S} {5,S}
        3 C  u0 p0 c0 {2,D} {6,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        6 R  u0 px c0 {3,S}
        """,)
    },
    '(CR2O)X': {
        'gas_precursors': ['CH2CO', 'H2CO', 'OCO2H2', 'CH3CHO', 'HCOOH'],
        'adsorbates': ['CH2COX', 'CH2OX', 'OC(OH)OHX', 'CH3CHOX', 'HCOOHX'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 C  u0 p0 c0 {3,D} {4,S} {5,S}
        3 O  u0 p2 c0 {2,D}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        """,)
    },
    '(CR2)X': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X  u0
        2 C   u0 {3,T} {4,S}
        3 R!H u0 {2,T}
        4 R   u0 {2,S}
        """,)
    },
    '(CRN)X': {
        'gas_precursors': ['OHCN'],
        'adsorbates': ['NCOHX'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0  p0 c0
        2 C  u0  p0 c0 {3,T} {4,S}
        3 N  u0  p1 c0 {2,T}
        4 R  u0  px c0 {2,S}
        """,)
    },
    '(CRCR)X': {
        'gas_precursors': ['CHCH', 'CHCCH3'],
        'adsorbates': ['CHCHX', 'CHCCH3X'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 C  u0 p0 c0 {3,T} {4,S}
        3 C  u0 p0 c0 {2,T} {5,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {3,S}
        """,)
    },
    '(NR3)X': {
        'gas_precursors': ['NH3'],
        'adsorbates': ['NH3X'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 N  u0 p1 c0 {3,S} {4,S} {5,S}
        3 R  u0 px c0 {2,S}
        4 R  u0 px c0 {2,S}
        5 R  u0 px c0 {2,S}
        """,)
    },
    '(NN)X': {
        'gas_precursors': ['NH2NH2', 'NH2NCH3CH3'],
        'adsorbates': ['NH2NH2X', 'NH2NCH3CH3X'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 N  u0 p1 c0 {3,S}
        3 N  u0 p1 c0 {2,S}
        """,)
    },
    '(NO)X': {
        'gas_precursors': ['H2NOH'],
        'adsorbates': ['H2NOHX'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 N  u0 p1 c0 {3,S}
        3 O  u0 p2 c0 {2,S}
        """,)
    },
    '(NC)X': {
        'gas_precursors': ['OCHNH2'],
        'adsorbates': ['OCHNH2X'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 N  u0 p1 c0 {3,S}
        3 C  u0 p0 c0 {2,S}
        """,)
    },
    '(NR2)X': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 N   u0 p1 c0 {3,D} {4,S}
        3 R!H u0 px c0 {2,D}
        4 R   u0 px c0 {2,S}
        """,)
    },
    '(N=C)X': {
        'gas_precursors': ['OCNH', 'NHCNH'],
        'adsorbates': ['OCNHX', 'NHCNHX'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 N  u0 p1 c0 {3,D}
        3 C  u0 p0 c0 {2,D}
        """,)
    },
    '(OR2)X': {
        'gas_precursors': ['H2O'],
        'adsorbates': ['H2OX'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 O  u0 p2 c0 {3,S} {4,S}
        3 R  u0 p[0,1,2] c0 {2,S}
        4 R  u0 p[0,1,2] c0 {2,S}
        """,)
    },
    '(OROR)X': {
        'gas_precursors': ['HOOH'],
        'adsorbates': ['HOOHX'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 O  u0 p2 c0 {3,S} {4,S}
        3 O  u0 p2 c0 {2,S} {5,S}
        4 R  u0 p0 c0 {2,S}
        5 R  u0 p0 c0 {3,S}
        """,)
    },
    '(OR)X': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 O u0 p2 c0 {3,D}
        3 R u0 px c0 {2,D}
        """,)
    },
    '(ONR)X': {
        'gas_precursors': [],
        'adsorbates': [],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 O u0 p2 c0 {3,D}
        3 N u0 p1 c0 {2,D} {4,S}
        4 R u0 px c0 {3,S}
        """,)
    },
    '(ONOR)X': {
        'gas_precursors': ['ONOH'],
        'adsorbates': ['ONOHX'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 O u0 p2 c0 {3,D}
        3 N u0 p1 c0 {2,D} {4,S}
        4 O u0 p2 c0 {3,S} {5,S}
        5 R u0 px c0 {4,S}
        """,)
    },
    '(ONN)X': {
        'gas_precursors': ['ONNH2', 'ONNCH3CH3'],
        'adsorbates': ['ONNH2X', 'ONNCH3CH3X'],
        'connectivity_string': textwrap.dedent("""
        1 * X u0 p0 c0
        2 O u0 p2 c0 {3,D}
        3 N u0 p1 c0 {2,D} {4,S}
        4 N u0 p2 c0 {3,S}
        """,)
    },
}
