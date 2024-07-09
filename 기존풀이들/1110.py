num = int(input())
f_num = num
count = 0

while True:
    a = f_num // 10
    b = f_num % 10
    c = (a + b) % 10
    f_num = (b * 10) + c
    count += 1

    if (num == f_num):
        break

print(count)