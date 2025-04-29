from itertools import *
cnt = 0
for i in permutations("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 4):
    for d in product("0123456789",repeat=2):
        a = ''.join(i)+''.join(d)
        chislo = a[-2] + a[-1]
        if int(chislo) % 7 == 0:
            cnt += 1
print (cnt)