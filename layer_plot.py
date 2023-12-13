# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:29:05 2023

@author: JoanaCatarino

Plot data per layer - total number of cells and proportion of cells 

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Load data
slice_data = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/data_prep/708075_slice_data.csv')
slice_data = slice_data.drop(columns=['Unnamed: 0'])

# Animal info
animal_id = 708075
genotype = 'Rbp4 Cre-neg'

# See in which layers of the regions we want to plot the cells are 
 # PL, ILA, ACAd, ACAv, ORBm, ORBl, ORBvl, Mos, AId, AIv

PL_layers = slice_data[slice_data.region == 'Prelimbic area']
print(PL_layers.layer.unique())

ILA_layers = slice_data[slice_data.region == 'Infralimbic area']
print(ILA_layers.layer.unique())

ACAd_layers = slice_data[(slice_data.region == 'Anterior cingulate area') & (slice_data.part == ' dorsal part')]
print(ACAd_layers.layer.unique())

ACAv_layers = slice_data[(slice_data.region == 'Anterior cingulate area') & (slice_data.part == ' ventral part')]
print(ACAv_layers.layer.unique())

ORBm_layers = slice_data[(slice_data.region == 'Orbital area') & (slice_data.part == ' medial part')]
print(ORBm_layers.layer.unique())

ORBl_layers = slice_data[(slice_data.region == 'Orbital area') & (slice_data.part == ' lateral part')]
print(ORBl_layers.layer.unique())

ORBvl_layers = slice_data[(slice_data.region == 'Orbital area') & (slice_data.part == ' ventrolateral part')]
print(ORBvl_layers.layer.unique())

AId_layers = slice_data[(slice_data.region == 'Agranular insular area') & (slice_data.part == ' dorsal part')]
print(AId_layers.layer.unique())

AIv_layers = slice_data[(slice_data.region == 'Agranular insular area') & (slice_data.part == ' ventral part')]
print(AIv_layers.layer.unique())

#%%
# Get cells per leyer per PFC subregion for each hemisphere individually and plot it

# Total number of cells in PL layers
PL_l1l=len(PL_layers[(PL_layers.layer == ' layer 1') & (PL_layers.hemisphere == 'left')])
PL_l23l=len(PL_layers[(PL_layers.layer == ' layer 2/3') & (PL_layers.hemisphere == 'left')])
PL_l5l=len(PL_layers[(PL_layers.layer == ' layer 5') & (PL_layers.hemisphere == 'left')])
PL_l6al=len(PL_layers[(PL_layers.layer == ' layer 6a') & (PL_layers.hemisphere == 'left')])
PL_l6bl=len(PL_layers[(PL_layers.layer == ' layer 6b') & (PL_layers.hemisphere == 'left')])

PL_l1r=len(PL_layers[(PL_layers.layer == ' layer 1') & (PL_layers.hemisphere == 'right')])
PL_l23r=len(PL_layers[(PL_layers.layer == ' layer 2/3') & (PL_layers.hemisphere == 'right')])
PL_l5r=len(PL_layers[(PL_layers.layer == ' layer 5') & (PL_layers.hemisphere == 'right')])
PL_l6ar=len(PL_layers[(PL_layers.layer == ' layer 6a') & (PL_layers.hemisphere == 'right')])
PL_l6br=len(PL_layers[(PL_layers.layer == ' layer 6b') & (PL_layers.hemisphere == 'right')])

# Proportion of cells in PL layers 
total_PL_left = PL_l1l + PL_l23l + PL_l5l + PL_l6al + PL_l6bl
total_PL_right = PL_l1r + PL_l23r + PL_l5r + PL_l6ar + PL_l6br

pp_pl_l1l = round((PL_l1l/total_PL_left)*100,1)
pp_pl_l23l = round((PL_l23l/total_PL_left)*100,1)
pp_pl_l5l = round((PL_l5l/total_PL_left)*100,1)
pp_pl_l6al = round((PL_l6al/total_PL_left)*100,1)
pp_pl_l6bl = round((PL_l6bl/total_PL_left)*100,1)

pp_pl_l1r = round((PL_l1r/total_PL_right)*100,1)
pp_pl_l23r = round((PL_l23r/total_PL_right)*100,1)
pp_pl_l5r = round((PL_l5r/total_PL_right)*100,1)
pp_pl_l6ar = round((PL_l6ar/total_PL_right)*100,1)
pp_pl_l6br = round((PL_l6br/total_PL_right)*100,1)


# Plot total number of cells in layers PL
x = np.arange(5)
y_left = [PL_l1l, PL_l23l, PL_l5l, PL_l6al, PL_l6bl]
y_right = [PL_l1r, PL_l23r, PL_l5r, PL_l6ar, PL_l6br]
color_left =  '#237578'
color_right = '#7CC8CB'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Prelimbic area', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 900)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_PL_layers_total.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_PL_layers_total.pdf', transparent=True)

# Plot proportion of cells in layers PL
x = np.arange(5)
y_left = [pp_pl_l1l, pp_pl_l23l, pp_pl_l5l, pp_pl_l6al, pp_pl_l6bl]
y_right = [pp_pl_l1r, pp_pl_l23r, pp_pl_l5r, pp_pl_l6ar, pp_pl_l6br]
color_left =  '#C46336'
color_right = '#EC9871'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Proportion of cells (%)', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Prelimbic area', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 80)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_PL_layers_proportion.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_PL_layers_proportion.pdf', transparent=True)


#%%

# Cells in ILA layers
ILA_l1l=len(ILA_layers[(ILA_layers.layer == ' layer 1') & (ILA_layers.hemisphere == 'left')])
ILA_l23l=len(ILA_layers[(ILA_layers.layer == ' layer 2/3') & (ILA_layers.hemisphere == 'left')])
ILA_l5l=len(ILA_layers[(ILA_layers.layer == ' layer 5') & (ILA_layers.hemisphere == 'left')])
ILA_l6al=len(ILA_layers[(ILA_layers.layer == ' layer 6a') & (ILA_layers.hemisphere == 'left')])
ILA_l6bl=len(ILA_layers[(ILA_layers.layer == ' layer 6b') & (ILA_layers.hemisphere == 'left')])

ILA_l1r=len(ILA_layers[(ILA_layers.layer == ' layer 1') & (ILA_layers.hemisphere == 'right')])
ILA_l23r=len(ILA_layers[(ILA_layers.layer == ' layer 2/3') & (ILA_layers.hemisphere == 'right')])
ILA_l5r=len(ILA_layers[(ILA_layers.layer == ' layer 5') & (ILA_layers.hemisphere == 'right')])
ILA_l6ar=len(ILA_layers[(ILA_layers.layer == ' layer 6a') & (ILA_layers.hemisphere == 'right')])
ILA_l6br=len(ILA_layers[(ILA_layers.layer == ' layer 6b') & (ILA_layers.hemisphere == 'right')])

# Proportion of cells in ILA layers 
total_ILA_left = ILA_l1l + ILA_l23l + ILA_l5l + ILA_l6al + ILA_l6bl
total_ILA_right = ILA_l1r + ILA_l23r + ILA_l5r + ILA_l6ar + ILA_l6br

pp_ila_l1l = round((ILA_l1l/total_ILA_left)*100,1)
pp_ila_l23l = round((ILA_l23l/total_ILA_left)*100,1)
pp_ila_l5l = round((ILA_l5l/total_ILA_left)*100,1)
pp_ila_l6al = round((ILA_l6al/total_ILA_left)*100,1)
pp_ila_l6bl = round((ILA_l6bl/total_ILA_left)*100,1)

pp_ila_l1r = round((ILA_l1r/total_ILA_right)*100,1)
pp_ila_l23r = round((ILA_l23r/total_ILA_right)*100,1)
pp_ila_l5r = round((ILA_l5r/total_ILA_right)*100,1)
pp_ila_l6ar = round((ILA_l6ar/total_ILA_right)*100,1)
pp_ila_l6br = round((ILA_l6br/total_ILA_right)*100,1)

# Plot layers ILA
x = np.arange(5)
y_left = [ILA_l1l, ILA_l23l, ILA_l5l, ILA_l6al, ILA_l6bl]
y_right = [ILA_l1r, ILA_l23r, ILA_l5r, ILA_l6ar, ILA_l6br]
color_left =  '#237578'
color_right = '#7CC8CB'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Infralimbic area', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 400)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ILA_layers_total.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ILA_layers_total.pdf', transparent=True)

# Plot proportion of cells in layers ILA
x = np.arange(5)
y_left = [pp_ila_l1l, pp_ila_l23l, pp_ila_l5l, pp_ila_l6al, pp_ila_l6bl]
y_right = [pp_ila_l1r, pp_ila_l23r, pp_ila_l5r, pp_ila_l6ar, pp_ila_l6br]
color_left =  '#C46336'
color_right = '#EC9871'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Proportion of cells (%)', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Infralimbic area', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 80)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ILA_layers_proportion.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ILA_layers_proportion.pdf', transparent=True)

#%%

# Cells in ACAd layers
ACAd_l1l=len(ACAd_layers[(ACAd_layers.layer == ' layer 1') & (ACAd_layers.hemisphere == 'left')])
ACAd_l23l=len(ACAd_layers[(ACAd_layers.layer == ' layer 2/3') & (ACAd_layers.hemisphere == 'left')])
ACAd_l5l=len(ACAd_layers[(ACAd_layers.layer == ' layer 5') & (ACAd_layers.hemisphere == 'left')])
ACAd_l6al=len(ACAd_layers[(ACAd_layers.layer == ' layer 6a') & (ACAd_layers.hemisphere == 'left')])
ACAd_l6bl=len(ACAd_layers[(ACAd_layers.layer == ' layer 6b') & (ACAd_layers.hemisphere == 'left')])

ACAd_l1r=len(ACAd_layers[(ACAd_layers.layer == ' layer 1') & (ACAd_layers.hemisphere == 'right')])
ACAd_l23r=len(ACAd_layers[(ACAd_layers.layer == ' layer 2/3') & (ACAd_layers.hemisphere == 'right')])
ACAd_l5r=len(ACAd_layers[(ACAd_layers.layer == ' layer 5') & (ACAd_layers.hemisphere == 'right')])
ACAd_l6ar=len(ACAd_layers[(ACAd_layers.layer == ' layer 6a') & (ACAd_layers.hemisphere == 'right')])
ACAd_l6br=len(ACAd_layers[(ACAd_layers.layer == ' layer 6b') & (ACAd_layers.hemisphere == 'right')])

# Proportion of cells in ACAd layers 
total_ACAd_left = ACAd_l1l + ACAd_l23l + ACAd_l5l + ACAd_l6al + ACAd_l6bl
total_ACAd_right = ACAd_l1r + ACAd_l23r + ACAd_l5r + ACAd_l6ar + ACAd_l6br

pp_acad_l1l = round((ACAd_l1l/total_ACAd_left)*100,1)
pp_acad_l23l = round((ACAd_l23l/total_ACAd_left)*100,1)
pp_acad_l5l = round((ACAd_l5l/total_ACAd_left)*100,1)
pp_acad_l6al = round((ACAd_l6al/total_ACAd_left)*100,1)
pp_acad_l6bl = round((ACAd_l6bl/total_ACAd_left)*100,1)

pp_acad_l1r = round((ACAd_l1r/total_ACAd_right)*100,1)
pp_acad_l23r = round((ACAd_l23r/total_ACAd_right)*100,1)
pp_acad_l5r = round((ACAd_l5r/total_ACAd_right)*100,1)
pp_acad_l6ar = round((ACAd_l6ar/total_ACAd_right)*100,1)
pp_acad_l6br = round((ACAd_l6br/total_ACAd_right)*100,1)

# Plot layers ACAd
x = np.arange(5)
y_left = [ACAd_l1l, ACAd_l23l, ACAd_l5l, ACAd_l6al, ACAd_l6bl]
y_right = [ACAd_l1r, ACAd_l23r, ACAd_l5r, ACAd_l6ar, ACAd_l6br]
color_left =  '#237578'
color_right = '#7CC8CB'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Anterior cingulate area - dorsal part', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 400)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ACAd_layers_total.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ACAd_layers_total.pdf', transparent=True)

# Plot proportion of cells in layers ACAd
x = np.arange(5)
y_left = [pp_acad_l1l, pp_acad_l23l, pp_acad_l5l, pp_acad_l6al, pp_acad_l6bl]
y_right = [pp_acad_l1r, pp_acad_l23r, pp_acad_l5r, pp_acad_l6ar, pp_acad_l6br]
color_left =  '#C46336'
color_right = '#EC9871'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Proportion of cells (%)', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Anterior cingulate area - dorsal part', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 80)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ACAd_layers_proportion.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ACAd_layers_proportion.pdf', transparent=True)

#%%

# Cells in ACAv layers
ACAv_l1l=len(ACAv_layers[(ACAv_layers.layer == ' layer 1') & (ACAv_layers.hemisphere == 'left')])
ACAv_l23l=len(ACAv_layers[(ACAv_layers.layer == ' layer 2/3') & (ACAv_layers.hemisphere == 'left')])
ACAv_l5l=len(ACAv_layers[(ACAv_layers.layer == ' layer 5') & (ACAv_layers.hemisphere == 'left')])
ACAv_l6al=len(ACAv_layers[(ACAv_layers.layer == ' layer 6a') & (ACAv_layers.hemisphere == 'left')])
ACAv_l6bl=len(ACAv_layers[(ACAv_layers.layer == ' layer 6b') & (ACAv_layers.hemisphere == 'left')])

ACAv_l1r=len(ACAv_layers[(ACAv_layers.layer == ' layer 1') & (ACAv_layers.hemisphere == 'right')])
ACAv_l23r=len(ACAv_layers[(ACAv_layers.layer == ' layer 2/3') & (ACAv_layers.hemisphere == 'right')])
ACAv_l5r=len(ACAv_layers[(ACAv_layers.layer == ' layer 5') & (ACAv_layers.hemisphere == 'right')])
ACAv_l6ar=len(ACAv_layers[(ACAv_layers.layer == ' layer 6a') & (ACAv_layers.hemisphere == 'right')])
ACAv_l6br=len(ACAv_layers[(ACAv_layers.layer == ' layer 6b') & (ACAv_layers.hemisphere == 'right')])

# Proportion of cells in ACAv layers 
total_ACAv_left = ACAv_l1l + ACAv_l23l + ACAv_l5l + ACAv_l6al + ACAv_l6bl
total_ACAv_right = ACAv_l1r + ACAv_l23r + ACAv_l5r + ACAv_l6ar + ACAv_l6br

pp_acav_l1l = round((ACAv_l1l/total_ACAv_left)*100,1)
pp_acav_l23l = round((ACAv_l23l/total_ACAv_left)*100,1)
pp_acav_l5l = round((ACAv_l5l/total_ACAv_left)*100,1)
pp_acav_l6al = round((ACAv_l6al/total_ACAv_left)*100,1)
pp_acav_l6bl = round((ACAv_l6bl/total_ACAv_left)*100,1)

pp_acav_l1r = round((ACAv_l1r/total_ACAv_right)*100,1)
pp_acav_l23r = round((ACAv_l23r/total_ACAv_right)*100,1)
pp_acav_l5r = round((ACAv_l5r/total_ACAv_right)*100,1)
pp_acav_l6ar = round((ACAv_l6ar/total_ACAv_right)*100,1)
pp_acav_l6br = round((ACAv_l6br/total_ACAv_right)*100,1)

# Plot layers PL
x = np.arange(5)
y_left = [ACAv_l1l, ACAv_l23l, ACAv_l5l, ACAv_l6al, ACAv_l6bl]
y_right = [ACAv_l1r, ACAv_l23r, ACAv_l5r, ACAv_l6ar, ACAv_l6br]
color_left =  '#237578'
color_right = '#7CC8CB'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Anterior cingulate area - ventral part', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 400)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ACAv_layers_total.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ACAv_layers_total.pdf', transparent=True)

# Plot proportion of cells in layers ACAv
x = np.arange(5)
y_left = [pp_acad_l1l, pp_acad_l23l, pp_acad_l5l, pp_acad_l6al, pp_acad_l6bl]
y_right = [pp_acad_l1r, pp_acad_l23r, pp_acad_l5r, pp_acad_l6ar, pp_acad_l6br]
color_left =  '#C46336'
color_right = '#EC9871'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Proportion of cells (%)', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Anterior cingulate area - dorsal part', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 80)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ACAd_layers_proportion.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ACAd_layers_proportion.pdf', transparent=True)

#%%

# Cells in ORBm layers
ORBm_l1l=len(ORBm_layers[(ORBm_layers.layer == ' layer 1') & (ORBm_layers.hemisphere == 'left')])
ORBm_l23l=len(ORBm_layers[(ORBm_layers.layer == ' layer 2/3') & (ORBm_layers.hemisphere == 'left')])
ORBm_l5l=len(ORBm_layers[(ORBm_layers.layer == ' layer 5') & (ORBm_layers.hemisphere == 'left')])
ORBm_l6al=len(ORBm_layers[(ORBm_layers.layer == ' layer 6a') & (ORBm_layers.hemisphere == 'left')])
ORBm_l6bl=len(ORBm_layers[(ORBm_layers.layer == ' layer 6b') & (ORBm_layers.hemisphere == 'left')])

ORBm_l1r=len(ORBm_layers[(ORBm_layers.layer == ' layer 1') & (ORBm_layers.hemisphere == 'right')])
ORBm_l23r=len(ORBm_layers[(ORBm_layers.layer == ' layer 2/3') & (ORBm_layers.hemisphere == 'right')])
ORBm_l5r=len(ORBm_layers[(ORBm_layers.layer == ' layer 5') & (ORBm_layers.hemisphere == 'right')])
ORBm_l6ar=len(ORBm_layers[(ORBm_layers.layer == ' layer 6a') & (ORBm_layers.hemisphere == 'right')])
ORBm_l6br=len(ORBm_layers[(ORBm_layers.layer == ' layer 6b') & (ORBm_layers.hemisphere == 'right')])

# Plot layers PL
x = np.arange(5)
y_left = [ORBm_l1l, ORBm_l23l, ORBm_l5l, ORBm_l6al, ORBm_l6bl]
y_right = [ORBm_l1r, ORBm_l23r, ORBm_l5r, ORBm_l6ar, ORBm_l6br]
color_left =  '#237578'
color_right = '#7CC8CB'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Orbital area - medial part', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 400)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ORBm_layers_total.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ORBm_layers_total.pdf', transparent=True)

#%%

# Cells in ORBl layers
ORBl_l1l=len(ORBl_layers[(ORBl_layers.layer == ' layer 1') & (ORBl_layers.hemisphere == 'left')])
ORBl_l23l=len(ORBl_layers[(ORBl_layers.layer == ' layer 2/3') & (ORBl_layers.hemisphere == 'left')])
ORBl_l5l=len(ORBl_layers[(ORBl_layers.layer == ' layer 5') & (ORBl_layers.hemisphere == 'left')])
ORBl_l6al=len(ORBl_layers[(ORBl_layers.layer == ' layer 6a') & (ORBl_layers.hemisphere == 'left')])
ORBl_l6bl=len(ORBl_layers[(ORBl_layers.layer == ' layer 6b') & (ORBl_layers.hemisphere == 'left')])

ORBl_l1r=len(ORBl_layers[(ORBl_layers.layer == ' layer 1') & (ORBl_layers.hemisphere == 'right')])
ORBl_l23r=len(ORBl_layers[(ORBl_layers.layer == ' layer 2/3') & (ORBl_layers.hemisphere == 'right')])
ORBl_l5r=len(ORBl_layers[(ORBl_layers.layer == ' layer 5') & (ORBl_layers.hemisphere == 'right')])
ORBl_l6ar=len(ORBl_layers[(ORBl_layers.layer == ' layer 6a') & (ORBl_layers.hemisphere == 'right')])
ORBl_l6br=len(ORBl_layers[(ORBl_layers.layer == ' layer 6b') & (ORBl_layers.hemisphere == 'right')])

# Plot layers PL
x = np.arange(5)
y_left = [ORBl_l1l, ORBl_l23l, ORBl_l5l, ORBl_l6al, ORBl_l6bl]
y_right = [ORBl_l1r, ORBl_l23r, ORBl_l5r, ORBl_l6ar, ORBl_l6br]
color_left =  '#237578'
color_right = '#7CC8CB'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Orbital area - lateral part', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 200)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ORBl_layers_total.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ORBl_layers_total.pdf', transparent=True)

#%%

# Cells in ORBvl layers
ORBvl_l1l=len(ORBvl_layers[(ORBvl_layers.layer == ' layer 1') & (ORBvl_layers.hemisphere == 'left')])
ORBvl_l23l=len(ORBvl_layers[(ORBvl_layers.layer == ' layer 2/3') & (ORBvl_layers.hemisphere == 'left')])
ORBvl_l5l=len(ORBvl_layers[(ORBvl_layers.layer == ' layer 5') & (ORBvl_layers.hemisphere == 'left')])
ORBvl_l6al=len(ORBvl_layers[(ORBvl_layers.layer == ' layer 6a') & (ORBvl_layers.hemisphere == 'left')])
ORBvl_l6bl=len(ORBvl_layers[(ORBvl_layers.layer == ' layer 6b') & (ORBvl_layers.hemisphere == 'left')])

ORBvl_l1r=len(ORBvl_layers[(ORBvl_layers.layer == ' layer 1') & (ORBvl_layers.hemisphere == 'right')])
ORBvl_l23r=len(ORBvl_layers[(ORBvl_layers.layer == ' layer 2/3') & (ORBvl_layers.hemisphere == 'right')])
ORBvl_l5r=len(ORBvl_layers[(ORBvl_layers.layer == ' layer 5') & (ORBvl_layers.hemisphere == 'right')])
ORBvl_l6ar=len(ORBvl_layers[(ORBvl_layers.layer == ' layer 6a') & (ORBvl_layers.hemisphere == 'right')])
ORBvl_l6br=len(ORBvl_layers[(ORBvl_layers.layer == ' layer 6b') & (ORBvl_layers.hemisphere == 'right')])

# Plot layers PL
x = np.arange(5)
y_left = [ORBvl_l1l, ORBvl_l23l, ORBvl_l5l, ORBvl_l6al, ORBvl_l6bl]
y_right = [ORBvl_l1r, ORBvl_l23r, ORBvl_l5r, ORBvl_l6ar, ORBvl_l6br]
color_left =  '#237578'
color_right = '#7CC8CB'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Orbital area - ventrolateral part', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 400)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ORBvl_layers_total.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ORBvl_layers_total.pdf', transparent=True)

#%%

# Cells in AId layers
AId_l1l=len(AId_layers[(AId_layers.layer == ' layer 1') & (AId_layers.hemisphere == 'left')])
AId_l23l=len(AId_layers[(AId_layers.layer == ' layer 2/3') & (AId_layers.hemisphere == 'left')])
AId_l5l=len(AId_layers[(AId_layers.layer == ' layer 5') & (AId_layers.hemisphere == 'left')])
AId_l6al=len(AId_layers[(AId_layers.layer == ' layer 6a') & (AId_layers.hemisphere == 'left')])
AId_l6bl=len(AId_layers[(AId_layers.layer == ' layer 6b') & (AId_layers.hemisphere == 'left')])

AId_l1r=len(AId_layers[(AId_layers.layer == ' layer 1') & (AId_layers.hemisphere == 'right')])
AId_l23r=len(AId_layers[(AId_layers.layer == ' layer 2/3') & (AId_layers.hemisphere == 'right')])
AId_l5r=len(AId_layers[(AId_layers.layer == ' layer 5') & (AId_layers.hemisphere == 'right')])
AId_l6ar=len(AId_layers[(AId_layers.layer == ' layer 6a') & (AId_layers.hemisphere == 'right')])
AId_l6br=len(AId_layers[(AId_layers.layer == ' layer 6b') & (AId_layers.hemisphere == 'right')])

# Plot layers PL
x = np.arange(5)
y_left = [AId_l1l, AId_l23l, AId_l5l, AId_l6al, AId_l6bl]
y_right = [AId_l1r, AId_l23r, AId_l5r, AId_l6ar, AId_l6br]
color_left =  '#237578'
color_right = '#7CC8CB'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Agranular insular area - dorsal part', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 300)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_AId_layers_total.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_AId_layers_total.pdf', transparent=True)

#%%

# Cells in AIv layers
AIv_l1l=len(AIv_layers[(AIv_layers.layer == ' layer 1') & (AIv_layers.hemisphere == 'left')])
AIv_l23l=len(AIv_layers[(AIv_layers.layer == ' layer 2/3') & (AIv_layers.hemisphere == 'left')])
AIv_l5l=len(AIv_layers[(AIv_layers.layer == ' layer 5') & (AIv_layers.hemisphere == 'left')])
AIv_l6al=len(AIv_layers[(AIv_layers.layer == ' layer 6a') & (AIv_layers.hemisphere == 'left')])
AIv_l6bl=len(AIv_layers[(AIv_layers.layer == ' layer 6b') & (AIv_layers.hemisphere == 'left')])

AIv_l1r=len(AIv_layers[(AIv_layers.layer == ' layer 1') & (AIv_layers.hemisphere == 'right')])
AIv_l23r=len(AIv_layers[(AIv_layers.layer == ' layer 2/3') & (AIv_layers.hemisphere == 'right')])
AIv_l5r=len(AIv_layers[(AIv_layers.layer == ' layer 5') & (AIv_layers.hemisphere == 'right')])
AIv_l6ar=len(AIv_layers[(AIv_layers.layer == ' layer 6a') & (AIv_layers.hemisphere == 'right')])
AIv_l6br=len(AIv_layers[(AIv_layers.layer == ' layer 6b') & (AIv_layers.hemisphere == 'right')])

# Plot layers PL
x = np.arange(5)
y_left = [AIv_l1l, AIv_l23l, AIv_l5l, AIv_l6al, AIv_l6bl]
y_right = [AIv_l1r, AIv_l23r, AIv_l5r, AIv_l6ar, AIv_l6br]
color_left =  '#237578'
color_right = '#7CC8CB'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Agranular insular area - ventral part', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 100)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_AIv_layers_total.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_AIv_layers_total.pdf', transparent=True)

#%%

# All cells for ACA 

ACA_layers = slice_data[slice_data.region == 'Anterior cingulate area']
print(ACA_layers.layer.unique())

ACA_l1l=len(ACA_layers[(ACA_layers.layer == ' layer 1') & (ACA_layers.hemisphere == 'left')])
ACA_l23l=len(ACA_layers[(ACA_layers.layer == ' layer 2/3') & (ACA_layers.hemisphere == 'left')])
ACA_l5l=len(ACA_layers[(ACA_layers.layer == ' layer 5') & (ACA_layers.hemisphere == 'left')])
ACA_l6al=len(ACA_layers[(ACA_layers.layer == ' layer 6a') & (ACA_layers.hemisphere == 'left')])
ACA_l6bl=len(ACA_layers[(ACA_layers.layer == ' layer 6b') & (ACA_layers.hemisphere == 'left')])

ACA_l1r=len(ACA_layers[(ACA_layers.layer == ' layer 1') & (ACA_layers.hemisphere == 'right')])
ACA_l23r=len(ACA_layers[(ACA_layers.layer == ' layer 2/3') & (ACA_layers.hemisphere == 'right')])
ACA_l5r=len(ACA_layers[(ACA_layers.layer == ' layer 5') & (ACA_layers.hemisphere == 'right')])
ACA_l6ar=len(ACA_layers[(ACA_layers.layer == ' layer 6a') & (ACA_layers.hemisphere == 'right')])
ACA_l6br=len(ACA_layers[(ACA_layers.layer == ' layer 6b') & (ACA_layers.hemisphere == 'right')])

# Plot layers PL
x = np.arange(5)
y_left = [ACA_l1l, ACA_l23l, ACA_l5l, ACA_l6al, ACA_l6bl]
y_right = [ACA_l1r, ACA_l23r, ACA_l5r, ACA_l6ar, ACA_l6br]
color_left =  '#237578'
color_right = '#7CC8CB'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Anterior cingulate area', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 400)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ACA_layers_total.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ACA_layers_total.pdf', transparent=True)

#%%

# All cells for ORB 

ORB_layers = slice_data[slice_data.region == 'Orbital area']
print(ORB_layers.layer.unique())

ORB_l1l=len(ORB_layers[(ORB_layers.layer == ' layer 1') & (ORB_layers.hemisphere == 'left')])
ORB_l23l=len(ORB_layers[(ORB_layers.layer == ' layer 2/3') & (ORB_layers.hemisphere == 'left')])
ORB_l5l=len(ORB_layers[(ORB_layers.layer == ' layer 5') & (ORB_layers.hemisphere == 'left')])
ORB_l6al=len(ORB_layers[(ORB_layers.layer == ' layer 6a') & (ORB_layers.hemisphere == 'left')])
ORB_l6bl=len(ORB_layers[(ORB_layers.layer == ' layer 6b') & (ORB_layers.hemisphere == 'left')])

ORB_l1r=len(ORB_layers[(ORB_layers.layer == ' layer 1') & (ORB_layers.hemisphere == 'right')])
ORB_l23r=len(ORB_layers[(ORB_layers.layer == ' layer 2/3') & (ORB_layers.hemisphere == 'right')])
ORB_l5r=len(ORB_layers[(ORB_layers.layer == ' layer 5') & (ORB_layers.hemisphere == 'right')])
ORB_l6ar=len(ORB_layers[(ORB_layers.layer == ' layer 6a') & (ORB_layers.hemisphere == 'right')])
ORB_l6br=len(ORB_layers[(ORB_layers.layer == ' layer 6b') & (ORB_layers.hemisphere == 'right')])

# Plot layers PL
x = np.arange(5)
y_left = [ORB_l1l, ORB_l23l, ORB_l5l, ORB_l6al, ORB_l6bl]
y_right = [ORB_l1r, ORB_l23r, ORB_l5r, ORB_l6ar, ORB_l6br]
color_left =  '#237578'
color_right = '#7CC8CB'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Orbital area', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 800)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ORB_layers_total.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_ORB_layers_total.pdf', transparent=True)

#%%

# All cells for AI

AI_layers = slice_data[slice_data.region == 'Agranular insular area']
print(AI_layers.layer.unique())

AI_l1l=len(AI_layers[(AI_layers.layer == ' layer 1') & (AI_layers.hemisphere == 'left')])
AI_l23l=len(AI_layers[(AI_layers.layer == ' layer 2/3') & (AI_layers.hemisphere == 'left')])
AI_l5l=len(AI_layers[(AI_layers.layer == ' layer 5') & (AI_layers.hemisphere == 'left')])
AI_l6al=len(AI_layers[(AI_layers.layer == ' layer 6a') & (AI_layers.hemisphere == 'left')])
AI_l6bl=len(AI_layers[(AI_layers.layer == ' layer 6b') & (AI_layers.hemisphere == 'left')])

AI_l1r=len(AI_layers[(AI_layers.layer == ' layer 1') & (AI_layers.hemisphere == 'right')])
AI_l23r=len(AI_layers[(AI_layers.layer == ' layer 2/3') & (AI_layers.hemisphere == 'right')])
AI_l5r=len(AI_layers[(AI_layers.layer == ' layer 5') & (AI_layers.hemisphere == 'right')])
AI_l6ar=len(AI_layers[(AI_layers.layer == ' layer 6a') & (AI_layers.hemisphere == 'right')])
AI_l6br=len(AI_layers[(AI_layers.layer == ' layer 6b') & (AI_layers.hemisphere == 'right')])

# Plot layers PL
x = np.arange(5)
y_left = [AI_l1l, AI_l23l, AI_l5l, AI_l6al, AI_l6bl]
y_right = [AI_l1r, AI_l23r, AI_l5r, AI_l6ar, AI_l6br]
color_left =  '#237578'
color_right = '#7CC8CB'
width = 0.3

fig, ax = plt.subplots(1,1, layout='constrained', figsize=(7,6), dpi= 500)

plt.bar(x-0.3, y_right, width=width, color=color_right) 
plt.bar(x, y_left, width=width, color=color_left) 

ax.set_xticks(x-0.15, ['layer 1', 'layer 2/3', 'layer 5', 'layer 6a', 'layer 6b']) 
ax.legend(['Right Hemisphere', 'Left Hemisphere'], loc='upper left', ncols=1, frameon=False) 
ax.set_ylabel('Total number of cells', labelpad=10, fontsize=10)
ax.bar_label(ax.containers[0], fontsize=8.5, color='#494949', padding=3)
ax.bar_label(ax.containers[1], fontsize=8.5, color='#494949', padding=3)
ax.set_title(f'#{animal_id}  {genotype}  Agranular insular area', fontsize=11, fontweight='bold', x=0.5 , y=1.05)
ax.set_ylim(0, 300)

plt.tight_layout(pad=2)
sns.despine()

#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_AI_layers_total.png', transparent=True)
#plt.savefig('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/Figures/'f'{animal_id}_AI_layers_total.pdf', transparent=True)

#%%

# All layers for all regions side by side












