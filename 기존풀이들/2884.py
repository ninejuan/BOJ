hm = input().split()
hour = int(hm[0])
minute = int(hm[1])

f_hour = hour
f_minute = minute - 45

if f_minute < 0:
    f_minute += 60
    f_hour -= 1

if f_hour < 0:
    f_hour += 24

print(f"{f_hour} {f_minute}")