import numpy as np
from scipy import stats

# input
n = int(input())
string = raw_input()
arr = list(map(int, string.split()))
np_array = np.array(arr)

# mean from numpy array
print(np.mean(np_array))

# median from numpy array
print(np.median(np_array))

# mode
print(stats.mode(np_array)[0][0])