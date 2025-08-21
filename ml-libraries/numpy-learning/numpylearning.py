import numpy as np


#-----numpy basics------#
#size, shape, ndim, dtype
#ones, full, zeros, empty, arange, linspace


"""a_mul = np.array([[[1,2,3],
                  [4,5,6],
                  [7,8,9]],
                  [[10, 11, 12],
                   [13, 14, 15],
                   [16, 17, 18]]])

print(a_mul.ndim) 
print(a_mul.shape)
print(a_mul.dtype)"""

""""
#ones, empty, zeros, and full, linspace, arange
a = np.ones((2, 3,3))
print(a)

a = np.zeros((2, 4,2))
print(a)

a = np.empty((2, 3,2))
print(a)

a = np.full((2, 3,3), 9)
print(a)
a= np.arange(0, 250, 5)
print(a)

a = np.linspace(0, 1000, 5)
print(a)"""

"""
#Math operations between np arrays, sin, cos, etc

a1 = np.array([1,1,1,4])
a2 = np.array([3,4,2,1])

print(a1 + a2)
print(a1 * 4)
print(a1 + 5)

"""


"""#appending, inserting,  deleting
a = np.array([[[1, 2, 3],
              [4,5,6],
              [7,8,9]],
              [[10, 11, 12],
               [13, 14, 15],
               [16,17,18]]])

#appending = np.append(a, ([1,1,1]))
#print(appending)

#inserting = np.insert(a, 6, [1,1])
#print(inserting)

#deleting = np.delete(a, 6)
#print(deleting)

#deleting = np.delete(a, 2, 1) #if its a 3D array the scale of the axis goes from 0-2, 1 being row and 2 being column, 0 is for the whole matrix
#print(deleting)"""




""" Concatentating, stacking, and aggregrate functions

a1 = np.array([[1, 2, 3],
              [4,5,6],
              [7,8,9]])
              

a2 = np.array([[10, 11, 12],
               [13, 14, 15],
               [16, 17, 18]])

concat = np.concatenate([a1, a2], axis=1)
print(concat)

hstack = np.hstack((a1, a2))
print(hstack)

vstack = np.vstack((a1, a2))
print(f"{vstack}\n")


print(a1.max())
print(a1.min())
print(np.median(a1))
print(np.cos(a1))
print(a1.std())
"""

"""
reshaping, flattening, and raveling

a = np.full((1, 4,2), 7)
print(a)
a = np.reshape(a, (2,4))
print(a)

a.flatten()
a.ravel()

"""

#numbers = np.random.random(100)

numbers = np.random.randint(100, size=4)
print(numbers)

numbers = np.random.binomial(4, p=0.8, size=(4, 2,2))
print(numbers)

numbers = np.random.choice([2,1,3,4], size=(2,3,3))
print(numbers)











