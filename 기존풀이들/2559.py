data = input().split()
N, K = int(data[0]), int(data[1])

tems = []

tem = input().split()
for i in range(0, len(tem)):
    tems.append(int(tem[i]))

res = window = sum(tems[:K])

for i in range(K, len(tems)):
    window += tems[i]- tems[i - K]
    res = max(res, window)

print(res)