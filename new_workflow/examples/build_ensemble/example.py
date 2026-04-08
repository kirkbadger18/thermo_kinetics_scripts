from data.Pt111_ads_data import Pt111_ads_data
from data.reference_data import reference_dict
from data.slab_data import slab_dict
from data.beefdict import beefdict
from data.refbeefdict import refbeefdict
from data.tree import RX
from data.group_data import group_data
from data.gas_data import gas_lib

import sys
sys.path.append('../../')
from adsorbate import AdsorbatesEnsemble, Adsorbates
from adsorption_correction import AdsorptionCorrectionTreeEnsemble, AdsorptionCorrectionTree

long_description = '''
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.'''


N_members = 40

ads_list = AdsorbatesEnsemble(Pt111_ads_data,
                              reference_dict,
                              slab_dict,
                              long_description,
                              beefdict,
                              refbeefdict,
                              )
ads_list.write_ensemble_of_RMG_thermodatabase_files(
    directory='thermolib/',
    file_prefix='surfaceThermoPt111',
    max_members=N_members)

correns = AdsorptionCorrectionTreeEnsemble(
    RX,
    group_data,
    Pt111_ads_data,
    gas_lib,
    reference_dict,
    slab_dict,
    beefdict,
    refbeefdict,
)

correns.write_files(
    directory="adscorr/",
    file_prefix="adsorptionPt111",
    max_members=N_members,
)

tree = AdsorptionCorrectionTree(RX,
                                group_data,
                                Pt111_ads_data,
                                gas_lib,
                                reference_dict,
                                slab_dict)

tree.write_RMG_adsorption_correction_file('adscorr/adsorptionPt111.py',
                                          ' ',
                                          )

ads_list = Adsorbates(Pt111_ads_data,
                      reference_dict,
                      slab_dict,
                      long_description)

ads_list.write_RMG_thermodatabase_file("thermolib/surfaceThermoPt111.py")
