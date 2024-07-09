N = int(input())
F = int(input())
n_len = len(str(N))
N = N - (int(str(N)[n_len-2]) * 10 + int(str(N)[n_len-1]))

while True:
    if N % F == 0:
        break
    N += 1

print(str(N)[n_len-2] + str(N)[n_len-1])