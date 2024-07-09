# 첫째 줄부터 8개의 줄에 체스판의 상태가 주어진다. ‘.’은 빈 칸이고, ‘F’는 위에 말이 있는 칸이다.

arr = []
count = 0

for i in range(0, 8):
    arr.append(input())

for i in range(0, 8):
    for j in range(0, 8):
        if i%2 == j%2 and arr[i][j] == 'F':
            count += 1

print(count)