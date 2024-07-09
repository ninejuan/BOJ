a, b = input().split()
a, b = int(a), int(b)
if a > b:
    print('>', end='\n')
elif a < b:
    print('<', end='\n')
elif a == b:
    print('==', end='\n')