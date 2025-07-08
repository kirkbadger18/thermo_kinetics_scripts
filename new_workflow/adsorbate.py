class Adsorbate:

    def __init__(self, adsorbate_dict, metal_dict):
        """
        This dictionary should be structured like:
        Adsorbate_dict = dict(
                            name= NAME,
                            dft_energy = E,
                            zpe = ZPE,
                            frequencies = FREQUENCIES,
                            sites = Sites,
                            beef_energies = Beef_Energies,
                            composition = dict(C=a,H=b,O=c,N=d),
                            )    
        and Metal_dict should look like:
        Pt_data = dict(
                reference_compositions={"CH4": {"C": 1,  "O": 0, "H":4, "Pt": 0},
                                        "H2O": {"C": 0, "O": 1, "H":2, "Pt": 0},
                                        "H2": {"C": 0, "O": 0, "H":2, "Pt": 0},
                                        "X": {"C": 0, "O": 0, "H":0, "Pt": 1},
                                        },
                reference_energies= {"CH4":-324.294,
                                     "H2O":-611.0186083,
                                     "H2": -32.6984442,
                                     "Pt":-377616.072,
                                    },
                reference_EOF={"CH4":-66.557,
                               "H2O":-238.929,
                               "H2":0,
                               "Pt":0,
                              },
                unit_cell_area = 62.105e-20/9.0,
                )
        """                    
        self.name = adsorbate_dict['name']
        self.composition = adsorbate_dict['composition']
        self.dft_energy = adsorbate_dict['dft_energy']
        self.zpe = adsorbate_dict['zpe']
        self.frequencies = adsorbate_dict['frequencies']
        self.sites = adsorbate_dict['sites']
        self.beef_energies = adsorbate_dict['beef_energies']
        self.reference_compositions = metal_dict
        self.reference_energies = metal_dict['reference_energies']
        self.unit_cell_area = metal_dict['unit_cell_area']

    def __repr__(self):
        return self.name

    def get_2D_translational_thermo(self):
        '''write me'''
        return H_trans, S_trans, Cp_trans

    def get_vibrational_thermo(self):
        '''write me'''
        return H_vib, S_vib, Cp_vib

    def get_thermo(self):
        '''write me'''
        return H, S, Cp

    def fit_NASA7_polynomial(self):
        '''write me'''
        return params

    def plot_NASA_fit(self):
        '''write me'''
        return None

    def get_RMG_thermo_database_entry(self):
        '''write me'''
        return string

    """
    to do:
        - write the "write mes"
        - add some functions to get beef ensemble of NASA7 polynomials
        - think of file format to store and read in beef_energies, 
          maybe with np.savetxt, np.loadtxt, or maybe pandas
        - Create a class Adsorbates, which can handle lists of adsorbate_dicts,
          and make RMG thermo files entirely.

