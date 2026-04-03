from adsorbate import Adsorbate, Adsorbates
import matplotlib.pyplot as plt


class SurfaceReaction:
    """
    This class is designed to take in 2 Adsorbate objects
    which are taken to be the initial state and the first-order saddle-point.
    Methods intended to be used are get_arrhenius_parameters, plot_arrhenius,
    write_RMG_library_entry, write_RMG_dictionary_entry.

    We may want to think further about how we instantiate these objects in the
    future, using an "Adsorbate" for the initial state probably doesn't make
    sense. We should later on make a StationaryPoint class which handles thermo
    generally and think about how to package input more cleanly.
    """
    def __init__(self,
                 initial_states: list[Adsorbate],
                 first_order_saddle_point: Adsorbate,
                 vacant_sites_required: int,
                 ):

        self.initial_states = initial_states
        self.first_order_saddle_point = first_order_saddle_point
        self.vacant_sites_required = vacant_sites_required
        self.reacant_number = len(initial_states) + self.vacant_sites_required
        self._get_delta_energy()

    def _get_delta_energy(self):
        E_init = 0
        for IS in self.initial_states:
            E_init += IS.dft_energy[0] + IS.zpe[0]
        nslabs = len(self.initial_states) - 1
        slabE = self.first_order_saddle_point.reference_energies['slab']
        E_fosp = self.first_order_saddle_point.dft_energy[0] \
            + self.first_order_saddle_point.zpe[0]
        dE = E_fosp + slabE * nslabs - E_init
        self.delta_energy = dE
        return

    def get_arrhenius_parameters(self):
        temps = self.first_order_saddle_point.temperatures.copy()
        q_is = 1
        for IS in self.initial_states:
            qtmp, _, _, _ = IS.get_thermo()
            q_is *= qtmp
        q_ts, _, _, _ = self.first_order_saddle_point.get_thermo()
        dE = self.delta_energy
        A, b, Ea = self._parameterize_arrhenius(temps, q_is, q_ts, dE)
        site_area = self.first_order_saddle_point.unit_cell_area
        N_A = 6.022e23
        site_dens = 1 / site_area / N_A
        gamma = 1 / site_dens ** site_dens
        A *= gamma
        return A, b, Ea

    def _parameterize_arrhenius(self,
                                temps: list[float],  # K
                                q_is: list[float],
                                q_ts: list[float],
                                dE: float,  # eV
                                ) -> tuple[float, float, float]:  # [m^2/mol/sec], [], [kJ/mol]
        A, b, Ea = 0, 0, 0
        """
        ToDo for Jully
        temps = self.initial_state.temperatures
        q_is, _, _, _ = self.initial_state.get_thermo()
        q_ts, _, _, _ = self.first_order_saddle_point.get_thermo()
        q_ratio = q_ts / q_is
        kfwd=f(q(T)
        please take this q ratio, and the temperatures and
        fit the arrhenious constants accourding to:
            https://cantera.org/3.1/python/kinetics.html#arrheniusrate
        """
        return A, b, Ea

    def plot_arrhenius(self, filename=None):
        """
        ToDo for Jully
        please save a png of an arrhenious plot to filename
        please use a log y axis instead of log(k), and please
        use 1000/T for the x axis.
        """
        plt.subplot()
        return

    def write_RMG_library_entry(self):
        """
        leave for kirk to write later
        """
        pass

    def write_RMG_dictionary_entry(self):
        """
        leave for kirk to write later
        """
        pass


class SurfaceReactions:
    """
    This class is a wrapper around the Reaction class, designed to handle
    multiple reactions simultaneously.
    """
    def __init__(self,
                 initial_states: Adsorbates,
                 first_order_saddle_points: Adsorbates
                 ):
        self.initial_states = initial_states
        self.first_order_saddle_points = first_order_saddle_points
        self.reaction_list = []

        for i in range(len(initial_states)):
            reaction = SurfaceReaction(initial_states[i],
                                       first_order_saddle_points[i])
            self.reaction_list.append(reaction)

    def get_arrhenius_parameters(self):
        parameters = []
        for rxn in self.reaction_list:
            parameters.append(rxn.get_arrhenius_parameters())
        return parameters

    def plot_arrhenius_fits(self):
        for i, rxn in enumerate(self.reaction_list):
            filename = f"arrhenius_fit_{i}.png"
            rxn.plot_arrhenius(filename=filename)
        return

    def write_RMG_library_entries(self):
        """
        Leave for kirk to write later
        """
        pass

    def write_RMG_dictionary_entries(self):
        """
        Leave for kirk to write later
        """
        pass
