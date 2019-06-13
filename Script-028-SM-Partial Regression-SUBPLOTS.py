#!/usr/bin/env python
# coding: utf-8
#
from __future__ import print_function
#get_ipython().run_line_magic('matplotlib', 'inline')
import os
import numpy as np
import pandas as pd
import seaborn as sns
from patsy import dmatrices
import statsmodels.api as sm
from matplotlib import pyplot as plt
#
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
df = df.dropna()
sns.set_style('darkgrid')
#
fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2)
# tuple for one row: fig, [ax1, ax2, ax3, ax4] = plt.subplots(nrows=1, ncols=4)
fig.suptitle('Partial regression: slope angle vs sediment thickness', fontsize=12)
#
# subplot 1
ax1.plt = sm.graphics.plot_partregress('sedim_thick', 'slope_angle', ['plate_phill', 'profile'], 
                                       data=df, obs_labels=False, ax=ax1)
ax1.set_title("Philippine Plate", fontsize=10)
ax1.annotate('A', xy=(-0.01, 1.06), xycoords="axes fraction", fontsize=18,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
# subplot 2
ax2.plt = sm.graphics.plot_partregress('sedim_thick', 'slope_angle', ['plate_pacif', 'profile'], 
                                       data=df, obs_labels=False, ax=ax2)
ax2.set_title("Pacific Plate", fontsize=10)
ax2.annotate('B', xy=(-0.01, 1.06), xycoords="axes fraction", fontsize=18,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
# subplot 3
ax3.plt = sm.graphics.plot_partregress('sedim_thick', 'slope_angle', ['plate_maria', 'profile'], 
                                       data=df, obs_labels=False, ax=ax3)
ax3.set_title("Mariana Plate", fontsize=10)
ax3.annotate('C', xy=(-0.01, 1.06), xycoords="axes fraction", fontsize=18,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
# subplot 4
ax4.plt = sm.graphics.plot_partregress('sedim_thick', 'slope_angle', ['plate_carol', 'profile'], 
                                       data=df, obs_labels=False, ax=ax4)
ax4.set_title("Caroline Plate", fontsize=10)
ax4.annotate('D', xy=(-0.01, 1.06), xycoords="axes fraction", fontsize=18,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
plt.tight_layout()
plt.show()
