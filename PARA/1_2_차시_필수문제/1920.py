import sys
input = sys.stdin.readline
N = int(input())
NL = list(map(int, input().split()))
M = int(input())
ML = list(map(int, input().split()))

for i in ML:
    if i in NL:
        print(1)
    else:
        print(0)