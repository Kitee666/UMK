# -*- coding: utf-8 -*-
"""Raport_3A_SikorskiDawid_291951.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VSQoWBzu45_Gcs7WuBvEXNkixyqZ0XMU
"""

import matplotlib.pyplot as plt
from adjustText import adjust_text
import numpy as np
import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
import scipy
import statsmodels
from statsmodels.formula.api import ols
from sklearn.neighbors import LocalOutlierFactor

beers = pd.read_csv("https://gist.githubusercontent.com/sikor272/7ba233a7e855f9a3ff8dca841f6591e4/raw/4777e8129b388aed30d14eccf68356a86b175492/beers.csv")

"""**WSZYSKIE PIWA**



"""

beers.plot.scatter(x='alkohol', y='kalorie')
texts = []
for row in np.array(beers):
    texts.append(plt.text(x=row[2], y=row[1], s=row[0]))
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red', lw=0.5))
plt.show()

print('Współczynnik korelacji: ', np.corrcoef(np.array(beers['alkohol']), np.array(beers['kalorie']))[1, 0])

linearBeers = linear_model.LinearRegression()
linearBeers.fit(np.array(beers['alkohol']).reshape(-1, 1), np.array(beers['kalorie']))
print('Kalorie = (', linearBeers.coef_[0], ') * Alkohol + (', linearBeers.intercept_, ')')

minA, maxA = min(beers['alkohol']), max(beers['alkohol'])

beers.plot.scatter(x='alkohol', y='kalorie')
texts = []

for row in np.array(beers):
    texts.append(plt.text(x=row[2], y=row[1], s=row[0]))
plt.plot([minA, maxA],
         [minA * linearBeers.coef_[0] + linearBeers.intercept_, maxA * linearBeers.coef_[0] + linearBeers.intercept_],
         color='blue')
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red', lw=0.5))
plt.show()

beers['reszty'] = [(row[1] - (row[2] * linearBeers.coef_[0] + linearBeers.intercept_)) for row in np.array(beers)]

beers.hist(column='reszty', bins=range(-10, 6, 2))

sm.qqplot(beers['reszty'], line='q')
plt.show()

scipy.stats.shapiro(beers['reszty'])

statsmodels.stats.stattools.durbin_watson(beers['reszty'])

model = ols('kalorie ~ alkohol', data=beers).fit()
print(model.summary())

beers['przewidywana'] = [(row[2] * linearBeers.coef_[0] + linearBeers.intercept_) for row in np.array(beers)]
beers['reszty_sandaryzowane'] = [(row[3] - np.mean(beers['reszty']))/np.std(beers['reszty'])  for row in np.array(beers)]
beers['przewidywana_standaryzowane'] = [(row[4] - np.mean(beers['przewidywana']))/np.std(beers['przewidywana'])  for row in np.array(beers)]
beers.plot.scatter(x='przewidywana_standaryzowane', y='reszty_sandaryzowane')
plt.xlabel("Standaryzowane wartości przewidywane")
plt.ylabel("Standaryzowane reszty")
plt.show()

beers['outlier'] = -(LocalOutlierFactor().fit_predict(np.array(beers['alkohol']).reshape(-1, 1), np.array(beers['kalorie'])))

beers.loc[beers['outlier'] == 1]

"""**PIWA LIGHT**"""

beers['znacznik'] = [1 if row[2] <= 4.3 else 0 for row in np.array(beers)]

light = beers.loc[beers['znacznik'] == 1][['marka', 'kalorie', 'alkohol']]

light.plot.scatter(x='alkohol', y='kalorie')
texts = []
for row in np.array(light):
    texts.append(plt.text(x=row[2], y=row[1], s=row[0]))
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red', lw=0.5))
plt.show()

print('Współczynnik korelacji: ', np.corrcoef(np.array(light['alkohol']), np.array(light['kalorie']))[1, 0])

linearBeersLight = linear_model.LinearRegression()
linearBeersLight.fit(np.array(light['alkohol']).reshape(-1, 1), np.array(light['kalorie']))
print('Kalorie = (', linearBeersLight.coef_[0], ') * Alkohol + (', linearBeersLight.intercept_, ')')

minA, maxA = min(light['alkohol']), max(light['alkohol'])

light.plot.scatter(x='alkohol', y='kalorie')
texts = []

for row in np.array(light):
    texts.append(plt.text(x=row[2], y=row[1], s=row[0]))
plt.plot([minA, maxA],
         [minA * linearBeersLight.coef_[0] + linearBeersLight.intercept_, maxA * linearBeersLight.coef_[0] + linearBeersLight.intercept_],
         color='blue')
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red', lw=0.5))
plt.show()

light['reszty'] = [(row[1] - (row[2] * linearBeersLight.coef_[0] + linearBeersLight.intercept_)) for row in np.array(light)]

light.hist(column='reszty')

sm.qqplot(light['reszty'], line='q')
plt.show()

scipy.stats.shapiro(light['reszty'])

statsmodels.stats.stattools.durbin_watson(light['reszty'])

model = ols('kalorie ~ alkohol', data=light).fit()
print(model.summary())

light['przewidywana'] = [(row[2] * linearBeersLight.coef_[0] + linearBeersLight.intercept_) for row in np.array(light)]
light['reszty_sandaryzowane'] = [(row[3] - np.mean(light['reszty']))/np.std(light['reszty'])  for row in np.array(light)]
light['przewidywana_standaryzowane'] = [(row[4] - np.mean(light['przewidywana']))/np.std(light['przewidywana'])  for row in np.array(light)]
light.plot.scatter(x='przewidywana_standaryzowane', y='reszty_sandaryzowane')
plt.xlabel("Standaryzowane wartości przewidywane")
plt.ylabel("Standaryzowane reszty")
plt.show()

light['outlier'] = -(LocalOutlierFactor().fit_predict(np.array(light['alkohol']).reshape(-1, 1), np.array(light['kalorie'])))

"""**Piwa normalne**"""

normal = beers.loc[beers['znacznik'] == 0][['marka', 'kalorie', 'alkohol']]

normal.plot.scatter(x='alkohol', y='kalorie')
texts = []
for row in np.array(normal):
    texts.append(plt.text(x=row[2], y=row[1], s=row[0]))
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red', lw=0.5))
plt.show()

print('Współczynnik korelacji: ', np.corrcoef(np.array(normal['alkohol']), np.array(normal['kalorie']))[1, 0])

linearBeersNormal = linear_model.LinearRegression()
linearBeersNormal.fit(np.array(normal['alkohol']).reshape(-1, 1), np.array(normal['kalorie']))
print('Kalorie = (', linearBeersNormal.coef_[0], ') * Alkohol + (', linearBeersNormal.intercept_, ')')

minA, maxA = min(normal['alkohol']), max(normal['alkohol'])

normal.plot.scatter(x='alkohol', y='kalorie')
texts = []

for row in np.array(normal):
    texts.append(plt.text(x=row[2], y=row[1], s=row[0]))
plt.plot([minA, maxA],
         [minA * linearBeersNormal.coef_[0] + linearBeersNormal.intercept_, maxA * linearBeersNormal.coef_[0] + linearBeersNormal.intercept_],
         color='blue')
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red', lw=0.5))
plt.show()

normal['reszty'] = [(row[1] - (row[2] * linearBeersNormal.coef_[0] + linearBeersNormal.intercept_)) for row in np.array(normal)]

normal.hist(column='reszty')

sm.qqplot(normal['reszty'], line='q')
plt.show()

scipy.stats.shapiro(normal['reszty'])

statsmodels.stats.stattools.durbin_watson(normal['reszty'])

model = ols('kalorie ~ alkohol', data=normal).fit()
print(model.summary())

normal['przewidywana'] = [(row[2] * linearBeersNormal.coef_[0] + linearBeersNormal.intercept_) for row in np.array(normal)]
normal['reszty_sandaryzowane'] = [(row[3] - np.mean(normal['reszty']))/np.std(normal['reszty'])  for row in np.array(normal)]
normal['przewidywana_standaryzowane'] = [(row[4] - np.mean(normal['przewidywana']))/np.std(normal['przewidywana'])  for row in np.array(normal)]
normal.plot.scatter(x='przewidywana_standaryzowane', y='reszty_sandaryzowane')
plt.xlabel("Standaryzowane wartości przewidywane")
plt.ylabel("Standaryzowane reszty")
plt.show()

normal['outlier'] = -(LocalOutlierFactor().fit_predict(np.array(normal['alkohol']).reshape(-1, 1), np.array(normal['kalorie'])))

normal.loc[normal['outlier'] == 1]

"""**TESTOWANIE**"""

for i in np.arange(2, 6.01, 0.2):
  i = round(i, 1)
  print('Przewidywana kalorycznosc dla piwa', i, '% wynosi:', i * linearBeers.coef_[0] + linearBeers.intercept_, 'kalorii')