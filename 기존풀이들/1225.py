import sys
input = sys.stdin.readline

a, b = map(list, input().split())

a = sum(list(map(int, a)))
b = sum(list(map(int, b)))

print(a * b)