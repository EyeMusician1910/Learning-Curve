import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.randint(100)

print(x)

x=random.randint(100, size=(5))

print(x)

x = random.choice([3, 5, 7, 9])

print(x)

#with a given probability
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)
#with a given probability and size of a 2d array
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)

#Shuffle
#The shuffle() method makes changes to the original array.
arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)
#The permutation() method returns a re-arranged array (and leaves the original array un-changed).
arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))
#displots
sns.displot([0, 1, 2, 3, 4, 5])

plt.show()
#With a kernel density estimate (KDE)
sns.displot([0, 1, 2, 3, 4, 5], kind="kde")

plt.show()

#Gaussian distribution

x = random.normal(size=(2, 3))

print(x)

#with a mean of 1 and a standard deviation of 2
x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)