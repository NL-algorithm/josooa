import sys

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_until(y, m, d):
    days = d
    for i in range(1, m):
        if i == 2:
            days += 29 if is_leap(y) else 28
        elif i in [1,3,5,7,8,10,12]:
            days += 31
        else:
            days += 30
    for i in range(1, y):
        days += 366 if is_leap(i) else 365
    return days

sy, sm, sd = map(int, sys.stdin.readline().split())
ey, em, ed = map(int, sys.stdin.readline().split())

if (ey - sy > 1000) or (ey - sy == 1000 and (em > sm or (em == sm and ed >= sd))):
    print("gg")
else:
    diff = days_until(ey, em, ed) - days_until(sy, sm, sd)
    print(f"D-{diff}")
