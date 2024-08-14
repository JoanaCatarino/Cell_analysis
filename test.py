# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:41:38 2024

@author: JoanaCatarino
"""

# right and left cells for all animals

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import emoji

# Import csv file with experiments' info for all the animals 
info = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/Experiment_info.csv', sep=';')

data_plot = pd.DataFrame(columns=['Animal','Right_hemisphere','Left_hemisphere']) 

for i in (info.Animal):
    
    print ('Starting', i)
    
    # Select the animal to pre-process
    animal_id = i
    
    # Import data for that animal
    data_pp = pd.read_csv('/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/data_prep/'f'{animal_id}_data_pp.csv')
    
    # Drop unnamed column
    data_pp = data_pp.drop(columns=['Unnamed: 0'])
    
    # Print stimulated hemisphere
    stim = data_pp.stimulation[0]
    print(stim)
    
    # Print genotype
    genotype = data_pp.genotype[0]
    print(genotype)
    
    # Plot total expression on right versus left hemispere
    right_cells = len(data_pp[data_pp['hemisphere'] == 'right']) #Total amount of cells in the right hemisphere
    left_cells = len(data_pp[data_pp['hemisphere'] == 'left']) #Total amount of cells in the left hemisphere

    # create new data frame with values to plot 
    data = pd.DataFrame([[animal_id, right_cells, left_cells]], columns=['Animal','Right_hemisphere','Left_hemisphere']) 
    data_plot = pd.concat([data_plot, data], ignore_index=True)
    
    print('Finished for', i)
    
print(emoji.emojize('DONE :star-struck:\U0001F42D'))

# plot data points for right versus left hemisphere
x1 = ['Right Hemisphere']
x2 = ['Left Hemisphere']
y1 = [data_plot.Right_hemisphere]
y2 = data_plot.Left_hemisphere
color= ['#85BDA6', '#08605F']

fig, ax = plt.subplots(1,1, figsize=(4,5), dpi= 500)
ax.bar(x1, y1, width=0.4, color=color)
ax.bar (x2, y2)
ax.set(ylim=(0,25000))
ax.set_title(f'#{animal_id}  {genotype}', fontsize=11, fontweight='bold', x=0.4 , y=1.05)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.margins(x=0.2)
plt.ylabel('Total number of cells', fontsize=10, labelpad=8)
plt.tight_layout()
sns.despine()


fig, ax = plt.subplots()
ax.bar(x,
       height=[np.mean(yi) for yi in y],
       yerr=[np.std(yi) for yi in y],    # error bars
       capsize=12, # error bar cap width in points
       width=w,    # bar width
       tick_label=["control", "test"],
       color=(0,0,0,0),  # face color transparent
       edgecolor=colors)

   