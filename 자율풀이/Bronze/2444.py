T = int(input())

for i in range(T):
    print(' ' * ((T - 1) - i), end = '')
    print('*' * (2 * i + 1))
    # print((2 * i + 1))
    
for i in range(T-1, 0, -1):
    print(' ', end="")
    print(' ' * ((T - 1) - i), end = '')
    print('*' * (2 * i - 1))
    # print((2 * i - 1))