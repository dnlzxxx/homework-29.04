from itertools import *
cnt = 0
for i in product('01', repeat=5):
    a = ''.join(i)
    if a[0] != '0' and int(a) % 4 == 0:
        cnt+=1
print(cnt)