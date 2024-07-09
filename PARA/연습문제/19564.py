import sys
wrd = input()
a = "abcdefghijklmnopqrstuvwxyz"

count = 1
for i in range(0, len(wrd)-1):
    if a.index(wrd[i]) < a.index(wrd[i+1]):
        continue
    else:
        count += 1
print(count) 