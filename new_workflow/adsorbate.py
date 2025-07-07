class Adsorbate:

    def __init__(self, Adsorbate_dict):
        """
        This dictionary should be structured like:
        Adsorbate_dict = dict(
                            name= NAME,
                            DFT_Energy = E,
                            zpe = ZPE,
                            composition = dict(C=a,H=b,O=c,N=d)
                            ref_data_file = PATH/TO/Ref_species
                            beef_data_file = PATH/beef/data
        """                    
        self.Adsorbate_dict = Adsorbate_dict

    def get_translational_thermo():

        return H_trans, S_trans, Cp_trans

    def get_rotational_thermo():

        return H_rot, S_rot, Cp_rot

    def get_vibrational_thermo():

        return H_vib, S_vib, Cp_vib

    def get_thermo():

        return H, S, Cp

    def fit_NASA7_polynomial()

        return params

    def plot_NASA_fit():

        return None

    def get_RMG_thermo_database_entry():

        return string


class Reacrion:

    def ...
