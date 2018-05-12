from sklearn import linear_model

def dot_product(X, Y):
    product = 0
    for i in range(0, len(X)):
        product += X[i] * Y[i]
    return product

# Parse input
raw = input().split()
m = int(raw[0])
n = int(raw[1])
raw_set = []
for i in range(0, n):
    raw_set.append(list(map(float, input().split())))
X = []
Y = []
for i in range(0, n):
    X.append(raw_set[i][:m])
    Y.append(raw_set[i][-1])
q = int(input())
query = []
for i in range(0, q):
    query.append(list(map(float, input().split())))

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_
for i in range(0, q):
    print(a + dot_product(b, query[i]))
