import numpy as np

class Adsorbate:

    def __init__(self, 
                 adsorbate_dict,
                 metal_dict,
                 P_ref = 1.0E5,  #Pa
                 NASA7_T_switch = 1000.0,  #K
                 twoD_gas_cutoff_frequency = 100.0,  #cm^{-1}
):
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
       
        self.P_ref = P_ref
        self.NASA7_T_switch = NASA7_T_switch
        self.twoD_gas_cutoff_frequency = twoD_gas_cutoff_frequency

        self._load_constants()
        self._get_adsorbate_mass()
        self._get_temperatures()
        self._check_if_2D_gas()

    def __repr__(self):
        return self.name

    def _get_adsorbate_mass(self):
        masses={'H': 1.01, 'C': 12.01, 'N': 14, 'O': 16}
        comp = self.composition
        self.adsorbate_mass=comp['H']*masses['H']
        self.adsorbate_mass+=comp['O']*masses['O']
        self.adsorbate_mass+=comp['C']*masses['C']
        self.adsorbate_mass+=comp['N']*masses['N']
        return

    def _get_temperatures(self):

        T0 = [298.15]
        T_low = 300.0
        T_high = 2000.0
        dT = 10.0 #temperature increment
        self.temperatures = np.append(T0, np.arange(T_low, T_high+dT, dT))
        return

    def _load_constants(self):
        self.R = 8.3144621E-3 #ideal Gas constant in kJ/mol-K
        self.kB = 1.38065e-23 #Boltzmann constant in J/K
        self.h = 6.62607e-34 #Planck constant in J*s
        self.c = 2.99792458e8 #speed of light in m/s
        self.amu = 1.6605e-27 #atomic mass unit in kg
        self.Avogadro = 6.0221E23 #mole^-1
        self.GHz_to_Hz = 1.0E9 #convert rotational constants from GHz to Hz
        self.invcm_to_invm = 1.0E2 #convert cm^-1 to m^-1, for frequencies
        self.hartree_to_kcalpermole = 627.5095 #convert hartree/molecule to kcal/mol
        self.hartree_to_kJpermole = 2627.25677 #convert hartree/molecule to kJ/mol
        self.eV_to_kJpermole = 96.485 #convert eV/molecule to kJ/mol
        self.eV_to_kJpermole = 96.485 #convert eV/molecule to kJ/mol
        return

    def _check_if_2D_gas(self):
        freq = self.frequencies
        if np.min(freq[0:2]) <= 100:
            self.twoD_gas = True
        return

    def get_2D_translational_thermo(self):
        
        area = self.unit_cell_area
        sites = self.sites
        pi = np.pi
        temps = self.temperatures
        m = self.adsorbate_mass
        h = self.h
        amu = self.amu
        kB = self.kB
        R = self.R

        q_trans  = np.ones(len(temps)) 
        S_trans  = np.zeros(len(temps))
        dH_trans  = np.zeros(len(temps))
        Cp_trans  = np.zeros(len(temps))

        for i, T in enumerate(temps):
            
            q_trans[i] = (2*pi*m*amu*kB*T/h**2) * area * sites
            S_trans[i] = R * (2.0 + np.log(q_trans[i]))
            Cp_trans[i] = R
            dH_trans[i] = R * T            
   
        return q_trans, S_trans, dH_trans, Cp_trans

    def get_vibrational_thermo(self):

        units = self.h * self.c / self.kB * self.invcm_to_invm # K * cm
        amu = self.amu
        kB = self.kB
        h = self.h
        P_ref = self.P_ref
        mass = self.adsorbate_mass
        temps = self.temperatures
        
        q_vib  = np.ones(len(temps))
        S_vib  = np.zeros(len(temps))
        dH_vib  = np.zeros(len(temps))
        Cv_vib  = np.zeros(len(temps))
    
        for t,temp in enumerate(temps):
            for (n,nu) in enumerate(self.frequencies[0:-1]):
                if self.twoD_gas==True and n <= 1:
                    pass
                else:
                    x = nu * units / temp #cm^-1 * K cm / K = dimensionless
                    q_vib[t]  *= 1.0 / (1.0 - np.exp( - x) )
                    qterm = 1.0 - np.exp( - x)
                    S_vib[t]  += -np.log(qterm) + x * np.exp( - x) / qterm 
                    dH_vib[t] += x * np.exp(-x) / qterm 
                    Cv_vib[t] += x ** 2.0 * np.exp( - x) / qterm ** 2.0
            S_vib[t]  *= self.R
            dH_vib[t] *= self.R * temp
            Cv_vib[t] *= self.R
        return q_vib, S_vib, dH_vib, Cv_vib

    def get_thermo(self):
        '''write me'''
        return Q, S, dH, Cp

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
    """
