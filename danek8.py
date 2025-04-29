from itertools import *
cnt = 0
valid_dates = []
for day in product(range(10), repeat = 2):
    a = ''.join(map(str, day))
    if not (1 <= int(a) <= 31):
        continue


    for month in product(range(10), repeat =2):
        b = ''.join(map(str, month))
        if not (1 <= int(b) <= 12):
            continue

        day_valid = int(a)
        month_valid = int(b)

        max_days = 31
        if day_valid in [4, 6, 9, 11]:
            max_days = 30
        elif month_valid == 2:
            max_days = 28

        if day_valid > max_days:
            continue

        for year in product(range(10), repeat = 2):
            c = ''.join(map(str, year))
            d = a+b+c
            if d == d[::-1]:
                cnt += 1
                valid_dates.append(d)

print(sorted(valid_dates))
print(cnt)
print('Ответ: А) следующая дата после 24.04.25 - 03.11.30')
print("Ответ: Б) по счету она 11")

