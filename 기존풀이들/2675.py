T = int(input())
wrdArr = []

for i in range(0, T, 1):
    R, wordS = input().split()
    temp = ""
    for j in range(0, len(wordS), 1):
        temp += wordS[j] * int(R)
    wrdArr.append(temp); temp = ""

for i in range(0, len(wrdArr), 1):
    print(wrdArr[i], end='\n')