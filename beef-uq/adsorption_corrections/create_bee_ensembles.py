import numpy as np
import os
import pandas as pd


class Molecule:

    def __init__(self):
        # start by defining some physical constants
        self.n_bee = 2000


def parse_input(species, molecule):
    script_dir = '../thermo/beef-ensembles/'
    inputfile = str(script_dir) + str(species) + '_ads_bee.txt'
    data = pd.read_csv(inputfile, sep="\t", header=0)
    molecule.perturbation = data.iloc[:, 3].to_numpy()

    return molecule.perturbation

name = 'C*R*C*'
list_of_species = 'nodes/species_list_' + name + '.dat'
info = open(list_of_species, 'r')
species_list = info.readlines()
info.close()

array_list = []
counter = -1
for species in species_list:
    counter += 1
    filename = species.strip()
    print(filename)

    test = Molecule()
    array_list.append(parse_input(filename, test))

stacked = np.stack(array_list, axis=0)
avg = np.mean(stacked, axis=0)

output_file = 'beef-ensembles/' + name + '_bee.txt'
column_names = ['averaged_values']
df = pd.DataFrame(avg, columns=[column_names])
df.to_csv(output_file, sep="\t", index=False)