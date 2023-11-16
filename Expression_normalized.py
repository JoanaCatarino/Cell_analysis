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
data = pd.read_csv('C:/Users/JoanaCatarino/OneDrive_KI/OneDrive - Karolinska Institutet/Skrivbordet/Joana/Cfos_analysis/708075/708075_slice_data.csv')
data = data.drop(columns=['Unnamed: 0'])

# Info about the experiment
animal_id = 708075
genotype = 'Rbp4 Cre_neg'
injection = 'left'