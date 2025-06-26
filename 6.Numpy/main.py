import numpy as np

help(np)
# the basics
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])

print(a)
print(b)

# Get dimensions
print(a.ndim)  # Number of dimensions
print(b.ndim)  # Number of dimensions

# Get shape
print(b.shape)

# Get data type
print(a.dtype)

# Get size
print(a.itemsize)

# Get total size
print(a.nbytes)
print(b.nbytes)

# Accessing / changing / specific elements, rows, columns, etc

c = np.array([[1, 2, 3, 4, 5, 6, 7], [8,9, 10, 11, 12, 13, 14]])

# Get specific element [r, c]
print(c[1, 3])

# Get a specific row
print(c[0, :])

# Get a specific column
print(c[:, 2])

# Getting a little more fancy [startindex,endindex,stepsize]
print(c[0, 1:6:2]) #[2, 4, 6]

# Change something
c[1, 5] = 20
c[:, 2] = [1,2]
print(c)

# 3d exemple
d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

# Get specific element (work outside in) : get 4
print(d[0,1,1])

# Get 2nd element
print(d[:,1,:]) #[[3,4],[7,8]]

# Replace
d[:,1,:] = [[8,8], [9,9]]

# Initialize diffrents types of Arrays

# All 0s matrix
print(np.zeros(5))
print(np.zeros((2,3,3)))

# All 1s matrix
print(np.ones((2,3)))

# Any other numbers
print(np.full((2,2), 9))

# Any other numbers (full like)
print(np.full(a, 4))

# Random decimal
print(np.random.rand(4,2))

# Random int
print(np.random.randint(0, 9,(3,3,3)))

# The identity
np.identity(3)


# Repeat
print(np.repeat([[1,2,3]], 3, axis=0))

output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9

output[1:4, 1:4] = z
print(output)

# Copy array

b = a.copy() # don't do b = a

#Maths

print(a)
print(a+2)
a += 2
print(a)

#Linear algebra
a = np.ones((2,3))
b= np.full((3,2), 2)

print(np.matmul(a,b))

#find the determinant
c = np.identity(3)
print(c)
print(np.linalg.det(c))

print(d[d >5])







