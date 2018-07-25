# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 14:12:44 2018

@author: starw_hyrtn4v
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%%
df = pd.read_csv('Ecommerce Customers')
df.info()

df.describe()

df.head()

sns.jointplot(df["Time on Website"], df["Yearly Amount Spent"])

#%%

sns.jointplot(df["Time on App"], df["Yearly Amount Spent"])

#%%

sns.jointplot(df["Time on App"], df["Length of Membership"], kind="hex")

#%%

sns.pairplot(df)

#%%
df.corr()

#%%
sns.lmplot("Yearly Amount Spent", "Length of Membership", df)

#%%

df.columns
df.info()

#%%
X = df[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = df['Yearly Amount Spent']

#%%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#%%

from sklearn.linear_model import LinearRegression

lm =LinearRegression()

#%%

lm.fit(X_train, y_train)

#%%

lm.coef_
#%%

predictions = lm.predict(X_test)

#%%
sns.scatterplot(y_test, predictions)
#%%
from sklearn import metrics

print('MAE',metrics.mean_absolute_error(y_test, predictions))
print('MSE',metrics.mean_squared_error(y_test,  predictions))
print('RMSE',np.sqrt(metrics.mean_squared_error(y_test,  predictions)))

#%%

plt.hist(y_test-predictions, bins = 50)

#%%

cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])
cdf
