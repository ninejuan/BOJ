M = int(input())
cup = ["NULL", 1, 2, 3]
for i in range(0, M): 
    x, y = map(int, input().split())
    cup[x], cup[y] = cup[y], cup[x]

print(cup.index(1))