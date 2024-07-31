import numpy as np

height = [10, 9, 8, 11, 5]
weight = [56, 60, 78, 47, 90]

np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)
print(np_weight)
bmi = np_weight/np_height **2
print(bmi)
print (bmi>0.5)
print([bmi>0.5])