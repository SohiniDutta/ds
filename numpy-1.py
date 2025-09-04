import numpy as np

# 1D Array
n1 = np.array([10,20,30,40])
#print(n1)

# 2D Array
n2 = np.array([[10,40],[70,90]])
#print(n2)

#Numpy zero arrays
n4 = np.zeros((4,9))
#print(n4)

#numpy array with same number
n5 = np.full((5,10),9)
#print(n5)

#print a range of numbers
n7 = np.arange(24,50)
n71 = np.arange(24,50,2)
#print(n71)

#print random integers as array
# np.random.randint(from, to, number of integers)
n = np.random.randint(1,100,10)
#print(n)

#shape of array
n9 = np.array([[4,7,9],[5,6,9]])
#print(n9.shape)
n9.shape = (3,2)
#print(n9)

# vstack - vertically stacking 2 arrays
a1 = np.array([10,20,30,40]) 
a2 = np.array([50,60,70,90]) 

#print(np.vstack((a1,a2)))

# hstack - horizontally stacking 2 arrays
a1 = np.array([10,20,30,40]) 
a2 = np.array([50,60,70,90]) 

#print(np.hstack((a1,a2)))

# column_stack - columnwise stacking 2 arrays
a1 = np.array([10,20,30,40]) 
a2 = np.array([50,60,70,90]) 

#print(np.column_stack((a1,a2)))



# Intersect 1d arrays (print the common elements between the two)
arr1 = np.array([10,40,70,90])
arr2 = np.array([70,40,10,100,47,9])

#print(np.intersect1d(arr1,arr2))




# Difference of two 1d arrays (a1 - a2 = a1 leftover elements) (a2 - a1 = a2 leftover elements)
arr1 = np.array([10,40,70,90])
arr2 = np.array([70,40,10,100,47,9])

#print(np.setdiff1d(arr1,arr2))
#print(np.setdiff1d(arr2,arr1))