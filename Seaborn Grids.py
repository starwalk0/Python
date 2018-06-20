# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 12:46:20 2018

@author: starw_hyrtn4v
"""

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
iris.head()
#%%

tips = sns.load_dataset('tips')

tips.head()

g = sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(plt.scatter,'total_bill','tip')