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

ratios = input().split()
ratio_boy = float(ratios[0])
ratio_girl = float(ratios[1])
p_boy = ratio_boy / (ratio_boy + ratio_girl)
num_children = 6
min_boys = 3
probability = 0
for i in range(min_boys, num_children + 1):
    probability += binomial_func(i, num_children, p_boy)

print(round(probability, 3))
