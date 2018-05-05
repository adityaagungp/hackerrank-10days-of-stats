raw = input().split()
a = float(raw[0])
b = float(raw[1])

# E[X] = lambda + lambda ** 2
c_a = 160 + 40 * (a + a ** 2)
c_b = 128 + 40 * (b + b ** 2)

print(round(c_a, 3))
print(round(c_b, 3))
