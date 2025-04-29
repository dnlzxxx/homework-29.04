from itertools import *
num = 0
for i in product("АКМОСТ", repeat=6):
    a = ''.join(i)
    num += 1
    if "КОСМОС" in a:
        print(num)