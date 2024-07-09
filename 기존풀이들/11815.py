import sys

N = int(sys.stdin.readline()) # 테스트케이스 개수
X = sys.stdin.readline().split() # 약수 개수를 판별할 수
arr = []

for i in range(0, N, 1):
    temp = 0
    for j in range(1, int(X[i])+1):
        if int(X[i]) % j == 0:
            temp += 1
    if temp % 2 == 0:
        arr.append(0)
    else:
        arr.append(1)
    temp = 0

for i in range(0, len(arr)):
    print(arr[i], end=' ')
# exit()
# count = int(input())
# num = input().split()
# num = list(map(int, num))

# for i in range(count):
#     if i % 5: # 

# print(num)

def get_divisor(n):
    n = int(n)
    divisors = []

    for i in range(1, n + 1):
        if (n % i == 0):            
            divisors.append(i)            

    return divisors

