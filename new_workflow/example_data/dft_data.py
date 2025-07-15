import textwrap


long_description = '''
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.'''

OXCXCH2 = dict(
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
