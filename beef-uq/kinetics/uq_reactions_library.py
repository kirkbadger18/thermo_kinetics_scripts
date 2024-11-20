import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

num_pts=2

name='reactions'

for k in range(num_pts):
    file="".join((name,'_',str(k),".py"))
    s=open('reactions.py','r')
    
####### OCX + OX <=> CO2X + Pt ######  
    new_file_content=""    
    for line in s:
      if "    index = 2," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/O-CO-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 3," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

####### h-C2H4X + Pt <=> h-C2H3X + HX ######  
# BEEF data
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 5," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/h2cch-h-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 6," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

####### h-C2H3X <=> CHX + CH2X ######  
# BEEF data
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 6," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/hc-ch2-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 7," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### h-C2H4X <=> CH2X + CH2X ######  
# BEEF data
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 7," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/CH2-CH2-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 8," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()    
    
####### CHCH3X + Pt + Pt  <=>  h-C2H3X + HX ######  
# BEEF data
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 8," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/hcch2-h-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 9," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

####### h-C2H3X + Pt <=> h-C2H2X + HX ######  
# BEEF data 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 9," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/hcch-h-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 10," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### h-C2H2X <=> CHX + CHX ######  
# BEEF data 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 10," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/hc-ch-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 11," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### h-C2H3X + Pt <=>  CCH2X + HX######
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 11," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/CH2C-H-IS-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 12," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### C2H5X + Pt + Pt <=> h-C2H4X + HX ######  
# BEEF data 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 12," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/h2cch2-h-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 13," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

    
####### h-C2H2X + Pt <=> h-C2HX + HX ######  
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 13," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/CHC-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 14," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

####### h-C2HX + HX  <=>  h-CCH2X + Pt ######  
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 14," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/CCH-H-FS-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 15," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### h-C2HX <=> CHX + CX ######  
# BEEF data 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 15," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/hc-c-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 16," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

    
####### OCX + HOX <=> CXOOH + Pt ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 16," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/CO-OH-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 17," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### H2OX + Pt <=> HOX + HX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 17," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/HO-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 18," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### OX + HX <=> HOX + Pt ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 18," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/O-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 19," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
    
####### CXOOH + OX <=> CO2X + HOX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 19," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/COOH-O-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 20," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CH4 + Pt + Pt <=> CH3X + CHX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 20," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/CH3-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 21," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
    
####### C2H6 + Pt + Pt <=> CH2CH3X + CHX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 21," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/CH2CH3-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 22," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CH3X + Pt <=> CH2X + HX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 22," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/CH2-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 23," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

####### CH2X + Pt <=> CHX + HX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 23," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/CH-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 24," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

####### CHX + OX <=> HCXO + Pt ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 24," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/HC-O-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 25," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### OCX + HX <=> HCXO + Pt ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 25," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/H-CO-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 26," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### OCX + HX <=> CXOH + Pt ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 26," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/CO-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 27," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CXOH + Pt <=> CX + HOX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 27," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/C-OH-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 28," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CH2CH3X + Pt <=> CH2X + CH3X ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 28," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('beef-ensembles/CH2-CH3-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 29," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
