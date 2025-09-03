import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from torch.quasirandom import SobolEngine

N_members=25
name='reactions'

N_reactions = 54
stick_coeff_indices = [1, 4, 33, 34, 35, 36, 37]
stick_arr_indices = [3, 18, 19, 38]
no_data_indices = [31, 32, 42, 50, 54]
indices = []

for i in range(1,N_reactions+1):
    if i not in stick_coeff_indices and i not in no_data_indices and i not in stick_arr_indices:
        indices.append(i)

beef_keys = ['O-CO','h2cch-h-diss','hc-ch2-diss','CH2-CH2','hcch2-h-diss',
             'hcch-h-diss','hc-ch-diss','h2cch2-h-diss','CHC-H','hc-c-diss',
             'CO-OH','HO-H','O-H','COOH-O','CH2-H','CH-H','HC-O','H-CO','CO-H',
             'C-OH','CH2-CH3',
             'XC-XC',
             'CCH-H-FS','CH2C-H-IS', 'XCCH2-H',
             #'CH2CH2X_to_bi',
             'XN-O','O-XNO','XN-OH',
             'H-XNH','XN-H', 
             'H-XNNH2','XNH-CH3',
             'XN-CH3','XN-CN','XC-N',
             'XNO-H', 'H-XNO', 'HXN-O',
             ]
### Read reaction file and store as list

def generate_sobol_set(N_member, N):
    sobol=SobolEngine(dimension=N,scramble=True,seed = 1409580)
    x_sobol=sobol.draw(N_members)
    return x_sobol.numpy()
x_sobol = generate_sobol_set(N_members,4)
x_sobol *= 30
x_sobol -=15

print(x_sobol)

with open('reactions.py','r') as f:
    original_lines = f.readlines()
### Read beef data from files and store in array
beef_data = np.zeros([N_members,len(beef_keys)])
for i, name in enumerate(beef_keys):
    beef_file = 'beef-ensembles/{}-bee.txt'.format(name)
    data=pd.read_csv(beef_file, sep="\t", header=0)
    beef_data[:,i] = data.iloc[0:N_members,1]

for k in range(N_members):
    new_lines = []   
    N_arr = 0
    N_stick_arr = 0
    Ea_line_nums = []
    for line_num, line in enumerate(original_lines):
        if N_arr < len(indices) and "    index = {},".format(indices[N_arr]) in line: 
            new_lines.append(line)
            found_Ea = False
            tmp_line_num = line_num
            while not found_Ea:
                tmp_line_num += 1
                tmp_line = original_lines[tmp_line_num]
                if tmp_line.startswith("        Ea"):
                    old_Ea = float(tmp_line.split('(')[1].split(',')[0])
                    Ea = old_Ea + beef_data[k,N_arr]                    
                    if Ea < 0:
                        Ea = 0
                        print('arr')
                    found_Ea = True
                    Ea_line = '        Ea = ({}, \'kJ/mol\'),\n'.format(str(Ea))
                    N_arr += 1
                    Ea_line_nums.append(tmp_line_num)
        elif N_stick_arr < len(stick_arr_indices) and "    index = {},".format(stick_arr_indices[N_stick_arr]) in line:
            new_lines.append(line)
            found_Ea = False
            tmp_line_num = line_num
            while not found_Ea:
                tmp_line_num += 1
                tmp_line = original_lines[tmp_line_num]
                if tmp_line.startswith("        Ea"):
                    old_Ea = float(tmp_line.split('(')[1].split(',')[0])
                    Ea = old_Ea + x_sobol[k,N_stick_arr]
                    if Ea < 0:
                        print('stick_arr')
                        Ea = 0
                    found_Ea = True
                    Ea_line = '        Ea = ({}, \'kJ/mol\'),\n'.format(str(Ea))
                    N_stick_arr += 1
                    Ea_line_nums.append(tmp_line_num)
        elif line_num in Ea_line_nums:
            new_lines.append(Ea_line)
        else:
            new_lines.append(line)
    with open('reactions_{}.py'.format(str(k)),'w') as f:
        f.writelines(new_lines)
