long_description = ''' '''

gas_list = [
    dict(
        gas_name='CNH2',
        heat_of_formation_0K=[371.9, 'kJ/mol'],
        gas_composition={'H': 2, 'C': 1, 'N': 1, 'O': 0, 'slab': 0},
        dft_energy=[-699.3467921, 'eV'],
        zpe=[1.075184923, 'eV'],
        frequencies=[722.7650129804078, 1002.8384193952513, 1401.9584267859707, 1595.4432105223648, 3252.463285096595, 3274.22867029891, 'cm-1'],
        symmetry_number=[2],
        electronic_degeneracy=[2],
        rotational_constants=[341.68, 37.8, 34.03, 'GHZ'],
        ),
    dict(
        gas_name='CNO',
        heat_of_formation_0K=[389.4, 'kJ/mol'],
        gas_composition={'H': 0, 'C': 1, 'N': 1, 'O': 1, 'slab': 0},
        dft_energy=[-1224.50919, 'eV'],
        zpe=[0.2296, 'eV'],
        frequencies=[315.5329272788069, 336.26126848926395, 1163.119928740231, 1868.0009705958814, 'cm-1'],
        symmetry_number=[1],
        electronic_degeneracy=[2],
        rotational_constants=[12.2, 12.2, 'GHZ'],
        ),
        ]

adsorbate_list = [
    {
        "adsorbate_name": "XCNH2",
        "adsorbate_composition": {
            "H": 2,
            "C": 1,
            "N": 1,
            "O": 0,
            "slab": 1
        },
        "dft_energy": [
            -378301.7456,
            "eV"
        ],
        "zpe": [
            0.817,
            "eV"
        ],
        "frequencies": [
            153.85,
            155.91,
            188.72,
            303.19,
            377.55,
            419.76,
            512.53,
            1090.92,
            1299.32,
            1582.57,
            3483.73,
            3605.26,
            "cm-1"
        ],
        "sites_occupied": 1,
        "connectivity": "1 X  u0 p0 c0 {2,T}\n2 C  u0 p0 c0 {1,T} {3,S}\n3 N  u0 p1 c0 {2,S} {4,S} {5,S}\n4 H  u0 p0 c0 {3,S}\n5 H  u0 p0 c0 {3,S}\n"
    },
    {
        "adsorbate_name": "XCNO",
        "adsorbate_composition": {
            "H": 0,
            "C": 1,
            "N": 1,
            "O": 1,
            "slab": 1
        },
        "dft_energy": [
            -378843.7773,
            "eV"
        ],
        "zpe": [
            0.301,
            "eV"
        ],
        "frequencies": [
            67.9,
            67.9,
            242.8,
            242.8,
            246.3,
            418.4,
            418.4,
            1193.2,
            1960.0,
            "cm-1"
        ],
        "sites_occupied": 1,
        "connectivity": "1 X  u0  p0  c0  {2,T}\n2 C  u0  p0  c0  {1,T}, {3,S}\n3 N  u0  p1  c0  {2,S} {4,D}\n4 O  u0  p2  c0  {3,D}\n"
    },
]