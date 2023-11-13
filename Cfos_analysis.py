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

#Import modules for stats
from numpy.random import seed 
from numpy.random import randn 
from numpy.random import normal 
from scipy.stats import ttest_ind


# Import data for a single animal
#data = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075_cells.csv')  #For desktop
data = pd.read_csv('/Users/joanacatarino/Desktop/708075_cells.csv') #For mac

# Info about the experiment
animal_id = 708075
genotype = 'Rbp4 Cre_neg'
injection = 'left'

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

fig, ax = plt.subplots(1,1, figsize=(4,5), dpi= 500)
ax.bar(x, y, width=0.4, color=color)
ax.set(ylim=(0,10000))
ax.set_title(f'#{animal_id}  {genotype}', fontsize=11, fontweight='bold', x=0.4 , y=1.05)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.margins(x=0.2)
plt.ylabel('Total number of cells', fontsize=10, labelpad=8)
plt.tight_layout()
sns.despine()
plt.show()

#plt.savefig('/Users/joanacatarino/Desktop/Results/Total_cells.png')
#plt.savefig('/Users/joanacatarino/Desktop/Results/Total_cells.pdf')

# In case we want to save the new data frame:
#slice_data.to_csv('/Users/joanacatarino/Desktop/Results/slice_data.csv')

#%%

# Quantify total number of cells in PFC for each hemisphere
    # PFC subregions to include: PL, ILA, ACAd, ACAv, ORBm, ORBl, ORBvl

# Create a new column that only includes the name of the region without specifying the layer
slice_data['region'], slice_data['layer'] = slice_data['name'].str.split(',', n=1).str

# Create a new colum with the position inside a region (medial, lateral, etc) to be used later
slice_data['position'], slice_data['layer4real'] = slice_data['layer'].str.split(',', n=1).str #It works but needs to be improved


# Get regions of interest (don't discriminate dorsal, ventral, medial, lateral, layers)
PL_left = slice_data[(slice_data.hemisphere == 'left') & (slice_data.region == 'Prelimbic area')] 
ILA_left = slice_data[(slice_data.hemisphere == 'left') & (slice_data.region == 'Infralimbic area')] 
ACA_left = slice_data[(slice_data.hemisphere == 'left') & (slice_data.region == 'Anterior cingulate area')] 
ORB_left = slice_data[(slice_data.hemisphere == 'left') & (slice_data.region == 'Orbital area')] 

PL_right = slice_data[(slice_data.hemisphere == 'right') & (slice_data.region == 'Prelimbic area')] 
ILA_right = slice_data[(slice_data.hemisphere == 'right') & (slice_data.region == 'Infralimbic area')] 
ACA_right = slice_data[(slice_data.hemisphere == 'right') & (slice_data.region == 'Anterior cingulate area')] 
ORB_right = slice_data[(slice_data.hemisphere == 'right') & (slice_data.region == 'Orbital area')] 

# Get amount of cells in each region of interest
PL_left_cells = PL_left[PL_left.columns[0]].count() 
ILA_left_cells = ILA_left[ILA_left.columns[0]].count() 
ACA_left_cells = ACA_left[ACA_left.columns[0]].count() 
ORB_left_cells = ORB_left[ORB_left.columns[0]].count() 

PL_right_cells = PL_right[PL_right.columns[0]].count() 
ILA_right_cells = ILA_right[ILA_right.columns[0]].count() 
ACA_right_cells = ACA_right[ACA_right.columns[0]].count() 
ORB_right_cells = ORB_right[ORB_right.columns[0]].count() 

# Get total amount of cells in PFC for each hemisphere
PFC_left = PL_left_cells + ILA_left_cells + ACA_left_cells + ORB_left_cells
PFC_right = PL_right_cells + ILA_right_cells + ACA_right_cells + ORB_right_cells


# Plot number of cells in PFC for each hemisphere
x = ['PFC right', 'PFC left']
y = [PFC_right, PFC_left] 
color= ['#B598AF', '#623B5A'] # Select color for the bars, light purple for right hemisphere and dark purple for left hemisphere

fig, ax = plt.subplots(1,1, figsize=(4,5), dpi= 500)
ax.bar(x, y, width=0.4, color=color)
ax.set(ylim=(0,10000))
ax.set_title(f'#{animal_id}  {genotype}', fontsize=11, fontweight='bold', x=0.4 , y=1.05)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.margins(x=0.2)
plt.ylabel('Total number of cells', fontsize=10, labelpad=8)
plt.tight_layout()
sns.despine()
plt.show()

#plt.savefig('/Users/joanacatarino/Desktop/Results/PFC_cells.png')
#plt.savefig('/Users/joanacatarino/Desktop/Results/PFC_cells.pdf')


#Plot total number of cells and PFC cells

x = ['Right Hemisphere', 'Left Hemisphere']
data_total = [right_cells, left_cells]
data_pfc = [PFC_right, PFC_left]

color_total = ['#08605F']
color_pfc = ['#623B5A'] 

fig, ax = plt.subplots(1,1, figsize=(4,5), dpi=500)
ax.bar(x=x, height=data_total, width=0.4, align='center', color=color_total, label='Total cells')
ax.bar(x=x, height=data_pfc, width=0.4, align='center', color=color_pfc, label='PFC cells')
ax.set(ylim=(0,10000))
ax.set_title(f'#{animal_id}  {genotype}', fontsize=11, fontweight='bold', x=0.4 , y=1.05)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#F4EDED', padding=3)
ax.legend(labels=['All cells', 'PFC cells'], fontsize=9, frameon=False)
ax.margins(x=0.2)
plt.ylabel('Total number of cells', fontsize=10, labelpad=8)
plt.tight_layout()
sns.despine()
plt.show()

#plt.savefig('/Users/joanacatarino/Desktop/Results/ratio.png')
#plt.savefig('/Users/joanacatarino/Desktop/Results/ratio.pdf')

#%%

# Compare the number of cells between different PFC subregions for each hemisphere
    # Regions to include: PL, ILA, ACAd, ACAv, ORBm, ORBl, ORBvl, Mos, AId, AIv


#Left hemisphere
PL_left = len(slice_data[(slice_data.hemisphere == 'left') & (slice_data.region == 'Prelimbic area')]) 
ILA_left = len(slice_data[(slice_data.hemisphere == 'left') & (slice_data.region == 'Infralimbic area')]) 
ACA_left = len(slice_data[(slice_data.hemisphere == 'left') & (slice_data.region == 'Anterior cingulate area')]) #There is no ACAv in this dataset so we can use the general ACA to represent ACAd
ORBm_left = len(ORB_left[(ORB_left.position == ' medial part')])
ORBl_left = len(ORB_left[(ORB_left.position == ' lateral part')])
ORBvl_left = len(ORB_left[(ORB_left.position == ' ventrolateral part')])
MOs_left = len(slice_data[(slice_data.hemisphere == 'left') & (slice_data.region == 'Secondary motor area')])
AId_left = len(slice_data[(slice_data.hemisphere == 'left') & (slice_data.region == 'Agranular insular area')& (slice_data.position == ' dorsal part')])
AIv_left = len(slice_data[(slice_data.hemisphere == 'left') & (slice_data.region == 'Agranular insular area')& (slice_data.position == ' ventral part')])

#Right hemisphere
PL_right = len(slice_data[(slice_data.hemisphere == 'right') & (slice_data.region == 'Prelimbic area')]) 
ILA_right = len(slice_data[(slice_data.hemisphere == 'right') & (slice_data.region == 'Infralimbic area')]) 
ACA_right = len(slice_data[(slice_data.hemisphere == 'right') & (slice_data.region == 'Anterior cingulate area')]) #There is no ACAv in this dataset so we can use the general ACA to represent ACAd
ORBm_right = len(ORB_right[(ORB_right.position == ' medial part')])
ORBl_right = len(ORB_right[(ORB_right.position == ' lateral part')])
ORBvl_right = len(ORB_right[(ORB_right.position == ' ventrolateral part')])
MOs_right = len(slice_data[(slice_data.hemisphere == 'right') & (slice_data.region == 'Secondary motor area')])
AId_right = len(slice_data[(slice_data.hemisphere == 'right') & (slice_data.region == 'Agranular insular area')& (slice_data.position == ' dorsal part')])
AIv_right = len(slice_data[(slice_data.hemisphere == 'right') & (slice_data.region == 'Agranular insular area')& (slice_data.position == ' ventral part')])

#Plot for both hemispheres separately

x=['PL', 'ILA', 'ACA', 'ORBm', 'ORBl', 'ORBvl', 'MOs', 'AId', 'AIv']
y_left=[PL_left, ILA_left, ACA_left, ORBm_left, ORBl_left, ORBvl_left, MOs_left, AId_left, AIv_left]
y_right=[PL_right, ILA_right, ACA_right, ORBm_right, ORBl_right, ORBvl_right, MOs_right, AId_right, AIv_right]
color_left =  '#3C5A14'
color_right = '#7EA967'

fig, (ax1, ax2) = plt.subplots(2,1, figsize=(7,7), dpi= 500)
fig.suptitle(f'#{animal_id}  {genotype}', fontsize=11, fontweight='bold')
plt.subplots_adjust(hspace=0.1)

ax1.bar(x, y_left, width=0.4, color=color_left)
ax1.set(ylim=(0,2500))
ax1.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
ax1.set_title('Left Hemisphere', fontsize=10, x=0.5 , y=1.05)
ax1.bar_label(ax1.containers[0], fontsize=8.5, color='#494949', padding=3)

ax2.bar(x, y_right, width=0.4, color=color_right)
ax2.set(ylim=(0,2500))
ax2.set_title('Right Hemisphere', fontsize=10, x=0.5 , y=1.05)
ax2.bar_label(ax2.containers[0], fontsize=8.5, color='#494949', padding=3)
ax2.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
plt.tight_layout(pad=2)
sns.despine()
plt.show()



# Plot for both hemispheres in the same figure - grouped bar plot

x = np.arange(9) 
y_left=[PL_left, ILA_left, ACA_left, ORBm_left, ORBl_left, ORBvl_left, MOs_left, AId_left, AIv_left]
y_right=[PL_right, ILA_right, ACA_right, ORBm_right, ORBl_right, ORBvl_right, MOs_right, AId_right, AIv_right]
color_right = '#7EA967'
color_left =  '#3C5A14'
width = 0.4
  
# plot data in grouped manner of bar type 
fig, ax = plt.subplots(1,1, layout='constrained', figsize=(10,6), dpi= 500)

plt.bar(x-0.4, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.2, ['PL', 'ILA', 'ACA', 'ORBm', 'ORBl', 'ORBvl', 'MOs', 'AId', 'AIv']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 2500)


plt.tight_layout(pad=2)
sns.despine()
plt.show()
 


 

