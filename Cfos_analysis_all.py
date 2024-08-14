# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:07:13 2024

@author: JoanaCatarino

Overall plots of expression between stimulated and non-stimulated hemispheres - to get a general picture of the data
- All animals ploted separately but in one go
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
    data_pp = pd.read_csv('/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/data_prep/'f'{animal_id}_data_pp.csv')
    
    # Drop unnamed column
    data_pp = data_pp.drop(columns=['Unnamed: 0'])
    
    # Print stimulated hemisphere
    stim = data_pp.stimulation[0]
    print(stim)
    
    # Print genotype
    genotype = data_pp.genotype[0]
    print(genotype)
    
    #Select dpi for the plots
    dpi = 500
    
    # Plot total expression on right versus left hemispere
    stim_cells = len(data_pp[data_pp['hemisphere'] == data_pp['stimulation']]) #Total amount of cells in stimulated hemisphere
    nonstim_cells = len(data_pp[data_pp['hemisphere'] != data_pp['stimulation']]) #Total amount of cells innon-stimulated hemisphere

    x = ['Stimulated\n Hemisphere', 'Non-Stimulated\n Hemisphere']
    y = [stim_cells, nonstim_cells] 
    ymax = (max(y) + 1000)

    fig, ax = plt.subplots(1,1, figsize=(4,5), dpi=dpi)
    ax.bar(x, y, width=0.4, color=['#85BDA6', '#08605F']) #light green for stim hemisph and dark green for non-stim hemisphere
    ax.set(ylim=(0,ymax))
    ax.set_title(f'#{animal_id}  {genotype}', fontsize=11, fontweight='bold', x=0.4 , y=1.05)
    ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
    ax.margins(x=0.2)
    plt.ylabel('Total number of cells', fontsize=10, labelpad=8)
    plt.tight_layout()
    sns.despine()
    
    #plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/Figures/Total_cells/'f'{animal_id}_Total_cells.png', transparent=True)
    #plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/Figures/Total_cells/'f'{animal_id}_Total_cells.pdf', transparent=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print('Finished for', i)
    
print(emoji.emojize('DONE :star-struck:\U0001F42D'))
