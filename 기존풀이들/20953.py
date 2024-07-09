# 공식 : (a + b) ** 2 * (a + b - 1) / 2

import sys

f_input = sys.stdin.readline
count = int(sys.stdin.readline().rstrip())

res = []
for i in range(0, count):
    id = sys.stdin.readline().rstrip().split()
    a, b = int(id[0]), int(id[1])
    res.append((a+b)**2*(a+b-1)/2)

for i in range(0, len(res)):
    print(int(res[i]))
