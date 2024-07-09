N = int(input())

man = []

for i in range(N):
    man.append(input()[0])

s_man = set(man)
res = []

for i in s_man:
    if man.count(i) >= 5:
        res.append(i)

if len(res) > 0:
    print(''.join(sorted(res)))
else:
    print("PREDAJA")