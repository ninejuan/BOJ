N = int(input())
count = 0

for i in range(N):
    S = input()
    loopd = []
    previous = S[0]
    flag = 0
    for j in range(len(S)):
        loopd.append(S[j])
        if loopd.count(S[j]) > 1 and previous != S[j]: flag = 1
        previous = S[j]
    if flag == 0: count += 1

print(count)

"""
N = int(input())
count = 0

for i in range(N):
    loopd = []
    previous = 0
    flag = 0
    S = input()
    for j in range(len(S)):
        loopd.append(S[j])
        print(previous, flag, loopd)
        if j == 0: continue
        elif loopd.index(S[j]) != 0 and previous != S[j]: 
            flag = 1
            print("flag plus")
        previous = S[j]
            
    print(f"flag: {flag}")
    if flag == 0: count += 1

print(count)
"""