#Slicing and Attributes in Numpy array>

# Normal Slicing in Numpy array>

# import numpy as np

# arr = np.array([10, 20, 30, 40])
# print(arr[0:1])
# print(arr[0:])
# print(arr[3:])
# print(arr[2:])
# print(arr[:3])
# print(arr[:2])

#Slicing of two arrays

# import numpy as np

# arr = np.array([[10, 20, 30, 40], [50, 60, 70 ,80]])
# print(arr[0:2,0:2])
# print(arr[1, 0:3])
# print(arr[0, 0:2])

#---------------------------------------------------------------------------------------------------------------

#Attributes in Python

import numpy as np

arr = np.array([[10, 20, 30, 40], [50, 60, 70 ,80]])
print(np.shape(arr))
print(np.size(arr))
print(np.ndim(arr))
print(arr.dtype)