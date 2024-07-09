import sys
input = sys.stdin.readline

T = int(input().rstrip())
res = []

for i in range(T):
    a, b = map(int, input().split())
    b = b % 4
    if b % 4 == 0:
        b = 4
    S = a ** b
    if S % 10 == 0:
        res.append(10)
    else:
        res.append(S%10)

for i in res:
    print(i)