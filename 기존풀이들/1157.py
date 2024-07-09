word = input().upper()
wlist = list(set(word))
c = []

for i in wlist:
    cnt = word.count(i)
    c.append(cnt)

if c.count(max(c)) > 1:
    print("?")
else:
    print(wlist[c.index(max(c))])