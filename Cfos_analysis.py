# -*- coding: utf-8 -*-
"""
Spyder Editor

Created by Joana Catarino

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import data for a single animal
data = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075_cells.csv')

# Info about the experiment
animal_id = 708075
genotype = 'Rbp4_Cre_neg'

# Create a new data frame that excludes the cells that were found outside the brain slice = root 
slice_data = data[~(data['acronym'] == 'root')]

#Check if there is any data in between hemispheres and remove it from the dataset
mid = slice_data[slice_data['ml_mm'] == 0]  
slice_data = slice_data[~(slice_data['ml_mm'] == 0)]

# Check which data is on each hemisphere 
right_hemisphere = slice_data[slice_data['ml_mm'] > 0]
left_hemisphere = slice_data[slice_data['ml_mm'] < 0]

# Create a column showing which data is on each hemisphere and rearrange index
slice_data['hemisphere'] = np.where(slice_data['ml_mm'] > 0, 'right', 'left')
slice_data = slice_data.drop(columns=['Unnamed: 0']) # This column contains the old index so we don't need it
slice_data = slice_data.reset_index(drop=True)

# Plot total expression on right versus left hemispere
right_cells = len(slice_data[slice_data['hemisphere'] == 'right']) #Total amount of cells in the right hemisphere
left_cells = len(slice_data[slice_data['hemisphere'] == 'left']) #Total amount of cells in the left hemisphere






ax = slice_data.plot.bar(x=(slice_data[slice_data['hemisphere']]), y=len(slice_data[slice_data['hemisphere']]), rot=0)


