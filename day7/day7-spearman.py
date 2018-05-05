def get_rank(array):
    rank = dict((x, i+1) for i, x in enumerate(sorted(set(array))))
    return [rank[i] for i in array]
    
n = int(input())
x_data = list(map(float, input().split()))
y_data = list(map(float, input().split()))

rx = get_rank(x_data)
ry = get_rank(y_data)

d = [(rx[i] -ry[i])**2 for i in range(0, n)]
rxy = 1 - (6 * sum(d)) / (n * (n*n - 1))

print(round(rxy, 3))
