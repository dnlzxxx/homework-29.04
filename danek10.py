from itertools import *
cnt = 0
#под буквой а
for i in product(range(10), repeat = 6):
    if i[0] + i[1] + i[2] == i[-3] + i[-2] + i[-1] and i.count(6) == 2:
        cnt += 1
print(cnt)
#под буквой б  не понял немного задание. всего билетов меньше ляма, а просят 1 135 246-ой билет