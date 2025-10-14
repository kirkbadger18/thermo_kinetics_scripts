import sys
sys.path.append('../../')
from data.reference_data import reference_dict
from data.slab_data import slab_dict
from data.gas_data import gas_lib
from data.Pt111_ads_data import Pt111_ads_lib
from data.tree import RX
from data.group_data import group_data

from adsorption_correction import AdsorptionCorrectionTree

tree = AdsorptionCorrectionTree(RX,
                                group_data,
                                Pt111_ads_lib,
                                gas_lib,
                                reference_dict,
                                slab_dict)

tree.write_RMG_adsorption_correction_file('adsorptionPt111.py',
                                          ' ',
                                          )
