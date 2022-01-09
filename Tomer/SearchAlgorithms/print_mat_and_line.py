import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

matrix_size = 11
a = np.eye(matrix_size)
x = np.array([1, 9])
y = np.array([4, 8])

sns.heatmap(a, cbar=False, cmap='Oranges')
sns.lineplot(x=x, y=y)
plt.show()
