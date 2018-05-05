import math

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

mean = float(input())
k = int(input())

# Poisson distribution
pd = ((mean ** k) * (math.e ** -mean)) / factorial(k)
print(round(pd, 3))
