N = int(input())
bj = 1
count = 1

while N > bj:
    bj += 6 * count
    count += 1
print(count)