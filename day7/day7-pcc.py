def mean(array):
    if len(array) == 0:
        return 0
    else:
        return sum(array) / len(array)

def stdev(array):
    arr_mean = mean(array)
    sq_dist = 0
    for i in array:
        sq_dist += (i - arr_mean) ** 2
    return (sq_dist / n) ** 0.5

n = int(input())
x_data = list(map(float, input().split()))
y_data = list(map(float, input().split()))

# calculate covariant
sum_var = 0
mean_x = mean(x_data)
mean_y = mean(y_data)
for i in range(0, n):
    sum_var += (x_data[i] - mean_x) * (y_data[i] - mean_y)
covariant = sum_var / n

# calculate PCC
pcc = covariant / (stdev(x_data) * stdev(y_data))
print(round(pcc, 3))
