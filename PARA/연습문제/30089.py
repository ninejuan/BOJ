T = int(input())

for i in range(0, T):
    sentence = input()
    for i in range(len(sentence)):
        if sentence[i:] == sentence[i:][::-1]:
            if i == 0:
                break
            sentence += sentence[i - 1::-1]
            break
    print(sentence)
