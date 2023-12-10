# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:53:46 2023

@author: JoanaCatarino

Script to organize the data that Napari generates to be in a more user friendly format and to contain only the information needed for 
the type of analysis we want

IMP!!!! csv file needs to contain the injected side and the stimulated side 
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Import data for a single animal
data = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/708075_cells.csv')  #For desktop

# CSV file with relevant infromation for experiment
info = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/Experiment_info.csv', sep=';')

# Remove the column 'Unnamed' because it is not giving any extra information
data = data.drop(columns=['Unnamed: 0'])

# Create a new data frame that excludes the cells that were found outside the brain slice = root and reset index
slice_data = data[~(data['acronym'] == 'root')]
slice_data = slice_data.reset_index(drop=True)

# Check if there are any cells located the middle of the two hemispheres and remove it from the dataset
mid = slice_data[slice_data['ml_mm'] == 0]  
slice_data = slice_data[~(slice_data['ml_mm'] == 0)]

# Check which data is on each hemisphere 
right_hemisphere = slice_data[slice_data['ml_mm'] > 0]
left_hemisphere = slice_data[slice_data['ml_mm'] < 0]

# Create a column showing which data is on each hemisphere
slice_data['hemisphere'] = np.where(slice_data['ml_mm'] > 0, 'right', 'left')

# To create a column with layers (teste again if this is working)
region=[]

for name in slice_data['name'].values:
    region.append(name.split(',')[0])
print(region)

slice_data['region'] = region # Add column that only include regions to the dataframe

# To create a column with the part of the regions where the cells are 
part=[]

for name in slice_data['name'].values:
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

slice_data['part'] = part

# To create a column with the layer in which the cells are
layer=[]
 
for name in slice_data['name'].values:
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
        
slice_data['layer'] = layer

# Remove the initial column that had all the info about region, part and layer together 
slice_data = slice_data.drop(columns=['name'])

# For futere improvement:
 # Remove columns with information about slide
 # Add a new one that only contains the animal number
 # Add column with injection site and stimulated side from csv file that contains info for all animals
 



