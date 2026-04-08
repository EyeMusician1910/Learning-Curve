import numpy as np
class Vector:
    # Vector operations
    # Addition, subtraction, scalar multiplication, and unit vector
    def add(self, a, b):
        return np.array(a) + np.array(b)
    def subtract(self, a, b):
        return np.array(a) - np.array(b)
    def scalar_multiply(self, c, v):
        return c * np.array(v)
    def unit_vector(self, v):
        return np.array(v) / np.linalg.norm(v)#Calculates the Euclidean distance(norm) of the vector
    def magnitude(self, v):
        return np.linalg.norm(v)
    def is_independent(self, vectors):
        return np.linalg.matrix_rank(vectors) == len(vectors)#Matrix rank is the maximum number of linearly independent column vectors in the matrix
    def dot_product(self, a, b):#Calculates the dot product of two vectors
        return np.dot(a,b)
#Example Usage
vec=Vector()
v1=[1,2,3]
v2=[4,5,6]
print(vec.add(v1,v2))
print(vec.subtract(v1,v2))
print(vec.scalar_multiply(2,v1))
print(vec.unit_vector(v1))
print(vec.magnitude(v1))
print(vec.is_independent([v1,v2]))
print(vec.dot_product(v1,v2))

#Matrix

class Matrix:
    def add(self, A, B):
        return np.array(A) + np.array(B)
    def subtract(self, A, B):
        return np.array(A) - np.array(B)
    def multiply(self, A, B):
        return np.dot(A,B)#Calculates the dot product of two matrices
    def scalar_multiply(self, c, M):
        return c * np.array(M)
    def transpose(self, M):
        return np.transpose(M)#Calculates the transpose of a matrix
    def determinant(self, M):
        return np.linalg.det(M)#Calculates the determinant of a matrix
    def inverse(self, M):
        return np.linalg.inv(M)#Calculates the inverse of a matrix, if it exists. If the matrix is singular (i.e., it does not have an inverse), this function will raise a LinAlgError.
    def SVD(self, M):
        return np.linalg.svd(M)#Performs Singular Value Decomposition on the matrix M and returns the singular values and the left and right singular vectors.
#Example Usage
mat=Matrix()
M1=[[1,2,3],[4,5,6],[7,8,10]]
M2=[[9,8,7],[6,5,4],[3,2,1]]
print(mat.add(M1,M2))
print(mat.subtract(M1,M2))
print(mat.scalar_multiply(2,M1))
print(mat.transpose(M1))
print(mat.determinant(M1))
print(mat.inverse(M1))
print(mat.SVD(M1))

#Euclidean Distance
def euclidean_distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))#Calculates the Euclidean distance between two points a and b in n-dimensional space. It does this by taking the difference between the two points, converting it to a NumPy array, and then calculating the norm (magnitude) of that difference vector.
#Example Usage
point1=[1,2,3]
point2=[4,5,6]
print(euclidean_distance(point1,point2))

#Covariance
def covariance(X, Y):
    return np.cov(X, Y)[0][1]#Calculates the covariance between two variables X and Y. The np.cov function returns a covariance matrix, and [0][1] accesses the covariance value between X and Y.
#Example Usage
X=[1,2,3]
Y=[4,5,6]
print(covariance(X,Y))

#Probability and Statistics
class Probability:
    def mean(data):
        return np.mean(data)#Calculates the mean (average) of a list of numbers.
    def variance(data):
        return np.var(data)#Calculates the variance of a list of numbers, which measures how much the numbers are spread out from the mean.
    def standard_deviation(data):
        return np.std(data)#Calculates the standard deviation of a list of numbers, which is the square root of the variance and provides a measure of the amount of variation or dispersion in the data.
    def probability(total, favorable):
        return favorable / total#Calculates the probability of an event occurring by dividing the number of favorable outcomes by the total number of possible outcomes.
    def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
        not_a = 1 - p_a
        p_b = p_b_given_a * p_a + p_b_given_not_a * not_a
        p_a_given_b = (p_b_given_a * p_a) / p_b
        return p_a_given_b#Calculates the probability of event A given event B using Bayes' theorem. It takes the prior probability of A (p_a), the likelihood of B given A (p_b_given_a), and the likelihood of B given not A (p_b_given_not_a) to compute the posterior probability p_a_given_b.  
#Example Usage
data=[1,2,3,4,5]
print(Probability.mean(data))
print(Probability.variance(data))
print(Probability.standard_deviation(data))
print(Probability.probability(10, 3))
print(Probability.bayes_theorem(0.2, 0.8, 0.1))