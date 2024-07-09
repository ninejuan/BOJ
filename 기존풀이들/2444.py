length = int(input())

for i in range(0, length):
    for j in range(0, length-i):
        print(' ', end='')
    print('*')