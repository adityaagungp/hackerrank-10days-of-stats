# Function to calculate median of a sorted array which always return an integer
def median(sorted_array):
    arr_length = len(sorted_array)
    median_idx = int(arr_length / 2)
    if arr_length % 2 == 0:
        return int((sorted_array[median_idx] + sorted_array[median_idx - 1]) / 2)
    else:
        return sorted_array[median_idx]

n = int(input())
array = list(map(int, input().split()))
array.sort()
lower = array[0 : int(len(array)/2)]
upper = array[int((len(array) + 1)/2) :]

# Q1
print(median(lower))

# Q2
print(median(array))

# Q3
print(median(upper))