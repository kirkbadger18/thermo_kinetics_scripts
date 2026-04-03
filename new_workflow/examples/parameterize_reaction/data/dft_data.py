import textwrap


long_description = '''
Data from NOx study
'''

reactants = [
        dict(
            adsorbate_name='XNO',
            atomic_composition={'H': 0, 'C': 0, 'N': 1, 'O': 1, 'slab': 1},
            bond_composition={},
            dft_energy=[-378586.3267, 'eV'],
            zpe=[0.180, 'eV'],
            frequencies=[155.09, 155.14, 290.49, 412.18, 412.21, 1473.12, 'cm-1'],
            sites_occupied=1,
            connectivity=textwrap.dedent(
            '''

            '''
            ),
        ),
        dict(
            adsorbate_name='XNO2',
            atomic_composition={'H': 0, 'C': 0, 'N': 1, 'O': 2, 'slab': 1},
            bond_composition={},
            dft_energy=[-379163.0881, 'eV'],
            zpe=[0.288, 'eV'],
            frequencies=[31.35, 43.35, 60.55, 234.48, 272.57, 520.52, 766.17, 1249.65, 1461.41, 'cm-1'],
            sites_occupied=1,
            connectivity=textwrap.dedent(
            '''

            '''
            ),
        ),
]

first_order_saddle_points = [
        dict(
            adsorbate_name='XN-O',
            atomic_composition={'H': 0, 'C': 1, 'N': 0, 'O': 2, 'slab': 1},
            bond_composition={},
            dft_energy=[-378584.0757, 'eV'],
            zpe=[0.118, 'eV'],
            frequencies=[211.5, 241.1, 425.7, 469.4, 548.7, 'cm-1'],
            sites_occupied=1,
            connectivity=textwrap.dedent(
            '''

            '''
            ),
        ),
        dict(
            adsorbate_name='OXN-O',
            atomic_composition={'H': 0, 'C': 1, 'N': 0, 'O': 1, 'slab': 1},
            bond_composition={},
            dft_energy=[-379162.4383, 'eV'],
            zpe=[0.217, 'eV'],
            frequencies=[79.1, 134.7, 162.3, 225.6, 299.0, 334.7, 664.8, 1606.5, 'cm-1'],
            sites_occupied=1,
            connectivity=textwrap.dedent(
            '''

            '''
            ),
        ),
]
