import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(array)
print(type(array))
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print(arr.ndim)
arr2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr2d[0, 1])

slice_array = np.array([1, 2, 3, 4, 5, 6, 7])

print(slice_array[1:5])
print(slice_array[4:])
print(slice_array[:4])
print(slice_array[-3:-1])
print(slice_array[1:5:2])

#slicing 2d array
slice_array2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(slice_array2d[1, 1:4])
print(slice_array2d[0:2, 2])

#Giving Datatypes when creating an array

arrData = np.array([1, 2, 3, 4], dtype='S')

print(arrData)
print(arrData.dtype)

#Converting Datatypes on existing arrays

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

#copy

arrCopy = np.array([1, 2, 3, 4, 5])
x = arrCopy.copy()
arrCopy[0] = 42

print(arrCopy)
print(x)

#view
arrView = np.array([1, 2, 3, 4, 5])
x = arrView.view()
arrView[0] = 42

print(arrView)
print(x)

#shape

arrShape = np.array([[1, 2, 3], [4, 5, 6]])
print(arrShape.shape)

#Reshaping
arrReshape = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arrReshape.reshape(4, 3)

print(newarr)

#Unknown dimension
arrUnknown = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arrUnknown.reshape(2, 2, -1)

print(newarr)

#Flattening the arrays
arrFlatten = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arrFlatten.reshape(-1)

print(newarr)

#Iterating arrays

arr1d = np.array([1, 2, 3])

for x in arr1d:
  print(x)

arr2d = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr2d:
  for y in x:
    print(y)

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr3d:
  for y in x:
    for z in y:
      print(z)

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

#Join

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

#Searing arrays

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)

#Sorting arrays

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

#Filtering arrays

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

