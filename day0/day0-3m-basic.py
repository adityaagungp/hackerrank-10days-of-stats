#input
n = int(input())
raws = input()
arr = list(map(int, raws.split()))

#find mean
print(float(sum(arr)) / len(arr))

#find median
sorted_arr = sorted(arr)
arr_length = len(arr)
median_idx = int(arr_length / 2)
median = 0
if arr_length % 2 == 0:
	median = float(sorted_arr[median_idx] + sorted_arr[median_idx - 1]) / 2
else:
	median = sorted_arr[median_idx]
print(median)

#find mode
mode = sorted_arr[0]
mode_occur = 0
temp_occur = 1
for i in range(1, len(sorted_arr)):
    if sorted_arr[i] == sorted_arr[i-1]:
        temp_occur += 1
    else:
        if temp_occur > mode_occur:
            mode = sorted_arr[i-1]
            mode_occur = temp_occur
        temp_occur = 1
if temp_occur > mode_occur:
    mode = sorted_arr[-1]
    mode_occur = temp_occur
print(mode)