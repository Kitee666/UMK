
#
# Raport 1A
# Dawid Sikorski 291951
#
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Zadanie 1
cereals = pd.read_csv("cereals.CSV")

# Zadanie 2
cereals.groupby(['Manuf', 'Shelf']) \
    .size().unstack() \
    .plot(kind='bar', stacked=True)
plt.show()

cereals.groupby(['Manuf', 'Shelf']) \
    .size().groupby(level=0).apply(
    lambda x: 100 * x / x.sum()
).unstack().plot(kind='bar', stacked=True)
plt.show()

# Zadanie 3
sns.heatmap(cereals.groupby(['Manuf', 'Shelf']) \
            .size().groupby(level=0).apply(
    lambda x: 100 * x / x.sum()
).unstack().fillna(0).T, annot=True)
plt.show()

# Zadanie 4
cereals['Potass_norm'] = (cereals['Potass'] - np.nanmean(cereals['Potass'])) / np.nanstd(cereals['Potass'])
cereals['Potass_outlier'] = abs(cereals['Potass_norm']) > 3
print(cereals.query('Potass_outlier | Potass.isnull()', engine='python'))

# Zadanie 5
sns.histplot(cereals, x='Potass', hue='Shelf', stat='count', multiple='stack')
plt.show()

sns.histplot(cereals, x='Potass', hue='Shelf', stat='count', multiple='fill')
plt.show()

# Zadanie 6
cereals['Calories_binned'] = pd.cut(cereals['Calories'],
                                    bins=[0, 80.99, 109.99, max(cereals['Calories'])],
                                    labels=['Mniej niz 90',
                                            'Pomiedzy 90 a 110',
                                            'Conajmniej 110'])

cereals.groupby(['Calories_binned', 'Shelf']) \
    .size().unstack().plot(kind='bar', stacked=True)
plt.show()
cereals.groupby(['Calories_binned', 'Shelf']) \
    .size().groupby(level=0).apply(
    lambda x: 100 * x / x.sum()
).unstack().plot(kind='bar', stacked=True)
plt.show()
