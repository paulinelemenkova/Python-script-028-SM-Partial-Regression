#!/usr/bin/env python
# coding: utf-8

# In[29]:


from __future__ import print_function
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import statsmodels.api as sm
from patsy import dmatrices
import os
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
df = df.dropna()
sns.set_style('darkgrid')

sm.graphics.plot_partregress('sedim_thick', 'slope_angle', ['plate_pacif', 'profile'], data=df, 
                             obs_labels=False)
plt.title("Partial regression of slope angle vs sediment thickness: \n Pacific Plate, 25 bathymetric profiles")
plt.annotate('B', xy=(-0.01, 1.06), xycoords="axes fraction", fontsize=18,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
plt.show()

