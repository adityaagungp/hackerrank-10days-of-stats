import math

rows = int(input())
elements = list(map(int, input().split()))
frequencies = list(map(int, input().split()))

# generate the sorted dataset
dataset = []
for i in range(0, rows):
    for j in range(0, frequencies[i]):
        dataset.append(elements[i])
dataset.sort()

# find index of Q1 and Q3
median_idx = int((sum(frequencies) - 1) / 2)
q1_idx = median_idx / 2
q3_idx = (median_idx + sum(frequencies)) / 2

# calculate Q1 and Q3
q1 = (dataset[math.floor(q1_idx)] + dataset[math.ceil(q1_idx)]) / 2
q3 = (dataset[math.floor(q3_idx)] + dataset[math.ceil(q3_idx)]) / 2

print(q3 - q1)