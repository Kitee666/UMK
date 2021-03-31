
#
#    Dawid Sikorski 291951
#

import numpy as np
import matplotlib.pyplot as plt

data_set = np.loadtxt(fname='kmeans.txt')
points = np.array([[i, 0] for i in data_set], dtype=object)
groups = np.array([[i, j] for i, j in zip(data_set[np.random.choice(data_set.shape[0], 3, replace=False)], [0, 1, 2])], dtype=object)

check = True
while check:
    check = False
    for point in points:
        distance = [np.sqrt(np.sum(np.square(group[0] - point[0]))) for group in groups]
        if point[1] != np.argmin(distance):
            point[1] = np.argmin(distance)
            check = True
    for g in groups:
        g[0] = np.mean(points[np.where(points[:, 1] == g[1])][:, 0])

colors = ['orange', 'cyan', 'magenta']
for g, color in zip(groups, colors):
    point = np.stack(points[np.where(points[:, 1] == g[1])][:, 0])
    plt.scatter(point[:, 0], point[:, 1], c=color)
plt.show()
