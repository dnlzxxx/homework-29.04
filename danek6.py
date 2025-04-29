from itertools import *
a = [1, 1, 2, 3, 3, 5, 8, 13]
count = 0
for i in combinations(a, r=4):
    if max(i) < sum(i) - max(i):
        count += 1
print(count)