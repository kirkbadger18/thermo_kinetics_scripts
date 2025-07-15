The Adsorbate class contains methods to compute temperature dependant entropy, heat capacty, and standard state enthalpy of formation from statistical mechanics. methods in the class fit a NASA7 polynomial to these thermodynamic quantities, and plot a comparison between the NASA7 polynomial and the values from statisical mechanics. There is also a method which is used to write out an entry to be used in an RMG thermolibrary.

An example of how this class can be used has been set up [here](https://github.com/kirkbadger18/thermo_kinetics_scripts/blob/new_workflow/new_workflow/example.ipynb). For more information keep reeding below.

The class is initialized with:
```
adsorbate = Adsorbate(adsorbate_dict,
                      reference_dict,
                      slab_dict,
                      long_description,
)
```
The `adsorbate_dict` is a dictionary which contains information about the adsorbate and should be formatted like this:
```
adsorbate_dict = dict(
            adsorbate_name = 'OXCXCH2',
            adsorbate_composition = {'H':2, 'C':2, 'N':0, 'O':1},
            dft_energy = [-378744.484815, 'eV'],
            zpe = [0.930, 'eV'],
            frequencies = [58.5,150.3,163.9,284.7,443.7,445.6,618.1,682.8,894.5,1032.6,1050.4,1361.4,1738.5,3001.1,3074.3, 'cm-1'],
            sites_occupied = 2,
            beef_energies = None,
            connectivity = textwrap.dedent(
            '''
            1 X u0 p0 c0 {3,S}
            2 X u0 p0 c0 {4,S}
            3 C u0 p0 c0 {1,S} {4,S} {5,D}
            4 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
            5 O u0 p2 c0 {3,D}
            6 H u0 p0 c0 {4,S}
            7 H u0 p0 c0 {4,S}
            '''
           ),
        )
```
The `reference_dict` contains information about the reference gas phase species and should be formatted like this:

```
reference_dict = dict(
                reference_compositions={"CH4": {"C": 1,  "O": 0, "H":4, "N": 0},
                                        "H2O": {"C": 0, "O": 1, "H":2, "N": 0},
                                        "H2": {"C": 0, "O": 0, "H":2, "N": 0},
                                        "NH3": {"C": 0, "O": 0, "H":3, "N": 1},
                                        },
                reference_energies= {"CH4":-324.294,
                                     "H2O":-611.0186083,
                                     "H2": -32.6984442,
                                     "NH3":-442.6510481,
                                    },
                reference_EOF={"CH4":-66.557,
                               "H2O":-238.929,
                               "H2":0,
                               'NH3':-38.565,
                              },
                )

```
The `slab_dict` contains information about the metal slab that is being used and should look like:
```
slab_dict = dict(
        slab_energy = -377616.072,
        metal = 'Pt',
        facet = '111',
        unit_cell_area = 62.105e-20/9.0,
        )
```
Lastly the `long_description` is used when formatting the RMG output, and example of what this might look like is:
```
long_description = '''
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.'''
```

Some methods accessable to `Adsorbate` are:
```
[get_0K_heat_of_formation(), get_2D_translational_thermo(),
get_vibrational_thermo(), get_thermo(), fit_NASA7_polynomial(),
get_thermo_from_NASA(), plot_NASA_fit(), get_RMG_thermo_database_entry()]
```
