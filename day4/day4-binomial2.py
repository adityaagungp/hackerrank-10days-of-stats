from functools import reduce

def comb(n, r):
    if r == 0 or n == r:
        return 1
    else:
        num = reduce(lambda x,y: x * y, range(r+1, n+1))
        denom = reduce(lambda x,y: x * y, range(1, n-r+1))
        return num // denom

def binomial_func(x, n, p):
    return comb(n, x) * (p ** x) * ((1 - p) ** (n - x))

raw_input = input().split()
p_rejected = float(raw_input[0]) / 100
n = int(raw_input[1])

# No more than 2 pistons rejected
p1 = 0
for i in range(0, 3):
    p1 += binomial_func(i, n, p_rejected)
print(round(p1, 3))

# At least 2 pistons rejected
p2 = 0
for i in range(2, 11):
    p2 += binomial_func(i, n, p_rejected)
print(round(p2, 3))
