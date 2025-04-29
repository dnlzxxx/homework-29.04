from itertools import *
a = [-2, -1, 1, 2]
count = 0
for i in product(a, repeat=4):
    if sum(i) == 5:
        count += 1
print(count)