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

injection_site = 'left'

for i in (data_total):
    print('Starting', i.animal_id[0])
    #Left hemisphere
    PL_left = len(i[(i.hemisphere == 'left') & (i.region == 'Prelimbic area')]) 
    ILA_left = len(i[(i.hemisphere == 'left') & (i.region == 'Infralimbic area')]) 
    ACAd_left = len(i[(i.hemisphere == 'left') & (i.region == 'Anterior cingulate area') & (i.position == ' dorsal part')])
    ACAv_left = len(i[(data.hemisphere == 'left') & (i.region == 'Anterior cingulate area') & (i.position == ' ventral part')])
    ORBm_left = len(i[(data.hemisphere == 'left') & (i.region == 'Orbital area') & (i.position == ' medial part')])
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
    AIv_right = len(i[(data.hemisphere == 'right') & (i.region == 'Agranular insular area') & (i.position == ' ventral part')])
    
    # Concatenate all this in one table
    data_table = [[i.animal_id[0],'PL', PL_left, 'left'],
                  [i.animal_id[0],'IL', ILA_left, 'left'], 
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
    
    PL_test = concat_df.Cells[(concat_df.Region == 'PL') & (concat_df.Hemisphere != injection_site)]
    
    
    
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

    ratio_df = pd.DataFrame(data_table, columns=['Animal', 'Region', 'ratio']) 
    
     
    print('Done with', i.animal_id[0])
    
print('Done for all animals!')






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




#%%
# initialize list of lists 
data = [['tom', 10], ['nick', 15], ['juli', 14]] 
  
# Create the pandas DataFrame 
df = pd.DataFrame(data, columns=['Name', 'Age']) 
  

data_table = [[animal_id,'PL_left', PL_left, 'left'], [animal_id,'ILA_left', ILA_left. 'left'], [animal_id, 'ACAd_left', ACAd_left, 'left'], [animal_id,'ACAv_left', ACAv_left, 'left'], 
              ['ORBm_left', ORBm_left, 'left'], ['ORBl_left', ORBl_left, 'left'], ['ORBvl_left', ORBvl_left, 'left'], MOs_left, AId_left, AIv_left,
        PL_right, ILA_right, ACAd_right, ACAv_right, ORBm_right, ORBl_right, ORBvl_right, MOs_right, AId_right, AIv_right]



df=pd.DataFrame(labels,columns=['Regions'], data, columns=['cells'])
df=pd.DataFrame(data, columns=['Cells'])



#just to keep 
  data_table = [[i.animal_id[0],'PL_left', PL_left, 'left'],
                [i.animal_id[0],'ILA_left', ILA_left, 'left'], 
                [i.animal_id[0], 'ACAd_left', ACAd_left, 'left'],
                [i.animal_id[0],'ACAv_left', ACAv_left, 'left'], 
                [i.animal_id[0],'ORBm_left', ORBm_left, 'left'], 
                [i.animal_id[0],'ORBl_left', ORBl_left, 'left'],
                [i.animal_id[0],'ORBvl_left', ORBvl_left, 'left'], 
                [i.animal_id[0], 'MOs_left', MOs_left,'left'], 
                [i.animal_id[0], 'AId_left', AId_left,'left'], 
                [i.animal_id[0], 'AIv_left', AIv_left,'left'],
                [i.animal_id[0], 'PL_right', PL_right, 'right'],
                [i.animal_id[0], 'ILA_right', ILA_right, 'right'],
                [i.animal_id[0], 'ACAd_right', ACAd_right, 'right'],
                [i.animal_id[0], 'ACAv_right', ACAv_right, 'right'],
                [i.animal_id[0], 'ORBm_right', ORBm_right, 'right'],
                [i.animal_id[0], 'ORBl_right', ORBl_right, 'right'],
                [i.animal_id[0], 'ORBvl_right', ORBvl_right, 'right'],
                [i.animal_id[0], 'MOs_right', MOs_right, 'right'],
                [i.animal_id[0], 'AId_right', AId_right, 'right'], 
                [i.animal_id[0], 'AIv_right', AIv_right, 'right']]

  ratio_df = pd.DataFrame(data_table, columns=['Animal', 'Region', 'Cells', 'Hemisphere']) 
   