# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:40:04 2018

@author: starw_hyrtn4v
"""

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
#%%

titanic = sns.load_dataset('titanic')
titanic.head()

#%%
sns.jointplot(x='fare',y='age',data=titanic)

#%%

sns.distplot(titanic['fare'], kde = False, color='red', bins=30)

#%%

sns.boxplot(x='class',y='age',data=titanic, palette='rainbow')

#%%

sns.swarmplot(x='class',y='age',data=titanic, palette='Set2')

#%%

sns.countplot(x='sex',data=titanic)

#%%

sns.heatmap(titanic.corr(),cmap='coolwarm')
plt.title('titanic.corr()')

#%%

g = sns.FacetGrid(titanic, col='sex')
g.map(plt.hist, 'age',)

#%%

g = sns.FacetGrid(titanic, col='sex')
g.map(sns.distplot, 'age',)