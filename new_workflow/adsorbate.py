import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MaxNLocator, LogLocator
import textwrap


class Adsorbate:

    def __init__(self,
                 adsorbate_dict: dict,
                 reference_dict: dict,
                 slab_dict: dict,
                 long_description: str,
                 P_ref: float = 1.0E5,  # Pa
                 NASA7_T_switch: float = 1000.0,  # K
                 twoD_gas_cutoff_frequency: float = 100.0,  # cm^{-1}
                 ):
        """
        This is a class designed for taking in dft data for adsorbates,
        the metal they are on and a chosen set of references and is meant
        to be used to compute thermochemistry for the adsorbates. This can
        be in the form of partition functions, thermodynamic quantities
        of interrest, or parameterized NASA7 polynomials. This class also
        has methods for generating RMG input files.

        These input dictionarys should be structured like:
        adsorbate_dict = dict(
                            adsorbate_name=str(name),
                            dft_energy=list[float(energy),str(unit)],
                            zpe=[float(energy),str(unit)],
                            frequencies=list[frequencies,str(unit)],
                            sites_occupied=float,
                            beef_energies=None,
                            atomic_composition={"C": int,  "O": int,
                                                "H": int, "N": int},
                            )
        reference_dict = dict(
                reference_compositions={"CH4": {"C": int,  "O": int,
                                        "H": int, "N": int, "slab": int},
                                        "H2O": {"C": int, "O": int,
                                        "H":2, "N": int, "slab": int},
                                        "H2": {"C": int, "O": int,
                                        "H":2, "N": int, "slab": int},
                                        },
                reference_energies= {"CH4":float,
                                     "H2O":float,
                                     "H2": float,
                                     "NH3: float,
                                     "slab": float
                                    },
                reference_EOF={"CH4": float,
                               "H2O": float,
                               "H2": float,
                               "NH3": float,
                               "slab": float
                              },
                )
        """
        self.adsorbate_name = adsorbate_dict['adsorbate_name']
        self.atomic_composition = adsorbate_dict['atomic_composition']
        self.dft_energy = adsorbate_dict['dft_energy']
        self.zpe = adsorbate_dict['zpe']
        self.frequencies = adsorbate_dict['frequencies']
        self.sites_occupied = adsorbate_dict['sites_occupied']
        self.connectivity = adsorbate_dict['connectivity']

        self.reference_compositions = reference_dict['reference_compositions']
        self.reference_energies = reference_dict['reference_energies']
        self.reference_EOF = reference_dict['reference_EOF']
        self.unit_cell_area = slab_dict['unit_cell_area']
        self.metal = slab_dict['metal']
        self.facet = slab_dict['facet']

        self.long_description = long_description
        self.P_ref = P_ref
        self.NASA7_T_switch = NASA7_T_switch
        self.twoD_gas_cutoff_frequency = twoD_gas_cutoff_frequency

        self._load_constants()
        self._get_adsorbate_molecular_mass()
        self._get_temperatures()
        self._check_if_2D_gas()

    def __repr__(self):
        """
        This allows us to print and asorbate object and get a
        human readable output
        """
        return self.name

    def _get_adsorbate_molecular_mass(self):
        """
        Internal method for computing the mass of the adsorbate
        excluding the surface
        """
        atomic_masses = {'H': 1.01, 'C': 12.01, 'N': 14, 'O': 16}
        atomic_composition = self.atomic_composition
        self.adsorbate_mass = atomic_composition['H'] * atomic_masses['H']
        self.adsorbate_mass += atomic_composition['O'] * atomic_masses['O']
        self.adsorbate_mass += atomic_composition['C'] * atomic_masses['C']
        self.adsorbate_mass += atomic_composition['N'] * atomic_masses['N']
        return

    def _get_temperatures(self):
        """
        Internal method for assigning the temperatures to evalate thermodynamic
        quantities at. This can be changed if needed, but note that it is
        designed so that the first temperature is 298, and that the rest of the
        temperatures are divisible by 10.
        """
        T0 = [298.15]
        T_low = 300.0
        T_high = 2000.0
        dT = 10.0  # temperature increment
        self.temperatures = np.append(T0, np.arange(T_low, T_high+dT, dT))
        return

    def _load_constants(self):
        """
        Here we assign all relevent constants as an attribute of our class
        """
        self.R = 8.3144621E-3  # ideal Gas constant in kJ/mol-K
        self.kB = 1.38065e-23  # Boltzmann constant in J/K
        self.h = 6.62607e-34  # Planck constant in J*s
        self.c = 2.99792458e8  # speed of light in m/s
        self.amu = 1.6605e-27  # atomic mass unit in kg
        self.Avogadro = 6.0221E23  # mole^-1
        self.GHz_to_Hz = 1.0E9  # convert rotational constants from GHz to Hz
        self.invcm_to_invm = 1.0E2  # convert cm^-1 to m^-1, for frequencies
        self.hartree_to_kcalpermole = 627.5095
        self.hartree_to_kJpermole = 2627.25677
        self.eV_to_kJpermole = 96.485  # convert eV/molecule to kJ/mol
        return

    def _check_if_2D_gas(self):
        """
        Internal method do determine if the two lowest frequency modes of the
        adsorbate should be treated as free translators. The desired cutoff is
        100 cm^-1 by default, but this can be set as desired.
        """
        freq = self.frequencies
        cutoff = self.twoD_gas_cutoff_frequency
        self.twoD_gas = False
        if np.max(freq[0:2]) <= cutoff:
            self.twoD_gas = True
        return

    def get_enthalpy_of_formation_at_0K(self):

        """
        General linear algebra framework to calculate the enthalpy
        (of formation) of a target (e.g., adsorbate) from a set of reference
        species (e.g., gas-phase species, adsorbates). The method is completely
        flexible and can be used with the conventional approach
        (using elements) or with more complex error cancellation methods
        (e.g., isodesmic reactions). Details for this method are provided in
        Kreitz et al., Chem. Soc. Rev., 2025, 54, 560-589,
        DOI: 10.1039/D4CS00768A
        """

        target_composition_dict = self.atomic_composition
        target_composition_keys = list(target_composition_dict.keys())
        ref_composition_dict = self.reference_compositions
        ref_composition_keys = list(ref_composition_dict.keys())

        number_target_features = len(target_composition_keys)
        number_ref_features = len(ref_composition_keys)
        assert number_target_features == number_ref_features

        target_feature_vector = np.zeros(number_target_features)
        for i, feature_key in enumerate(target_composition_keys):
            target_feature_vector[i] = target_composition_dict[feature_key]
        ref_feature_matrix_shape = [number_ref_features, number_ref_features]
        ref_feature_matrix = np.zeros(ref_feature_matrix_shape)
        for i, species_key in enumerate(ref_composition_keys):
            for j, feature_key in enumerate(target_composition_keys):
                ref_feature_matrix[j, i] = ref_composition_dict[
                    species_key][feature_key]

        matinv = inv(ref_feature_matrix)
        target_ref_vector = -np.matmul(matinv, target_feature_vector)

        ref_EOF_list = list(self.reference_EOF.values())
        ref_enthalpies_of_formation_at_0K = np.array(ref_EOF_list)
        ref_energy_vals = self.reference_energies.values()
        ref_dft_energies = np.array(list(ref_energy_vals))
        ref_dft_energies *= self.eV_to_kJpermole

        target_dft_energy = self.dft_energy[0] + self.zpe[0]
        target_dft_energy *= self.eV_to_kJpermole

        enthalpy_of_formation_0K = target_dft_energy
        enthalpy_of_formation_0K += target_ref_vector.dot(ref_dft_energies)
        ref_dH_0k = ref_enthalpies_of_formation_at_0K
        enthalpy_of_formation_0K -= target_ref_vector.dot(ref_dH_0k)

        return enthalpy_of_formation_0K

    def get_2D_translational_thermo(self):
        """
        This method computes the partition function, enthalpy increment
        entropy, and heat capacity for a 2D free translator. This will only
        return non-zero S, dH, and cP if the adsorbate attribute "twoD_gas"
        is true.
        """
        area = self.unit_cell_area
        sites = self.sites_occupied
        pi = np.pi
        temps = self.temperatures
        m = self.adsorbate_mass
        h = self.h
        amu = self.amu
        kB = self.kB
        R = self.R

        q_trans = np.ones(len(temps))
        S_trans = np.zeros(len(temps))
        dH_trans = np.zeros(len(temps))
        Cp_trans = np.zeros(len(temps))
        if self.twoD_gas:
            for i, T in enumerate(temps):
                q_trans[i] = (2*pi*m*amu*kB*T/h**2) * area * sites
                S_trans[i] = R * (2.0 + np.log(q_trans[i]))
                Cp_trans[i] = R
                dH_trans[i] = R * T

        return q_trans, S_trans, dH_trans, Cp_trans

    def get_vibrational_thermo(self):
        """
        This returns the vibrational partition function, enthalpy increment,
        entropy and heat capacity for the vibrational modes of the adsorbate.
        """
        units = self.h * self.c / self.kB * self.invcm_to_invm  # K * cm
        temps = self.temperatures
        q_vib = np.ones(len(temps))
        S_vib = np.zeros(len(temps))
        dH_vib = np.zeros(len(temps))
        Cv_vib = np.zeros(len(temps))

        for t, temp in enumerate(temps):
            for n, nu in enumerate(self.frequencies[0:-1]):
                if self.twoD_gas and n <= 1:
                    pass
                else:
                    x = nu * units / temp  # cm^-1 * K cm / K = dimensionless
                    q_vib[t] *= 1.0 / (1.0 - np.exp(-x))
                    qterm = 1.0 - np.exp(-x)
                    S_vib[t] += -np.log(qterm) + x * np.exp(-x) / qterm
                    dH_vib[t] += x * np.exp(-x) / qterm
                    Cv_vib[t] += x ** 2.0 * np.exp(-x) / qterm ** 2.0
            S_vib[t] *= self.R
            dH_vib[t] *= self.R * temp
            Cv_vib[t] *= self.R
        return q_vib, S_vib, dH_vib, Cv_vib

    def get_thermo(self):
        """
        The enthalpy of formation of is derived from the DFT data at 0K. We
        need to correct the enthalpy of formation to 298K, which includes a
        correction based on the partition functions, but also an additional
        correction that is based on correcting the reference species see:
        Ruscic and Bross,Computer Aided Chemical Engineering,45,3-114,2019,
        DOI:10.1016/B978-0-444-64087-1.00001-2, page 75). If you are reading
        this, you should probably read the whole paper!
        """

        # Values from Ruscic and Bross (see above), page 75
        h_correction = 4.234  # kJ/mol. enthalpy_H(298) - enthalpy_H(0)
        c_correction = 1.051  # kJ/mol. enthalpy_C(298) - enthalpy_C(0)
        n_correction = 4.335  # kJ/mol. enthalpy_N(298) - enthalpy_N(0)
        o_correction = 4.340  # kJ/mol. enthalpy_O(298) - enthalpy_O(0)
        EOF_ref_correction = 0.0
        comp = self.atomic_composition
        EOF_ref_correction += comp['H'] * h_correction
        EOF_ref_correction += comp['C'] * c_correction
        EOF_ref_correction += comp['N'] * n_correction
        EOF_ref_correction += comp['O'] * o_correction

        q_t, S_t, dH_t, Cp_t = self.get_2D_translational_thermo()
        q_v, S_v, dH_v, Cv_v = self.get_vibrational_thermo()

        Q = q_v * q_t
        S = S_t + S_v
        dH = dH_t + dH_v
        Cp = Cp_t + Cv_v
        enthalpy_of_formation_at_0K = self.get_enthalpy_of_formation_at_0K()
        self.enthalpy_of_formation_at_298K = enthalpy_of_formation_at_0K
        self.enthalpy_of_formation_at_298K += dH[0]
        self.enthalpy_of_formation_at_298K -= EOF_ref_correction
        H = self.enthalpy_of_formation_at_298K + dH - dH[0]
        return Q, S, H, Cp

    def fit_NASA7_polynomial(self):
        """
        This method calls the get thermo method and fits a NASA7 polynomial
        for two regimes: the low temperature regime T = [298K-1000K], and the
        high temperature regime T = [1000K-2000K]. The form of this polynomial
        is described here:
        https://cantera.org/stable/reference/thermo/species-thermo.html
        """

        """
        Note to self:
        This section is a bit messy and long, we should delegate parts of this
        method to other methods. Additionally, we should rename these variables
        to be more descriptive.
        """
        R = self.R
        Q, S, H, Cp = self.get_thermo()
        H0 = H[0]
        S0 = S[0]
        T_switch = self.NASA7_T_switch
        temps = self.temperatures

        i_switch = -1
        for i in range(len(temps)):
            if temps[i] == T_switch:
                i_switch = i
        if i_switch == -1:
            print("We have a problem! Cannot find switching temperature")

        # start by creating the independent variable matrix for the low-T fit
        YT = np.array([
            np.ones(len(temps[:i_switch+1])),
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
        # now determine the enthalpy coefficient for the low-T region
        subtract = a_low[0] + a_low[1] / 2.0 * T_ref + a_low[2] / 3.0 * \
            T_ref ** 2.0 + a_low[3] / 4.0*T_ref ** 3.0 \
            + a_low[4] / 5.0 * T_ref ** 4.0

        a_low = np.append(a_low, H0 / R - subtract * T_ref)
        # now determine the entropy coefficient for the low-T region
        subtract = a_low[0] * np.log(T_ref) + a_low[1]*T_ref + a_low[2] / \
            2.0 * T_ref ** 2.0 + a_low[3] / 3.0 * T_ref ** 3.0 \
            + a_low[4] / 4.0 * T_ref ** 4.0

        a_low = np.append(a_low, S0 / R - subtract)
        #
        # NOW SWITCH TO HIGH-TEMPERATURE REGIME!
        #
        T_ref = T_switch
        # compute the heat capacity, enthalpy, and entropy at the switch temp
        Cp_switch = a_low[0] + a_low[1] * T_ref + a_low[2] * T_ref ** 2.0 \
            + a_low[3] * T_ref ** 3.0 + a_low[4] * T_ref ** 4.0

        H_switch = a_low[0] * T_ref + a_low[1] / 2.0 * T_ref ** 2.0 + \
            a_low[2] / 3.0 * T_ref ** 3.0 + a_low[3] / 4.0 * T_ref ** 4.0 \
            + a_low[4] / 5.0 * T_ref ** 5.0 + a_low[5]

        S_switch = a_low[0] * np.log(T_ref) + a_low[1] * T_ref + a_low[2] / \
            2.0 * T_ref ** 2.0 + a_low[3] / 3.0 * T_ref ** 3.0 + \
            a_low[4] / 4.0 * T_ref ** 4.0 + a_low[6]

        # repeat the process for the high-temperature regime
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
        a_high[0] = Cp_switch - (a_high[0] + a_high[1] * T_switch + a_high[2]
                                 * T_switch ** 2.0 + a_high[3] * T_switch **
                                 3.0 + a_high[4] * T_switch ** 4.0)

        a_high = np.append(a_high, H_switch -
                           (a_high[0] + a_high[1] / 2.0 * T_ref + a_high[2] /
                            3.0 * T_ref ** 2.0 + a_high[3]/4.0*T_ref ** 3.0 +
                            a_high[4] / 5.0 * T_ref ** 4.0) * T_ref)

        a_high = np.append(a_high, S_switch -
                           (a_high[0] * np.log(T_ref) + a_high[1] * T_ref +
                            a_high[2] / 2.0 * T_ref ** 2.0 + a_high[3] / 3.0
                            * T_ref ** 3.0 + a_high[4] / 4.0 * T_ref ** 4.0))
        return a_low, a_high

    def get_thermo_from_NASA(self):
        a_low, a_high = self.fit_NASA7_polynomial()
        R = self.R
        T_switch = self.NASA7_T_switch
        temps = self.temperatures

        cp_fit = np.zeros(len(temps))
        h_fit = np.zeros(len(temps))
        s_fit = np.zeros(len(temps))

        for i, temp in enumerate(temps):
            if temp <= T_switch:
                cp_fit[i] = a_low[0] + a_low[1] * temp + a_low[2] * temp ** \
                    2.0 + a_low[3] * temp ** 3.0 + a_low[4] * temp ** 4.0

                h_fit[i] = a_low[0] * temp + a_low[1] / 2.0 * temp ** 2.0 + \
                    a_low[2] / 3.0 * temp ** 3.0 + a_low[3] / 4.0 * temp ** \
                    4.0 + a_low[4] / 5.0 * temp ** 5.0 + a_low[5]

                s_fit[i] = a_low[0] * np.log(temp) + a_low[1] * temp + \
                    a_low[2] / 2.0 * temp ** 2.0 + a_low[3] / 3.0 * temp ** \
                    3.0 + a_low[4] / 4.0 * temp ** 4.0 + a_low[6]
            else:
                cp_fit[i] = a_high[0] + a_high[1] * temp + a_high[2] * temp \
                    ** 2.0 + a_high[3] * temp ** 3.0 + a_high[4] * temp ** 4.0

                h_fit[i] = a_high[0] * temp + a_high[1] / 2.0 * temp ** 2.0 + \
                    a_high[2] / 3.0 * temp ** 3.0 + a_high[3] / 4.0 * temp \
                    ** 4.0 + a_high[4] / 5.0 * temp ** 5.0 + a_high[5]

                s_fit[i] = a_high[0] * np.log(temp) + a_high[1] * temp + \
                    a_high[2] / 2.0 * temp ** 2.0 + a_high[3] / 3.0 * temp \
                    ** 3.0 + a_high[4] / 4.0 * temp ** 4.0 + a_high[6]

        cp_fit *= R
        h_fit *= R
        s_fit *= R

        return s_fit, h_fit, cp_fit

    def plot_NASA7_fit(self):
        """
        This method creates a plot of the computed thermodynamic quantities vs
        the estimate from the NASA7 polynomial.
        """
        S_fit, H_fit, Cp_fit = self.get_thermo_from_NASA()
        Q, S, H, Cp = self.get_thermo()
        HOF_298 = self.enthalpy_of_formation_at_298K
        plt.figure(dpi=300, figsize=(12, 4))
        gs = gridspec.GridSpec(1, 3)
        gs.update(wspace=0.5, hspace=0.4)
        ax0 = plt.subplot(gs[0])
        ax1 = plt.subplot(gs[1])
        ax2 = plt.subplot(gs[2])
        temps = self.temperatures
        ax0.plot(temps, Cp, marker='o', markeredgecolor='r', color='w',
                 alpha=0.5, linestyle='None', label='stat. mech.')
        ax0.plot(temps, Cp_fit, 'b', linewidth=2, label='NASA')
        ax1.semilogy(temps, H - HOF_298, marker='o', markeredgecolor='r',
                     color='w', alpha=0.5, linestyle='None')
        ax1.semilogy(temps, H_fit - HOF_298, 'b', linewidth=2)
        ax2.semilogy(temps, S, marker='o', markeredgecolor='r',
                     color='w', alpha=0.5, linestyle='None')
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
        ax0.set_ylabel(r'$\text{heat capacity}\,' +
                       '(\text{JK}^{-1}\text{mol}^{-1})$',
                       fontsize=12)
        ax1.set_ylabel(r'$\text{change in enthalpy}\, (\text{Jmol}^{-1})$',
                       fontsize=12)
        ax2.set_ylabel(r'$\text{entropy}\, (\text{JK}^{-1}\text{mol}^{-1})$',
                       fontsize=12)

        plt.savefig('Parameterized_NASA7_fit.png', bbox_inches='tight',
                    dpi=300, transparent=False)
        return None

    def get_RMG_thermo_database_entry(self, index: int):
        """
        This method creates string which when printed or written could
        be added to RMG. This method is public, but will likely most often be
        called indirectly to write entire RMG thermolibrary files
        """
        al, ah = self.fit_NASA7_polynomial()
        str_l = 'coeffs=[{}]'.format(", ".join(map(str, al)))
        str_h = 'coeffs=[{}]'.format(", ".join(map(str, ah)))
        f0 = str(round(self.frequencies[0], 2))
        f1 = str(round(self.frequencies[1], 2))
        line = 'entry(\n'
        line += '    index = {},\n'.format(str(index))
        line += '    label = \"{}\",\n'.format(self.adsorbate_name)
        line += '    molecule = \n'
        line += '\"\"\"\n'
        line += self.connectivity
        line += '\"\"\",\n'
        line += '    thermo = NASA(\n'
        line += '        polynomials = [\n'
        line += '            NASAPolynomial(' + str_l + ', Tmin=(298.0,' + \
            '\'K\'),Tmax=(1000.0, \'K\')),\n'
        line += '            NASAPolynomial(' + str_h + ', Tmin=(1000.0,' + \
            '\'K\'), Tmax=(2000.0, \'K\')),\n'
        line += '        ],\n'
        line += '        Tmin = (298.0,\'K\'),\n'
        line += '        Tmax = (2000.0,\'K\'),\n'
        line += '    ),\n'
        line += 'longDesc = u\"\"\"'
        line += self.long_description + '\n'
        if self.twoD_gas:
            line += 'The two lowest frequencies, {} and {},'.format(f0, f1) + \
                'where replaced by the 2D gas model.\n'
        line += '""",\n'
        line += '    metal = \"{}\",\n'.format(self.metal)
        line += '    facet = \"{}\",\n)\n'.format(self.facet)

        return line


class Adsorbates:
    """
    This class is designed to be a wrapper around Adsorbate. In most cases we
    want the thermochemistry for a list of adsorbates instead of just one.
    This is what this class is for. You feed all the same information you would
    to Adsorbate, except instead of one adsorbate dict, you feed in a list of
    adsorbate dicts.
    """
    def __init__(self,
                 adsorbate_list: list[dict],
                 reference_dict: dict,
                 slab_dict: dict,
                 long_description: str,
                 P_ref: float = 1.0E5,  # Pa
                 NASA7_T_switch: float = 1000.0,  # K
                 twoD_gas_cutoff_frequency: float = 100.0,  # cm^{-1}
                 ):

        self.slab_dict = slab_dict
        self.adsorbate_list = []
        for ads_dict in adsorbate_list:
            ads = Adsorbate(ads_dict, reference_dict, slab_dict,
                            long_description, P_ref, NASA7_T_switch,
                            twoD_gas_cutoff_frequency)
            self.adsorbate_list.append(ads)

        return

    def _get_vacantX_str(self):
        """
        This internal method produces a string which is the first entry in
        an RMG surface thermo library file
        """
        first_part = textwrap.dedent(
            """
            entry(
                index = 1,
                label = "vacant",
                molecule =
                \"\"\"
                1 X  u0 p0 c0
                \"\"\",
                thermo = NASA(
                    polynomials = [
                        NASAPolynomial(coeffs=[
                        0, 0, 0, 0,
                        0, 0, 0], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
                        NASAPolynomial(coeffs=[
                        0, 0, 0,   0,
                        0, 0, 0], Tmin=(1000.0,'K'), Tmax=(3000.0, 'K')),
                    ],
                    Tmin = (298.0, 'K'),
                    Tmax = (3000.0, 'K'),
                ),
            """
        )
        metal_type = self.slab_dict['metal']
        facet = self.slab_dict['facet']
        metal_str = "    metal = \"" + metal_type + '\",\n'
        facet_str = "    facet = \"" + facet + '\",\n)\n'
        return first_part + metal_str + facet_str

    def plot_NASA7_fits(self):
        """
        This wraps around Adsorbate.get_NASA7_fit()
        """
        for ads in self.adsorbate_list:
            ads.plot_NASA7_fit()
        return

    def get_RMG_thermo_database_entries(self, start_idx=1):
        """
        This wraps around: Adsorbate.get_RMG_thermo_database_entry()
        """
        string_tot = ''
        for i, ads in enumerate(self.adsorbate_list):
            i += start_idx
            rmg_str = ads.get_RMG_thermo_database_entry(i) + '\n'
            string_tot += rmg_str
        return string_tot

    def write_RMG_thermodatabase_file(self,
                                      filename: str,
                                      libname: str = ' ',
                                      short_description: str = ' ',
                                      long_description: str = '    \n',
                                      ):

        """
        This is the main method of this class and is used to write an RMG
        thermo database file. The filename is the name of the file you wnat to
        make. The libname is string that shows up at the top of the file as:
        name = "name"
        The short and long description also show up at the top of the file.
        """
        main_str = self.get_RMG_thermo_database_entries(start_idx=2)
        header_str = textwrap.dedent(
            """
            #!/usr/bin/env python
            # encoding: utf-8
            """
        )
        name_str = 'name = \"' + libname + '\"\n'
        short_desc_str = 'shortDesc = u\"' + short_description + '\"\n'
        long_desc_str = 'longDesc = u\"\"\"\n' + long_description + '\"\"\"\n'
        vacantx_str = self._get_vacantX_str()
        file_str = header_str + name_str + short_desc_str + \
            long_desc_str + vacantx_str + main_str
        with open(filename, 'w') as f:
            f.writelines(file_str)


class AdsorbatesEnsemble(Adsorbates):
    """
    This is a class that wraps around Adsorbates and allows for an
    ensemble of RMG thermodatabase files to be written. The extra inputs
    are an ensemble of energy perturbations to the reference species
    and all of the adsorbates in the adsrobates_list.
    """
    def __init__(self,
                 adsorbate_list: list[dict],
                 reference_dict: dict,
                 slab_dict: dict,
                 long_description: dict,
                 ensemble_energies_array: dict,
                 reference_ensemble: dict,
                 ensemble_scale: float = 0.683,
                 P_ref: float = 100000,
                 NASA7_T_switch: float = 1000,
                 twoD_gas_cutoff_frequency: float = 100):

        super().__init__(adsorbate_list,
                         reference_dict,
                         slab_dict,
                         long_description,
                         P_ref,
                         NASA7_T_switch,
                         twoD_gas_cutoff_frequency)

        self.ensemble_energies_array = ensemble_energies_array
        self.ref_ensemble = reference_ensemble
        self.ensemble_scale = ensemble_scale
        self.original_ads_list = self.adsorbate_list.copy()
        self.reference_dict = reference_dict
        self.original_ref_dict = self.reference_dict.copy()
        self.rydberg_to_eV = 13.6056980659

    def write_ensemble_of_RMG_thermodatabase_files(
            self,
            directory="./",
            file_prefix="database",
            max_members=None,
            ):
        names = [ads.adsorbate_name for ads in self.adsorbate_list]
        ref_names = list(self.ref_ensemble.keys())
        if max_members:
            N_members = max_members
        else:
            N_members = len(self.ensemble_energies_array[names[0]])
        for i in range(N_members):
            for j, name in enumerate(names):
                dE = self.ensemble_energies_array[name][i]
                dE *= self.rydberg_to_eV * self.ensemble_scale
                oldE = self.original_ads_list[j].dft_energy[0]
                newE = oldE - dE
                self.adsorbate_list[j].dft_energy[0] = newE
            for j, name in enumerate(ref_names):
                dE = self.ref_ensemble[name][i]
                dE *= self.rydberg_to_eV * self.ensemble_scale
                oldE = self.original_ref_dict['reference_energies'][name]
                newE = oldE - dE
                self.reference_dict['reference_energies'][name] = newE
            """ loop to do same for refs"""
            name = directory + file_prefix + "_{}.py".format(str(i))
            self.write_RMG_thermodatabase_file(name)
        return None
