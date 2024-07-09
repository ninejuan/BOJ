N = int(input())
word = list(input())

for _ in range(0, N-1):
    f_word = input()
    for i in range(0, len(word)):
        if word[i] == f_word[i]:
            continue
        else:
            word[i] = "?"
print(*word, sep = "")