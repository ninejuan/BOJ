K, Q, L, B, N, P = map(int, input().split())
inp = [K, Q, L, B, N, P]
normal = [1, 1, 2, 2, 2, 8]
res = []

for i in range(6):
    res.append(normal[i] - inp[i])

for i in range(6):
    print(res[i], end=" ")