# -*- coding: utf-8 -*-
"""
Spyder Editor

Created by Joana Catarino

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Import data for a single animal
data = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075_cells.csv')  #For desktop
#data = pd.read_csv('/Users/joanacatarino/Desktop/708075_cells.csv') #For mac


# Info about the experiment
animal_id = 708075
genotype = 'Rbp4 Cre_neg'


# Create a new data frame that excludes the cells that were found outside the brain slice = root 
slice_data = data[~(data['acronym'] == 'root')]

# Check if there are any cells located the middle of the two hemispheres and remove it from the dataset
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

x = ['Right Hemisphere', 'Left Hemisphere']
y = [right_cells, left_cells] 
color= ['#85BDA6', '#08605F'] # Select color for the bars, light green for right hemisphere and dark green for left hemisphere

fig, ax = plt.subplots(1,1, figsize=(3.8,5), dpi= 500)
ax.bar(x, y, width=0.4, color=color)
ax.set(ylim=(0,10000))
ax.set_title(f'#{animal_id}  {genotype}', fontsize=11, x=0.4 , y=1.02)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.margins(x=0.2)
plt.ylabel('Total number of cells', fontsize=10)
plt.tight_layout()
sns.despine()
plt.show()


