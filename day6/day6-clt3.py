import math

# hard-coded inputs
z = 1.96
std = 80
n = 100
mean = 500

# calculate A and B
margin_error = z * std / math.sqrt(n)
a = mean - margin_error
b = mean + margin_error
print(round(a, 2))
print(round(b, 2))
