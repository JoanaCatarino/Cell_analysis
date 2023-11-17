# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:32:06 2023

@author: JoanaCatarino
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Import data for all the animals and drop new index
data = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/714000/714000_slice_data.csv')
data = data.drop(columns=['Unnamed: 0'])

# Info about the experiment
animal_id = data.animal_id[0]
genotype = 'Tlx3 Cre_pos'
injection = 'left'

#Left hemisphere
PL_left = len(data[(data.hemisphere == 'left') & (data.region == 'Prelimbic area')]) 
ILA_left = len(data[(data.hemisphere == 'left') & (data.region == 'Infralimbic area')]) 
ACAd_left = len(data[(data.hemisphere == 'left') & (data.region == 'Anterior cingulate area') & (data.position == ' dorsal part')])
ACAv_left = len(data[(data.hemisphere == 'left') & (data.region == 'Anterior cingulate area') & (data.position == ' ventral part')])
ORBm_left = len(data[(data.hemisphere == 'left') & (data.region == 'Orbital area') & (data.position == ' medial part')])
ORBl_left = len(data[(data.hemisphere == 'left') & (data.region == 'Orbital area') & (data.position == ' lateral part')])
ORBvl_left = len(data[(data.hemisphere == 'left') & (data.region == 'Orbital area') & (data.position == ' ventrolateral part')])
MOs_left = len(data[(data.hemisphere == 'left') & (data.region == 'Secondary motor area')])
AId_left = len(data[(data.hemisphere == 'left') & (data.region == 'Agranular insular area') & (data.position == ' dorsal part')])
AIv_left = len(data[(data.hemisphere == 'left') & (data.region == 'Agranular insular area') & (data.position == ' ventral part')])

#Right hemisphere
PL_right = len(data[(data.hemisphere == 'right') & (data.region == 'Prelimbic area')]) 
ILA_right = len(data[(data.hemisphere == 'right') & (data.region == 'Infralimbic area')]) 
ACAd_right = len(data[(data.hemisphere == 'right') & (data.region == 'Anterior cingulate area') & (data.position == ' dorsal part')])
ACAv_right = len(data[(data.hemisphere == 'right') & (data.region == 'Anterior cingulate area') & (data.position == ' ventral part')])
ORBm_right = len(data[(data.hemisphere == 'right') & (data.region == 'Orbital area') & (data.position == ' medial part')])
ORBl_right = len(data[(data.hemisphere == 'right') & (data.region == 'Orbital area') & (data.position == ' lateral part')])
ORBvl_right = len(data[(data.hemisphere == 'right') & (data.region == 'Orbital area') & (data.position == ' ventrolateral part')])
MOs_right = len(data[(data.hemisphere == 'right') & (data.region == 'Secondary motor area')])
AId_right = len(data[(data.hemisphere == 'right') & (data.region == 'Agranular insular area') & (data.position == ' dorsal part')])
AIv_right = len(data[(data.hemisphere == 'right') & (data.region == 'Agranular insular area') & (data.position == ' ventral part')])

# Normalization (ratio)
PL_norm = round((PL_left/PL_right), 1)
ILA_norm = round((ILA_left/ILA_right), 1)
ACAd_norm = round((ACAd_left/ACAd_right), 1)
ACAv_norm = round((ACAv_left/ACAv_right), 1)
ORBm_norm = round((ORBm_left/ORBm_right), 1)
ORBl_norm = round((ORBl_left/ORBl_right), 1)
ORBvl_norm = round((ORBvl_left/ORBvl_right), 1)
MOs_norm = round((MOs_left/MOs_right), 1)
AId_norm = round((AId_left/AId_right),1)
AIv_norm = round((AIv_left/AIv_right), 1)

# Plot normalized expression
x=['PL', 'ILA', 'ACAd', 'ACAv','ORBm', 'ORBl', 'ORBvl', 'MOs', 'AId', 'AIv']
y=[PL_norm, ILA_norm, ACAd_norm, ACAv_norm, ORBm_norm, ORBl_norm, ORBvl_norm, MOs_norm, AId_norm, AIv_norm]

fig,ax = plt.subplots(1,1, figsize=(10,7), dpi= 500)

ax.bar(x, y, width=0.45, color='#3C5A14')
ax.set(ylim=(0,20))
ax.set_ylabel('Increase in expression in injected hemisphere', labelpad=10, fontsize=10)
ax.set_title(f'#{animal_id}  {genotype}', fontsize=10, x=0.5 , y=1.05)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/714000/Figures/'f'{animal_id}_PFC_ratio.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/714000/Figures/'f'{animal_id}_PFC_ratio.pdf', transparent=True)

#%%

# Import data for all the animals and drop new index
data1 = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/708075_slice_data.csv')
data1 = data1.drop(columns=['Unnamed: 0'])
data2 = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/714000/714000_slice_data.csv')
data2 = data2.drop(columns=['Unnamed: 0'])
data3 = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/714001/714001_slice_data.csv')
data3 = data3.drop(columns=['Unnamed: 0'])


data_total = [data1, data2, data3]

injection_site = 'left' # this needs to be in the initial dataframe and needs to be moved inside the loop

for i in (data_total):
    print('Starting', i.animal_id[0])
    
    animal_id = i.animal_id[0]
    
    #Left hemisphere
    PL_left = len(i[(i.hemisphere == 'left') & (i.region == 'Prelimbic area')]) 
    ILA_left = len(i[(i.hemisphere == 'left') & (i.region == 'Infralimbic area')]) 
    ACAd_left = len(i[(i.hemisphere == 'left') & (i.region == 'Anterior cingulate area') & (i.position == ' dorsal part')])
    ACAv_left = len(i[(i.hemisphere == 'left') & (i.region == 'Anterior cingulate area') & (i.position == ' ventral part')])
    ORBm_left = len(i[(i.hemisphere == 'left') & (i.region == 'Orbital area') & (i.position == ' medial part')])
    ORBl_left = len(i[(i.hemisphere == 'left') & (i.region == 'Orbital area') & (i.position == ' lateral part')])
    ORBvl_left = len(i[(i.hemisphere == 'left') & (i.region == 'Orbital area') & (i.position == ' ventrolateral part')])
    MOs_left = len(i[(i.hemisphere == 'left') & (i.region == 'Secondary motor area')])
    AId_left = len(i[(i.hemisphere == 'left') & (i.region == 'Agranular insular area') & (i.position == ' dorsal part')])
    AIv_left = len(i[(i.hemisphere == 'left') & (i.region == 'Agranular insular area') & (i.position == ' ventral part')])
    
    #Right hemisphere
    PL_right = len(i[(i.hemisphere == 'right') & (i.region == 'Prelimbic area')]) 
    ILA_right = len(i[(i.hemisphere == 'right') & (i.region == 'Infralimbic area')]) 
    ACAd_right = len(i[(i.hemisphere == 'right') & (i.region == 'Anterior cingulate area') & (i.position == ' dorsal part')])
    ACAv_right = len(i[(i.hemisphere == 'right') & (i.region == 'Anterior cingulate area') & (i.position == ' ventral part')])
    ORBm_right = len(i[(i.hemisphere == 'right') & (i.region == 'Orbital area') & (i.position == ' medial part')])
    ORBl_right = len(i[(i.hemisphere == 'right') & (i.region == 'Orbital area') & (i.position == ' lateral part')])
    ORBvl_right = len(i[(i.hemisphere == 'right') & (i.region == 'Orbital area') & (i.position == ' ventrolateral part')])
    MOs_right = len(i[(i.hemisphere == 'right') & (i.region == 'Secondary motor area')])
    AId_right = len(i[(i.hemisphere == 'right') & (i.region == 'Agranular insular area') & (i.position == ' dorsal part')])
    AIv_right = len(i[(i.hemisphere == 'right') & (i.region == 'Agranular insular area') & (i.position == ' ventral part')])
    
    # Concatenate all this in one table
    data_table = [[i.animal_id[0],'PL', PL_left, 'left'],
                  [i.animal_id[0],'ILA', ILA_left, 'left'], 
                  [i.animal_id[0], 'ACAd', ACAd_left, 'left'],
                  [i.animal_id[0],'ACAv', ACAv_left, 'left'], 
                  [i.animal_id[0],'ORBm', ORBm_left, 'left'], 
                  [i.animal_id[0],'ORBl', ORBl_left, 'left'],
                  [i.animal_id[0],'ORBvl', ORBvl_left, 'left'], 
                  [i.animal_id[0], 'MOs', MOs_left,'left'], 
                  [i.animal_id[0], 'AId', AId_left,'left'], 
                  [i.animal_id[0], 'AIv', AIv_left,'left'],
                  [i.animal_id[0], 'PL', PL_right, 'right'],
                  [i.animal_id[0], 'ILA', ILA_right, 'right'],
                  [i.animal_id[0], 'ACAd', ACAd_right, 'right'],
                  [i.animal_id[0], 'ACAv', ACAv_right, 'right'],
                  [i.animal_id[0], 'ORBm', ORBm_right, 'right'],
                  [i.animal_id[0], 'ORBl', ORBl_right, 'right'],
                  [i.animal_id[0], 'ORBvl', ORBvl_right, 'right'],
                  [i.animal_id[0], 'MOs', MOs_right, 'right'],
                  [i.animal_id[0], 'AId', AId_right, 'right'], 
                  [i.animal_id[0], 'AIv', AIv_right, 'right']]
    
    concat_df = pd.DataFrame(data_table, columns=['Animal', 'Region', 'Cells', 'Hemisphere']) 
    
    #Normalizaton (ratio)
    PL_norm = round((concat_df.Cells[(concat_df.Region == 'PL') & (concat_df.Hemisphere == injection_site)].values[0]) / 
                    (concat_df.Cells[(concat_df.Region == 'PL') & (concat_df.Hemisphere != injection_site)].values[0]), 1)  # injection side / non injection side
    ILA_norm = round((concat_df.Cells[(concat_df.Region == 'ILA') & (concat_df.Hemisphere == injection_site)].values[0]) / 
                     (concat_df.Cells[(concat_df.Region == 'ILA') & (concat_df.Hemisphere != injection_site)].values[0]), 1)  
    ACAd_norm = round((concat_df.Cells[(concat_df.Region == 'ACAd') & (concat_df.Hemisphere == injection_site)].values[0]) / 
                      (concat_df.Cells[(concat_df.Region == 'ACAd') & (concat_df.Hemisphere != injection_site)].values[0]), 1)  
    ACAv_norm = round((concat_df.Cells[(concat_df.Region == 'ACAv') & (concat_df.Hemisphere == injection_site)].values[0]) / 
                    (concat_df.Cells[(concat_df.Region == 'ACAv') & (concat_df.Hemisphere != injection_site)].values[0]), 1)  
    ORBm_norm = round((concat_df.Cells[(concat_df.Region == 'ORBm') & (concat_df.Hemisphere == injection_site)].values[0]) / 
                    (concat_df.Cells[(concat_df.Region == 'ORBm') & (concat_df.Hemisphere != injection_site)].values[0]), 1)  
    ORBl_norm = round((concat_df.Cells[(concat_df.Region == 'ORBl') & (concat_df.Hemisphere == injection_site)].values[0]) / 
                    (concat_df.Cells[(concat_df.Region == 'ORBl') & (concat_df.Hemisphere != injection_site)].values[0]), 1)  
    ORBvl_norm = round((concat_df.Cells[(concat_df.Region == 'ORBvl') & (concat_df.Hemisphere == injection_site)].values[0]) / 
                    (concat_df.Cells[(concat_df.Region == 'ORBvl') & (concat_df.Hemisphere != injection_site)].values[0]), 1)  
    MOs_norm = round((concat_df.Cells[(concat_df.Region == 'MOs') & (concat_df.Hemisphere == injection_site)].values[0]) / 
                    (concat_df.Cells[(concat_df.Region == 'MOs') & (concat_df.Hemisphere != injection_site)].values[0]), 1)  
    AId_norm = round((concat_df.Cells[(concat_df.Region == 'AId') & (concat_df.Hemisphere == injection_site)].values[0]) / 
                    (concat_df.Cells[(concat_df.Region == 'AId') & (concat_df.Hemisphere != injection_site)].values[0]), 1) 
    AIv_norm = round((concat_df.Cells[(concat_df.Region == 'AIv') & (concat_df.Hemisphere == injection_site)].values[0]) / 
                    (concat_df.Cells[(concat_df.Region == 'AIv') & (concat_df.Hemisphere != injection_site)].values[0]), 1)  
    
    # Save the values in a new DataFrame
    data_table = [[i.animal_id[0],'PL', PL_norm],
                  [i.animal_id[0],'ILA', ILA_norm], 
                  [i.animal_id[0], 'ACAd', ACAd_norm],
                  [i.animal_id[0],'ACAv', ACAv_norm], 
                  [i.animal_id[0],'ORBm', ORBm_norm], 
                  [i.animal_id[0],'ORBl', ORBl_norm],
                  [i.animal_id[0],'ORBvl', ORBvl_norm], 
                  [i.animal_id[0], 'MOs', MOs_norm], 
                  [i.animal_id[0], 'AId', AId_norm], 
                  [i.animal_id[0], 'AIv', AIv_norm]]

    # Name the columns in the new dataframe
    ratio_df = pd.DataFrame(data_table, columns=['Animal', 'Region', 'Ratio']) 
    
    # Replace NAN with 0
    ratio_df['Ratio'] = ratio_df['Ratio'].fillna(0)
    
    # Save new dataframe
    ratio_df.to_csv('/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/ratio_df/'f'{animal_id}_ratio_df.csv')

    print('Done with', i.animal_id[0])
    
print('Done for all animals!')

# Plot ratio for all animals in the same figure

# Load data 

data708075 = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/ratio_df/708075_ratio_df.csv')
data708075 = data708075.drop(columns=['Unnamed: 0'])
data714000 = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/ratio_df/714000_ratio_df.csv')
data714000 = data714000.drop(columns=['Unnamed: 0'])
data714001 = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/ratio_df/714001_ratio_df.csv')
data714001 = data714001.drop(columns=['Unnamed: 0'])

# Plot for both hemispheres in the same figure - grouped bar plot
x = np.arange(10) 
y_708075= data708075.Ratio
y_714000= data714000.Ratio
y_714001= data714001.Ratio

color1 = '#023C40'
color2 = '#549F93'
color3 = '#9FAF90'

width = 0.25
  
# plot data in grouped manner of bar type 
fig, ax = plt.subplots(1,1, layout='constrained', figsize=(18,6), dpi= 500)

plt.bar(x-0.25, y_708075, width=width, color=color1) 
plt.bar(x, y_714000, width=width, color=color2) 
plt.bar(x+0.25, y_714001, width=width, color=color3) 

ax.set_xticks(x, ['PL', 'ILA', 'ACAd', 'ACAv', 'ORBm', 'ORBl', 'ORBvl', 'MOs', 'AId', 'AIv']) 
ax.legend(['708075', '714000', '714001'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Increase in expression', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[2], fontsize=8.5, color='#494949', padding=3)
#ax.set_title(f'#{animal_id}  {genotype}', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 18)

plt.tight_layout(pad=2)
sns.despine()