import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
#Tossing a coin 10 times and counting the number of heads
x = random.binomial(n=1, p=0.5, size=10)

print(x)
#Visualization of Binomial Distribution
sns.displot(random.binomial(n=10, p=0.5, size=1000))

plt.show()

#Poisson Distribution
x = random.poisson(lam=2, size=10)

print(x)

#Visualization of Poisson Distribution
sns.displot(random.poisson(lam=2, size=1000))

plt.show()

#Uniform Distribution
x = random.uniform(size=(2, 3))

print(x)

#Visualization of Uniform Distribution
sns.displot(random.uniform(size=1000), kind="kde")

plt.show()

#Logistic Distribution
x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x)

#Visualization of Logistic Distribution
sns.displot(random.logistic(size=1000), kind="kde")

plt.show()

#Multinomial Distribution
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)

#Exponential Distribution
x = random.exponential(scale=2, size=(2, 3))

print(x)

#Visualization of Exponential Distribution
sns.displot(random.exponential(size=1000), kind="kde")

plt.show()

#Chi Square Distribution
x = random.chisquare(df=2, size=(2, 3))

print(x)

#Visualization of Chi Square Distribution
sns.displot(random.chisquare(df=1, size=1000), kind="kde")

plt.show()

#Rayleigh Distribution
x = random.rayleigh(scale=2, size=(2, 3))

print(x)

#Visualization of Rayleigh Distribution
sns.displot(random.rayleigh(size=1000), kind="kde")

plt.show()

#Pareto Distribution
x = random.pareto(a=2, size=(2, 3))

print(x)
#Visualization of Pareto Distribution
sns.displot(random.pareto(a=2, size=1000))

plt.show()

#Zipf Distribution
x = random.zipf(a=2, size=(2, 3))

print(x)

#Visualization of Zipf Distribution

x = random.zipf(a=2, size=1000)
sns.displot(x[x<10])

plt.show()