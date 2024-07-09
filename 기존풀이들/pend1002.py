import math

T = int(input())
x1, y1, r1, x2, y2, r2 = map(int, input().split())

dis = math.sqrt((x1-x2)**2+(y1-y2)**2)

if dis == 0 and r1 == r2:
    print(-1)
elif 