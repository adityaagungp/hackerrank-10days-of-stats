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
    return (sq_dist / len(array)) ** 0.5

# hard-coded inputs
x_data = [95, 85, 80, 70, 60]
y_data = [85, 95, 70, 65, 70]

# calculate covariant
sum_var = 0
mean_x = mean(x_data)
mean_y = mean(y_data)
for i in range(0, 5):
    sum_var += (x_data[i] - mean_x) * (y_data[i] - mean_y)
covariant = sum_var / 5

# calculate a and b so that Y = a + bX
b = covariant / (stdev(x_data) ** 2)
a = mean_y - (b * mean_x)

# expect Y if X = 80
score = a + (b * 80)
print(round(score, 3))
