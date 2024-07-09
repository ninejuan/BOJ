import math

T = int(input())

for _ in range(0, T):
    n, m = map(int, input().split())
    print(math.factorial(m) // (math.factorial(n) * math.factorial(m-n)))
