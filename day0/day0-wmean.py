# parse input
n = int(input())
arr_data = list(map(int, input().split()))
arr_weight = list(map(int, input().split()))

total = 0
for i in range (0, n):
    total += arr_data[i] * arr_weight[i]

# calculate and round weighted mean
weighted_mean = total/sum(arr_weight)
print(round(weighted_mean, 1))