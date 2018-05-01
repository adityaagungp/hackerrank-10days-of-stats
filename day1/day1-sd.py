n = int(input())
arr = list(map(int, input().split()))

# calculate mean
mean = sum(arr) / n

# calculate SD
sq_dist = 0
for i in arr:
    sq_dist += (i - mean) ** 2
std = (sq_dist / n) ** 0.5

# round the SD
print(round(std, 1))