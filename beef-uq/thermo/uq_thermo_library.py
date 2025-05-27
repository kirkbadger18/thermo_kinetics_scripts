import numpy as np
import pandas as pd
import os

Name='surfaceThermoPt111'
N_members=2000

key1 = 'NASAPolynomial(coeffs=[' 
key2 = '        Tmin'
labels=[]
NASA_lines = []
original_filename="".join((Name,".py"))

f = open(original_filename,'r')
original_lines = f.readlines()
f.close()

j=0
for i, line in enumerate(original_lines):
    if line.startswith("    label"):
        old=line.strip()
        bits=line.split(" = ")
        label = bits[1].replace(",","").replace("\n","").replace('"',"")
        if label != 'vacant':
            labels.append(label)
    if key1 in line and '#' not in line and label != 'vacant':
        if j % 2 == 0:
            NASA_lines.append(i)
        j += 1

beef_data = np.zeros([N_members,len(labels)])
for i in range(len(labels)):
    filename='beef-ensembles/' + str(labels[i]) + '_bee.txt'
    data=pd.read_csv(filename, sep="\t", header=0)
    beef_data[:,i]=data.iloc[0:N_members,1]
del data

for i in range(N_members):
    new_lines = []
    skip = []
    l = 0
    for j, line in enumerate(original_lines):
        if j in NASA_lines:
            stop = False
            NASA_list = []
            step = j
            while not stop:	
                bits = original_lines[step]
                NASA_list.append(bits)
                skip.append(step)
                step += 1	
                if original_lines[step].startswith(key2):
                    stop = True

            joint = ''.join(NASA_list)
            split1 = joint.split('[')[1].split(']')[0].split()
            split2 = joint.split('[')[2].split(']')[0].split()
            lowT = []
            highT = []

            for k in range(7):
                if k == 5: 
                    beef = beef_data[i,l]/8.314e-3
                    num1 = beef + float(split1[k].split(',')[0])
                    num2 = beef + float(split2[k].split(',')[0])
                else:
                    num1 = float(split1[k].split(',')[0])
                    num2 = float(split2[k].split(',')[0])
                lowT.append(num1)
                highT.append(num2)
            new_lines.append('            NASAPolynomial(coeffs=[\n')
            new_lines.append('             {}, {}, {}, {},\n'.format(lowT[0], lowT[1], lowT[2], lowT[3]))
            new_lines.append('             {}, {}, {}], Tmin=(298.0,\'K\'), Tmax=(1000.0, \'K\')),\n'.format(lowT[4], lowT[5], lowT[6]))
            new_lines.append('            NASAPolynomial(coeffs=[\n')
            new_lines.append('             {}, {}, {}, {},\n'.format(highT[0], highT[1], highT[2], highT[3]))
            new_lines.append('             {}, {}, {}], Tmin=(1000.0,\'K\'), Tmax=(2000.0, \'K\')),\n'.format(highT[4], highT[5], highT[6]))
            new_lines.append('        ],\n')
            l += 1
        elif j in skip:
            pass
        else:
            new_lines.append(original_lines[j])
    newname = Name + '_{}.py'.format(str(i))
    f = open(newname,'w')
    f.writelines(new_lines)
    f.close()
