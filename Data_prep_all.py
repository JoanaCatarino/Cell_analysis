# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 17:54:32 2024

@author: JoanaCatarino

Script to pre-process several files at the same time
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import emoji

# Import csv file with experiments' info for all the animals 
info = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/Experiment_info.csv', sep=';')

for i in (info.Animal):
    
    print ('Starting', i)
 
    # Select the animal to pre-process
    animal_id = i
    
    # Import data for that animal
    data = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/data_raw/'f'{animal_id}_cells.csv')
    
    # Remove the column 'Unnamed' because it is not giving any extra information
    data = data.drop(columns=['Unnamed: 0'])
    
    # Create a new data frame that excludes the cells that were found outside the brain slice = root 
    data = data[~(data['acronym'] == 'root')]
    data = data.reset_index(drop=True) # Reset index
    
    # Check if there are any cells located the middle of the two hemispheres and remove it from the dataset
    mid = data[data['ml_mm'] == 0]  
    data = data[~(data['ml_mm'] == 0)]
    
    # Check which data is on each hemisphere 
    right_hemisphere = data[data['ml_mm'] > 0]
    left_hemisphere = data[data['ml_mm'] < 0]
    
    # Create a column showing which data is on each hemisphere
    data['hemisphere'] = np.where(data['ml_mm'] > 0, 'right', 'left')
    
    # To create a column with only the region in which the cell is
    region=[] # create
    
    for name in data['name'].values:
        region.append(name.split(',')[0])
    
    data['region'] = region # Add column that only include regions to the dataframe
    
    # To create a column with the part of the region where the cell is
    part=[]
    
    for name in data['name'].values:
        #print(name.split(','))
        if len(name.split(',')) == 3:
            if name.split(',')[1].endswith('part'):
                part.append(name.split(',')[1])
            else:part.append(None)
    
        elif len(name.split(',')) == 2:
            if name.split(',')[-1].endswith('part'): # remove this to work a bit better
                part.append(name.split(',')[-1])
            else:
                part.append(None)
        else:
            part.append(None)      
    
    data['part'] = part
    
    # To create a column with the layer in which the cell is
    layer=[]
     
    for name in data['name'].values:
        #print(name.split(','))
        if len(name.split(',')) == 3:
            if name.split(',')[-1].startswith(' layer'):
                layer.append(name.split(',')[-1])
            else:layer.append(None)
    
        elif len(name.split(',')) == 2:
            if name.split(',')[-1].startswith(' layer') or name.split(',')[-1].startswith(' Layer') : # remove this to work a bit better
                layer.append(name.split(',')[-1])
            else:
                layer.append(None)
        else:
            layer.append(None)
            
    data['layer'] = layer
    
    # Remove the initial column that had all the info about region, part and layer together 
    data = data.drop(columns=['name'])
    
    # Save this pre-processed table without more experiment info 
    data.to_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/data/'f'{animal_id}_data.csv')
    
    # Create a new data frame that contains Napari pre-processed data and more experiment info
    data_pp = [] # pp stands for pre-processed
    data_pp = data
    
    # Insert column with animal id
    data_pp.insert(0, 'animal_id', animal_id)
    
    # Add sex of the animal to the initial data frame
    genotype = info.loc[(info.Animal == animal_id), 'Genotype'].values[0]
    data_pp['genotype'] = genotype
    
    # Add sex of the animal to the initial data frame
    sex = info.loc[(info.Animal == animal_id), 'Sex'].values[0]
    data_pp['sex'] = sex
    
    # Add injected hemisphere to the initial data frame
    injection = info.loc[(info.Animal == animal_id, 'Injection slice')].values[0]
    data_pp['injection'] = injection
    
    # Add injected area to the initial data frame
    inj_area = info.loc[(info.Animal == animal_id, 'Injected area')].values[0]
    data_pp['inj_area'] = inj_area
    
    # Add injected area to the initial data frame
    virus = info.loc[(info.Animal == animal_id, 'Virus')].values[0]
    data_pp['virus'] = virus
    
    # Add stimulated hemisphere to the data frame 
    stimulation = info.loc[(info.Animal == animal_id, 'Stimulated slice')].values[0]
    data_pp['stimulation'] = stimulation
    
    # Reorganize the columns within the data frame
    data_pp = data_pp.loc[:,['animal_id','genotype','sex','acronym','region','part','layer','hemisphere','injection',
                             'inj_area','virus','stimulation','structure_id','ap_mm','dv_mm','ml_mm','ap_coords',
                             'dv_coords','ml_coords','section_name']]
        
    # Save new data
    data_pp.to_csv('/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/data_prep/'f'{animal_id}_data_pp.csv')
    
    print('Finished for', i)
    
print(emoji.emojize('DONE :star-struck:\U0001F42D'))
