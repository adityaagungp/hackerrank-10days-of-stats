import math

# use built math.erf
def pdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))

x = int(input())
n = int(input())
mean = float(input())
std = float(input())
new_mean = n * mean
new_std = std * math.sqrt(n)

print(round(pdf(x, new_mean, new_std), 4))
