from data.Pt111_ads_data import Pt111_ads_data
from data.reference_data import reference_dict
from data.slab_data import slab_dict
import sys
sys.path.append('../../')
from adsorbate import Adsorbates

long_description = '''
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.'''

ads_list = Adsorbates(Pt111_ads_data,
                      reference_dict,
                      slab_dict,
                      long_description)

ads_list.write_RMG_thermolib("surfaceThermoPt111_adsorbed_refs.py")