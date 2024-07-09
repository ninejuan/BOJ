import sys

n, m = map(int, sys.stdin.readline().split()) # type: ignore
pm_l = dict()
pm_n = dict()

for i in range(1, n+1):
    _in = sys.stdin.readline().strip() # type: ignore
    pm_l[i] = _in
    pm_n[_in] = i

for i in range(m):
    get = sys.stdin.readline().strip() # type: ignore
    if get[0].isdigit():
        print(pm_l[int(get)])
    else:
        print(pm_n[get])