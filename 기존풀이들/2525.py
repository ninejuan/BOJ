hm = input().split()
hour = int(hm[0])
minute = int(hm[1])
C = int(input())

f_min = minute + C
f_hour = hour
while f_min > 59:
    if f_min > 59:
        f_hour += 1
        f_min -= 60

if f_hour >= 24:
    f_hour -= 24

print(f"{f_hour} {f_min}")