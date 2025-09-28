from data.Pt111_ads_data import Pt111_ads_data
from data.reference_data import reference_dict
from data.slab_data import slab_dict
from data.beefdict import beefdict
from data.refbeefdict import refbeefdict

import sys
sys.path.append('../../')
from adsorbate import AdsorbatesEnsemble

long_description = '''
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.'''

ads_list = AdsorbatesEnsemble(Pt111_ads_data,
                              reference_dict,
                              slab_dict,
                              long_description,
                              beefdict,
                              refbeefdict,
                              )
ads_list.write_RMG_thermolib('database_ensemble/surfaceThermoPt111_adsorbed_refs.py')

#ads_list.write_ensemble_of_thermodatabase_files(directory='database_ensemble/',
#                                                file_prefix="surfaceThermoPt111_adsorbed_refs",
#                                                max_members=10,
#                                                )