from adsorbate import Adsorbate
from gas import Gas
import numpy as np


class Group:

    def __init__(self,
                 adsorbate_list,
                 gas_list,
                 reference_dict,
                 slab_dict,
                 long_description=' ',
                 P_ref=1.0E5,  # Pa
                 NASA7_T_switch=1000.0,  # K
                 twoD_gas_cutoff_frequency=100.0,
                 ):

        self.adsorbate_list = []
        for ads_dict in adsorbate_list:
            ads = Adsorbate(ads_dict, reference_dict, slab_dict,
                            long_description, P_ref, NASA7_T_switch,
                            twoD_gas_cutoff_frequency)
            self.adsorbate_list.append(ads)

        self.gas_list = []
        for gas_dict in gas_list:
            gas = Gas(gas_dict, reference_dict, long_description, P_ref,
                      NASA7_T_switch)
            self.gas_list.append(gas)
        return

    def get_group_correction(self):
        dH_list, dS_list = [], []
        dcP_array = np.zeros([7, len(self.adsorbate_list)])
        for i, ads in enumerate(self.adsorbate_list):
            Qa, Sa, Ha, cPa = ads.get_thermo()
            gas = self.gas_list[i]
            print(ads.fit_NASA7_polynomial())
            Qg, Sg, Hg, cPg = gas.get_thermo()
            dH_list.append(float(Ha[0] - Hg[0]))
            dS_list.append(1e3*(float(Sa[0] - Sg[0])))
            temps = gas.temperatures
            desired_temps = [300, 400, 500, 600, 800, 1000, 1500]
            count = 0
            for j, T in enumerate(temps):
                if T in desired_temps:
                    dcP_array[count, i] = 1e3*(float(cPa[j] - cPg[j]))
                    count += 1
        dH = np.mean(dH_list)
        dS = np.mean(dS_list)
        dcP = np.mean(dcP_array, axis=1)
        return dH, dS, dcP
        
                







