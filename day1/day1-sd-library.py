import statistics as st

n = int(input())
data = list(map(int, input().split()))

#calculate the SD
print(round(st.pstdev(data), 1))
