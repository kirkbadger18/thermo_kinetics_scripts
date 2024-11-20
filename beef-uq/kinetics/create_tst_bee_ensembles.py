import numpy as np
import pandas as pd
import sys, os
import glob

# declare a class for molecules
class Molecule:

    def __init__(self):
        # start by defining some physical constants
        self.eV_to_kJpermole = 96.485  # convert eV/molecule to kJ/mol
        self.rydberg_to_eV = 13.6056980659  # convert Ry/molecule to eV/molecule
        self.scale_BEEF = 0.683  # 0.683 scaling factor for the BEEF ensemble #0.4 for C2H6 and CH4 dissociation
        self.is_twoD_gas = False
        self.tst_twoD_gas = False
        self.N_BEE = 2000

def parse_input_file(inputfile, molecule):
    script_dir = 'dft-data/'
    abs_file_path = script_dir + str(inputfile)

    molecule.output_file = "".join((inputfile.strip('.dat'), '-bee.txt'))

    input_file = open(abs_file_path, 'r')
    lines = input_file.readlines()
    input_file.close()

    error_name = True
    error_is_bee = True
    error_tst_bee = True

    for line in lines:
        # start by looking for the name
        if line.strip().startswith("name"):
            bits = line.split('=')
            name = bits[1].strip().replace("'", "").replace('"', '')
            molecule.name = name
            error_name = False

        # now look for the DFT energy
        elif line.strip().startswith("IS_SPE"):
            bits = line.split('=')
            is_SPE_info = bits[1].strip().replace("[", "").replace("]", "").split(',')
            is_SPE = float(is_SPE_info[0])
            units = is_SPE_info[1].strip().replace("'", "").replace('"', '')
            if units == 'eV':
                molecule.is_SPE = is_SPE
                molecule.is_SPE_units = units.strip()
                error_is_SPE = False
            else:
                print("DFT energy is missing proper units!\n Please use 'eV'")
                break

        # now look for the ZPE energy
        elif line.strip().startswith("IS_ZPE"):
            bits = line.split('=')
            is_ZPE_info = bits[1].strip().replace("[", "").replace("]", "").split(',')
            is_ZPE = float(is_ZPE_info[0])
            units = is_ZPE_info[1].strip().replace("'", "").replace('"', '')
            if units == 'eV':
                molecule.is_ZPE = is_ZPE
                molecule.is_ZPE_units = units.strip()
                error_is_ZPE = False
            else:
                print("ZPE energy is missing proper units!\n Please use 'eV'")
                break

        # now look for the DFT energy
        elif line.strip().startswith("TST_SPE"):
            bits = line.split('=')
            tst_SPE_info = bits[1].strip().replace("[", "").replace("]", "").split(',')
            tst_SPE = float(tst_SPE_info[0])
            units = tst_SPE_info[1].strip().replace("'", "").replace('"', '')
            if units == 'eV':
                molecule.tst_SPE = tst_SPE
                molecule.tst_SPE_units = units.strip()
                error_tst_SPE = False
            else:
                print("gas DFT energy is missing proper units!\n Please use 'eV'")
                break

        # now look for the ZPE energy
        elif line.strip().startswith("TST_ZPE"):
            bits = line.split('=')
            tst_ZPE_info = bits[1].strip().replace("[", "").replace("]", "").split(',')
            tst_ZPE = float(tst_ZPE_info[0])
            units = tst_ZPE_info[1].strip().replace("'", "").replace('"', '')
            if units == 'eV':
                molecule.tst_ZPE = tst_ZPE
                molecule.tst_ZPE_units = units.strip()
                error_tst_ZPE = False
            else:
                print("gas ZPE energy is missing proper units!\n Please use 'eV'")
                break

        # now look for the BEE
        elif line.strip().startswith("bee_IS"):
            bits = line.split('=')
            is_bee_data_info = bits[1].strip().replace("[", "").replace("]", "").split(',')
            is_bee_data = is_bee_data_info
            molecule.is_bee_energies = []
            for i in range(len(is_bee_data)):
                molecule.is_bee_energies.append(float(is_bee_data[i]))
            if len(is_bee_data) == molecule.N_BEE:
                error_is_bee = False
            else:
                print("The number of sample of the IS BEE is not 2000!\n Please check again!")
                break

        # now look for the gas BEE
        elif line.strip().startswith("bee_TS"):
            bits = line.split('=')
            tst_bee_data_info = bits[1].strip().replace("[", "").replace("]", "").split(',')
            tst_bee_data = tst_bee_data_info
            molecule.tst_bee_energies = []
            for i in range(len(tst_bee_data)):
                molecule.tst_bee_energies.append(float(tst_bee_data[i]))

            if len(tst_bee_data) == molecule.N_BEE:
                error_tst_bee = False
            else:
                print("The number of sample of the TS BEE is not 2000!\n Please check again!")
                break

    if error_name or error_tst_bee or error_is_bee:
        print("Input file is missing information: %s" % (inputfile))
    else:
        print("successfully parsed file %s" % (inputfile))

    return

def compute_ensemble(molecule):
    N_BEE = molecule.N_BEE
    eV_to_kJpermole = molecule.eV_to_kJpermole
    scale_BEEF = molecule.scale_BEEF
    rydberg_to_eV = molecule.rydberg_to_eV

    molecule.is_energy = molecule.is_SPE + molecule.is_ZPE
    molecule.tst_energy = molecule.tst_SPE + molecule.tst_ZPE
    molecule.ea = molecule.tst_energy * eV_to_kJpermole - molecule.is_energy * eV_to_kJpermole

    molecule.is_uq = np.zeros(molecule.N_BEE)
    molecule.tst_uq = np.zeros(molecule.N_BEE)
    molecule.ea_uq = np.zeros(molecule.N_BEE)
    molecule.delta_ea = np.zeros(molecule.N_BEE)

    for i in range(N_BEE):
        molecule.is_uq[i] = molecule.is_energy - molecule.is_bee_energies[i] * scale_BEEF * rydberg_to_eV
        molecule.is_uq[i] *= eV_to_kJpermole
        molecule.tst_uq[i] = molecule.tst_energy - molecule.tst_bee_energies[i] * scale_BEEF * rydberg_to_eV
        molecule.tst_uq[i] *= eV_to_kJpermole

        molecule.ea_uq[i] = molecule.tst_uq[i] - molecule.is_uq[i]

        if molecule.ea_uq[i] < 0:
            molecule.ea_uq[i] = 0
        else:
            molecule.ea_uq[i] = molecule.ea_uq[i]

        molecule.delta_ea[i] = molecule.ea_uq[i] - molecule.ea

    results_dir = 'beef-ensembles/'
    results_file = results_dir + molecule.output_file
    data = np.c_[molecule.ea_uq, molecule.delta_ea]
    names = ['Ea=' + str(molecule.ea), 'delta_Ea']
    df = pd.DataFrame(data, columns=[names])
    df.to_csv(results_file, sep="\t", index=False)

    return

for filename in glob.iglob('dft-data/*.dat'):
    print(filename)
    test = Molecule()
    parse_input_file(filename.split('/')[1],test)
    compute_ensemble(test)