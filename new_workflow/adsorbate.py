import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import NullFormatter, MaxNLocator, LogLocator

class Adsorbate:

    def __init__(self, 
                 adsorbate_dict,
                 reference_dict,
                 slab_dict,
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
        self.connectivity = adsorbate_dict['connectivity']

        self.reference_compositions = reference_dict['reference_compositions']
        self.reference_energies = reference_dict['reference_energies']
        self.reference_EOF = reference_dict['reference_EOF']
        
        self.unit_cell_area = slab_dict['unit_cell_area']
        self.slab_energy = slab_dict['slab_energy']
        self.metal = slab_dict['metal']
        self.facet = slab_dict['facet']

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
        self.twoD_gas = False
        if np.max(freq[0:2]) <= 100:
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
        self.HOF_298K = HOF_0K + dH[0] - HOF_correction
        H = self.HOF_298K + dH - dH[0] 
        return Q, S, H, Cp

    def fit_NASA7_polynomial(self):
        R = self.R
        Q, S, H, Cp = self.get_thermo()
        H0 = H[0]
        S0 = S[0]
        T_switch = self.NASA7_T_switch
        temps=self.temperatures

        i_switch = -1
        for i in range(len(temps)):
            if temps[i]==T_switch:
                i_switch = i
        if i_switch==-1:
            print("We have a problem! Cannot find switching temperature")
        
    
        #start by creating the independent variable matrix for the low-temperature fit
        YT = np.array([np.ones(len(temps[:i_switch+1])),
                       temps[:i_switch+1],
                       temps[:i_switch+1]**2.0,
                       temps[:i_switch+1]**3.0,
                       temps[:i_switch+1]**4.0,
                       ],
                    dtype=np.float64,
                    )
        Y = YT.T

        b = Cp[:i_switch+1] / R  
        a_low = np.linalg.lstsq(Y, b, rcond=None)[0]

        T_ref = 298.15
        #now determine the enthalpy coefficient for the low-T region
        subtract = a_low[0] + a_low[1]/2.0*T_ref + a_low[2]/3.0*T_ref**2.0 + a_low[3]/4.0*T_ref**3.0  + a_low[4]/5.0*T_ref**4.0
        a_low = np.append(a_low, H0 / R - subtract * T_ref)
        #now determine the entropy coefficient for the low-T region
        subtract = a_low[0] * np.log(T_ref) + a_low[1]*T_ref     + a_low[2]/2.0*T_ref**2.0  + a_low[3]/3.0*T_ref**3.0  + a_low[4]/4.0*T_ref**4.0
        a_low = np.append(a_low, S0 / R - subtract )

        #
        # NOW SWITCH TO HIGH-TEMPERATURE REGIME!
        #
        T_ref = T_switch
        #compute the heat capacity, enthalpy, and entropy at the switching point
        Cp_switch = a_low[0] + a_low[1]*T_ref + a_low[2]*T_ref**2.0  + a_low[3]*T_ref**3.0  + a_low[4]*T_ref**4.0
        H_switch = a_low[0]*T_ref + a_low[1]/2.0*T_ref**2.0 + a_low[2]/3.0*T_ref**3.0  + a_low[3]/4.0*T_ref**4.0  + a_low[4]/5.0*T_ref**5.0 + a_low[5]
        S_switch = a_low[0]*np.log(T_ref) + a_low[1]*T_ref + a_low[2]/2.0*T_ref**2.0  + a_low[3]/3.0*T_ref**3.0  + a_low[4]/4.0*T_ref**4.0 + a_low[6]
    
        #now repeat the process for the high-temperature regime
        a_high = [0.0]
        YT = np.array([temps[i_switch:],
                       temps[i_switch:]**2.0,
                       temps[i_switch:]**3.0,
                       temps[i_switch:]**4.0,
                       ],
                      dtype=np.float64,
                      )
        Y = YT.transpose()

        b = Cp[i_switch:] / R - Cp_switch
        a_high = np.append(a_high, np.linalg.lstsq(Y, b, rcond=None)[0])
        a_high[0] = Cp_switch - (a_high[0] + a_high[1]*T_switch + a_high[2]*T_switch**2.0  + a_high[3]*T_switch**3.0  + a_high[4]*T_switch**4.0)
    
        a_high = np.append(a_high, H_switch - (a_high[0] + a_high[1]/2.0*T_ref + a_high[2]/3.0*T_ref**2.0  + a_high[3]/4.0*T_ref**3.0  + a_high[4]/5.0*T_ref**4.0)*T_ref )
        a_high = np.append(a_high, S_switch - (a_high[0]*np.log(T_ref) + a_high[1]*T_ref + a_high[2]/2.0*T_ref**2.0  + a_high[3]/3.0*T_ref**3.0  + a_high[4]/4.0*T_ref**4.0) )

    
        line = '    thermo = NASA(\n'
        line += "        polynomials = [\n"
        line += "            NASAPolynomial(coeffs=[%.8E, %.8E, %.8E, %.8E, %.8E, %.8E, %.8E], Tmin=(%.1F, 'K'), Tmax=(%.1F, 'K')), \n"%(a_low[0], a_low[1], a_low[2], a_low[3], a_low[4], a_low[5], a_low[6], 298.0, 1000.0)
        line += "            NASAPolynomial(coeffs=[%.8E, %.8E, %.8E, %.8E, %.8E, %.8E, %.8E], Tmin=(%.1F, 'K'), Tmax=(%.1F, 'K')), \n"%(a_high[0], a_high[1], a_high[2], a_high[3], a_high[4], a_high[5], a_high[6], 1000.0, max(temps))
        line += "        ],\n"
        line += "        Tmin = (%.1F,'K'),\n"%(298)
        line += "        Tmax = (%.1F,'K'),\n"%(max(temps))
        line += "    ),\n"
    
    
        #molecule.thermo_lines = line
        #molecule.a_low = a_low
        #molecule.a_high = a_high

        return a_low, a_high

    def get_thermo_from_NASA(self):
        a_low, a_high = self.fit_NASA7_polynomial()
        R = self.R
        T_switch = self.NASA7_T_switch
        temps = self.temperatures
        i_switch = -1
        for i in range(len(temps)):
            if temps[i]==T_switch:
                i_switch = i
    
        cp_fit = np.zeros(len(temps))
        h_fit = np.zeros(len(temps))
        s_fit = np.zeros(len(temps))

        for (i,temp) in enumerate(temps):
            if temp <= T_switch:
                cp_fit[i] = a_low[0] + a_low[1]*temp + a_low[2]*temp**2.0  + a_low[3]*temp**3.0  + a_low[4]*temp**4.0
                h_fit[i] = a_low[0]*temp + a_low[1]/2.0*temp**2.0 + a_low[2]/3.0*temp**3.0  + a_low[3]/4.0*temp**4.0  + a_low[4]/5.0*temp**5.0 + a_low[5]
                s_fit[i] = a_low[0]*np.log(temp) + a_low[1]*temp + a_low[2]/2.0*temp**2.0  + a_low[3]/3.0*temp**3.0  + a_low[4]/4.0*temp**4.0 + a_low[6]
            else:
                cp_fit[i] = a_high[0] + a_high[1]*temp + a_high[2]*temp**2.0  + a_high[3]*temp**3.0  + a_high[4]*temp**4.0
                h_fit[i] = a_high[0]*temp + a_high[1]/2.0*temp**2.0 + a_high[2]/3.0*temp**3.0  + a_high[3]/4.0*temp**4.0  + a_high[4]/5.0*temp**5.0 + a_high[5]
                s_fit[i] = a_high[0]*np.log(temp) + a_high[1]*temp + a_high[2]/2.0*temp**2.0  + a_high[3]/3.0*temp**3.0  + a_high[4]/4.0*temp**4.0 + a_high[6]

        cp_fit *= R        
        h_fit *= R  
        s_fit *= R

        return s_fit, h_fit, cp_fit

    def plot_NASA_fit(self):
        
        S_fit, H_fit, Cp_fit = self.get_thermo_from_NASA()
        Q, S, H, Cp = self.get_thermo()
        HOF_298 = self.HOF_298K
        fig = plt.figure(dpi=300,figsize=(12,4))
        gs = gridspec.GridSpec(1, 3)
        gs.update(wspace=0.5, hspace=0.4)
        ax0 = plt.subplot(gs[0])
        ax1 = plt.subplot(gs[1])
        ax2 = plt.subplot(gs[2])
        temps = self.temperatures
        ax0.plot(temps, Cp, marker='o', markeredgecolor='r',color='w',alpha=0.5,linestyle='None',label='stat. mech.')
        ax0.plot(temps, Cp_fit, 'b', linewidth=2,label='NASA')
        ax1.semilogy(temps, H - HOF_298, marker='o', markeredgecolor='r',color='w',alpha=0.5,linestyle='None')
        ax1.semilogy(temps, H_fit - HOF_298, 'b', linewidth=2)
        ax2.semilogy(temps, S, marker='o', markeredgecolor='r',color='w',alpha=0.5,linestyle='None')
        ax2.semilogy(temps, S_fit, 'b', linewidth=2)
        ax0.set_ylim(min(Cp_fit)*0.9, max(Cp_fit)*1.025)
        ax1.set_ylim(top=max(H - HOF_298)*1.025)
        ax2.set_ylim(10e-3*0.9, max(S_fit)*1.025)
        ax1.yaxis.set_major_locator(LogLocator(base=10.0, numticks=4))
        ax2.yaxis.set_major_locator(LogLocator(base=10.0, numticks=4))
       
        for ax in [ax0, ax1, ax2]:
            ax.set_xlim(min(temps)*0.95, max(temps)*1.025)
            ax.xaxis.set_major_locator(MaxNLocator(4))
            ax.tick_params(axis='both', which='major', labelsize=12)
            ax.set_xlabel("temperature (K)", fontsize=12)

        ax0.legend()
        ax0.set_ylabel(r'$\text{heat capacity}\, (\text{JK}^{-1}\text{mol}^{-1})$', fontsize=12)
        ax1.set_ylabel(r'$\text{change in enthalpy}\, (\text{Jmol}^{-1})$', fontsize=12)
        ax2.set_ylabel(r'$\text{entropy}\, (\text{JK}^{-1}\text{mol}^{-1})$', fontsize=12)
    
        plt.savefig('Parameterized_NASA7_fit.png',bbox_inches='tight',dpi=300,transparent=False)
        return None

    def get_RMG_thermo_database_entry(self, index, long_description):
       
        al, ah = self.fit_NASA7_polynomial()
        str_l = 'coeffs={}'.format(str(al))
        str_h = 'coeffs={}'.format(str(ah))
        f0 = str(round(self.frequencies[0],2))
        f1 = str(round(self.frequencies[1],2))
        line = 'entry(\n'
        line += '    index = {},\n'.format(str(index))
        line += '    label = {},\n'.format(self.adsorbate_name)
        line += '    molecule = \n'
        line += '\"\"\"'
        line += self.connectivity + '\n'
        line += '\"\"\",\n'
        line += '    thermo = NASA(\n'
        line += '        polynomials = [\n'
        line += '            NASAPolynomial(' + str_l + ', Tmin=(298.0, \'K\'), Tmax=(1000.0, \'K\')),\n'
        line += '            NASAPolynomial(' + str_h + ', Tmin=(1000.0, \'K\'), Tmax=(2000.0, \'K\')),\n'
        line += '        ],\n'
        line += '        Tmin = (298.0,\'K\'),\n'
        line += '        Tmax = (2000.0,\'K\'),\n'
        line += '    ),\n' 
        line += 'longDesc = u\"\"\"'
        line += long_description + '\n'
        if self.twoD_gas:
            line += 'The two lowest frequencies, {} and {}, where replaced by the 2D gas model.\n'.format(f0,f1)
        line += '""",\n'
        line += '    metal = \"{}\",\n'.format(self.metal)
        line += '    facet = \"{}\",\n)\n'.format(self.facet) 

        return line

    """
    to do:
        - write the "write mes"
        - add some functions to get beef ensemble of NASA7 polynomials
        - think of file format to store and read in beef_energies, 
          maybe with np.savetxt, np.loadtxt, or maybe pandas
        - Create a class Adsorbates, which can handle lists of adsorbate_dicts,
          and make RMG thermo files entirely.
    """
