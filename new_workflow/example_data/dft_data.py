import textwrap


long_description = '''
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.'''

adsorbate = dict(
            adsorbate_name = 'OXCXCH2',
            adsorbate_composition = {'H':2, 'C':2, 'N':0, 'O':1},
            dft_energy = [-378744.484815, 'eV'],
            zpe = [0.930, 'eV'],
            frequencies = [58.5,150.3,163.9,284.7,443.7,445.6,618.1,682.8,894.5,1032.6,1050.4,1361.4,1738.5,3001.1,3074.3, 'cm-1'],
            sites_occupied = 2,
            beef_energies = None,
            connectivity = textwrap.dedent(
            '''
            1 X u0 p0 c0 {3,S}
            2 X u0 p0 c0 {4,S}
            3 C u0 p0 c0 {1,S} {4,S} {5,D}
            4 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
            5 O u0 p2 c0 {3,D}
            6 H u0 p0 c0 {4,S}
            7 H u0 p0 c0 {4,S}
            '''
            ),
        )


adsorbate_list = [
        dict(
            adsorbate_name = 'OXCXCH2',
            adsorbate_composition = {'H':2, 'C':2, 'N':0, 'O':1},
            dft_energy = [-378744.484815, 'eV'],
            zpe = [0.930, 'eV'],
            frequencies = [58.5,150.3,163.9,284.7,443.7,445.6,618.1,682.8,894.5,1032.6,1050.4,1361.4,1738.5,3001.1,3074.3, 'cm-1'],
            sites_occupied = 2,
            connectivity = textwrap.dedent(
            '''
            1 X u0 p0 c0 {3,S}
            2 X u0 p0 c0 {4,S}
            3 C u0 p0 c0 {1,S} {4,S} {5,D}
            4 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
            5 O u0 p2 c0 {3,D}
            6 H u0 p0 c0 {4,S}
            7 H u0 p0 c0 {4,S}
            '''
            ),
        ),
        dict(
            adsorbate_name = 'XNO',
            adsorbate_composition = {'H':0, 'C':0, 'N':1, 'O':1},
            dft_energy = [-378586.3267, 'eV'],
            zpe = [0.18, 'eV'],
            frequencies = [155.09, 155.14, 290.49, 412.18, 412.21, 1473.12, 'cm-1'],
            sites_occupied = 1,
            connectivity = textwrap.dedent(
            '''
            1 X  u0 p0 c0 {2,S}
            2 N  u0 p1 c0 {1,S} {3,D}
            3 O  u0 p2 c0 {2,D}
            '''
            ),
        ),
        dict(
            adsorbate_name = 'XNO2',
            adsorbate_composition = {'H':0, 'C':0, 'N':1, 'O':2},
            dft_energy = [-379163.0881, 'eV'],
            zpe = [0.288, 'eV'],
            frequencies = [31.35, 43.35, 60.55, 234.48, 272.57, 520.52, 766.17, 1249.65, 1461.41, 'cm-1'],
            sites_occupied = 1,
            connectivity = textwrap.dedent(
            '''
            1 X  u0  p0 c0  {2,S}
            2 N  u0  p0 c+1  {1,S} {3,D} {4,S}
            3 O  u0  p2 c0  {2,D}
            4 O  u0  p3 c-1  {2,S}
            '''
            ),
        ),
]
