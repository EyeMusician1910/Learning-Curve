# vNumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function.
To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

Check dimensions of the ndarray:use <array_name>.ndim

Array indexing is the same as accessing an array element.

You can access an array element by referring to its index number.

The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

# Slicing:

Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1

# Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

use astype() to change the data type of an existing array.

The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

The copy SHOULD NOT be affected by the changes.

# Copy vs View

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

# Shape

The shape of an array is the number of elements in each dimension.  

# Reshaping

Reshaping means changing the shape of an array.

# Flattening the arrays

Flattening array means converting a multidimensional array into a 1D array.

We can use reshape(-1) to do this.

# Iterating

Iterating means going through elements one by one.

We can use the for loop.

We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

Enumeration means mentioning sequence number of somethings one by one.

Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.

# Array Joins

We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.

We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.

# Splitting

Splitting breaks one array into multiple.

We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

# Searching

You can search an array for a certain value, and return the indexes that get a match.

To search an array, use the where() method.

There is a method called searchsorted() which performs a binary search in the array

# Sorting

Sorting means putting elements in an ordered sequence.

# Filtering

Getting some elements out of an existing array and creating a new array out of them is called filtering.

In NumPy, you filter an array using a boolean index list.

# Random

Random number does NOT mean a different number every time. Random means something that can not be predicted logically.

NumPy offers the random module to work with random numbers.

randint() for integers, rand() method returns a random float between 0 and 1.

pass values inside rand() to make an array of random floats.

Use random.choice(value) to choose a random element from an array.

Probability Density function: A function that describes a continuous probabiity.
Use choice() and also give values to specify the porbability for each value.

Random Permutations : Use shuffle() & permutation()

The shuffle() method makes changes to the original array.

The permutation() method returns a re-arranged array (and leaves the original array un-changed).

# Displotas
distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.

# Gaussian Distribution:

Use the random.normal() method to get a Normal Data Distribution.

It has three parameters:

loc - (Mean) where the peak of the bell exists.

scale - (Standard Deviation) how flat the graph distribution should be.

size - The shape of the returned array.

