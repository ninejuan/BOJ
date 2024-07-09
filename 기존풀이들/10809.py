alphabet = "abcdefghijklmnopqrstuvwxyz"
wordS = str(input())
result = ""

for i in range(0, 26, 1):
    if alphabet[i] in wordS:
        result += f"{wordS.index(alphabet[i])} "
    else:
        result += "-1 "
print(result[:-1])
    # print(wordS[i] == alphabet[i])
    # print(alphabet.(i))
    # wordS.find(alphabet.index(i))
    # if wordS[i] not in alphabet:
    #     result.join("-1 ")
