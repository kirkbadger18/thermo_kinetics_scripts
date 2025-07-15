import numpy as np

class Adsorbate:

    def __init__(self, 
                 adsorbate_dict,
                 reference_dict,
                 slab_energy,
                 unit_cell_area, 
                 P_ref = 1.0E5,  #Pa
                 NASA7_T_switch = 1000.0,  #K
                 twoD_gas_cutoff_frequency = 100.0,  #cm^{-1}
):
        """
        These dictionarys should be structured like:
        adsorbate_dict = dict(
                            adsorbate_name= string,
                            dft_energy = float,
                            zpe = float,
                            frequencies = list,
                            sites_occupied = float,
                            beef_energies = list,
                            adsorbate_composition = {"C": int,  "O": int, "H": int, "N": int},
                            )    
        reference_dict = dict(
                reference_compositions={"CH4": {"C": int,  "O": int, "H": int, "N": int},
                                        "H2O": {"C": int, "O": int, "H":2, "N": int},
                                        "H2": {"C": int, "O": int, "H":2, "N": int},
                                        },
                reference_energies= {"CH4":float,
                                     "H2O":float,
                                     "H2": float,
                                     "NH3: float,
                                    },
                reference_EOF={"CH4": float,
                               "H2O": float,
                               "H2": float,
                               "NH3": float
                              },
                )
        """                    
        self.adsorbate_name = adsorbate_dict['adsorbate_name']
        self.adsorbate_composition = adsorbate_dict['adsorbate_composition']
        self.dft_energy = adsorbate_dict['dft_energy']
        self.zpe = adsorbate_dict['zpe']
        self.frequencies = adsorbate_dict['frequencies']
        self.sites_occupied = adsorbate_dict['sites_occupied']
        self.beef_energies = adsorbate_dict['beef_energies']
        self.reference_compositions = reference_dict['reference_compositions']
        self.reference_energies = reference_dict['reference_energies']
        self.reference_EOF = reference_dict['reference_EOF']
        self.unit_cell_area = unit_cell_area
        self.slab_energy = slab_energy

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
        comp = self.adsorbate_composition
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
        return

    def _check_if_2D_gas(self):
        freq = self.frequencies
        if np.min(freq[0:2]) <= 100:
            self.twoD_gas = True
        return

    def get_0K_heat_of_formation(self):

        comp = self.adsorbate_composition
        comp_keys = list(comp.keys())
        ref_comp = self.reference_compositions 
        ref_mol_keys=list(ref_comp.keys())
        
        num_elements = len(comp_keys)
        num_references = len(ref_mol_keys)

        N = np.zeros(num_elements)
        for i, key in enumerate(comp_keys):
            N[i] = comp[key]

        N_R = np.zeros((num_references, num_elements))
        for i, mol_key in enumerate(ref_mol_keys):
            for j, key in enumerate(comp_keys):
                N_R[i,j] = ref_comp[mol_key][key]

        M=-N.dot(np.linalg.inv(N_R))

        H_ref=np.array(list(self.reference_EOF.values()))
        E_ref=np.array(list(self.reference_energies.values()))

        E=self.dft_energy[0]+self.zpe[0] - self.slab_energy
        E_kJ = E * self.eV_to_kJpermole
        E_ref_term = M.dot(E_ref) * self.eV_to_kJpermole
        H_ref_term = M.dot(H_ref)
        HOF_0K = (E_kJ + E_ref_term - H_ref_term)
        return HOF_0K

    def get_2D_translational_thermo(self):
        
        area = self.unit_cell_area
        sites = self.sites_occupied
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
        if self.twoD_gas:
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

        h_correction = 4.234 #kJ/mol. enthalpy_H(298) - enthalpy_H(0)
        c_correction = 1.051 #kJ/mol. enthalpy_C(298) - enthalpy_C(0)
        n_correction = 4.335 #kJ/mol. enthalpy_N(298) - enthalpy_N(0)
        o_correction = 4.340 #kJ/mol. enthalpy_O(298) - enthalpy_O(0)
    
        HOF_correction = 0.0
        comp = self.adsorbate_composition
        HOF_correction += comp['H'] * h_correction
        HOF_correction += comp['C'] * c_correction    
        HOF_correction += comp['N'] * n_correction
        HOF_correction += comp['O'] * o_correction        
   
        q_t, S_t, dH_t, Cp_t = self.get_2D_translational_thermo()
        q_v, S_v, dH_v, Cv_v = self.get_vibrational_thermo()

        Q = q_v * q_t
        S = S_t + S_v 
        dH = dH_t + dH_v 
        Cp = Cp_t + Cv_v
        HOF_0K = self.get_0K_heat_of_formation()
        HOF_298K = HOF_0K + dH[0] - HOF_correction
        H = HOF_298K + dH - dH[0] 
        return Q, S, H, Cp

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
