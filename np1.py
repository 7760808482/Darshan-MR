'''You are given a list of integers arr. Convert it into a NumPy ndarray and find the indices of all elements equal to 5 using np.where().'''

import numpy as np
arr=[5,1,5,3,5,7,9]
x=np.array(arr)
print(type(x))
y=np.where(x==5)
print(y)


'''You are given a list of integers. Convert it into ndarray and find all indices where the value is greater than 10.'''
import numpy as np
arr=[4,12,7,15,3,20,1]
x=np.array(arr)
print(x)
y=np.where(x>10)
print(y)

#Convert the list into ndarray and find indices of even numbers.
import numpy as np
arr=[2,5,8,11,14,7,6]
x=np.array(arr)
print(x)
y=np.where(x%2==0)
print(y)


#Convert the list into ndarray and find indices of numbers less than 0.
import numpy as np
arr=[3,-1,4,-5,6,-1]
x=np.array(arr)
print(x)
y=np.where(x<0)
print(y)


#Convert the list into ndarray and find indices where elements are between 5 and 15 (inclusive).
import numpy as np
arr=[2,6,10,15,18,5,1]
x=np.array(arr)
print(x)
y=np.where((x>=5)&(x<=15))
print(y)



'''Find indices of numbers that are:
divisible by 3
AND greater than 10'''
import numpy as np
arr=[3,6,9,12,15,18,2,5]
arr_np=np.array(arr)
indices=np.where((arr_np%3==0)&(arr_np>10))
print(arr_np)
print(indices)