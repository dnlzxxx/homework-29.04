from itertools import *
cnt = 0
letters = ['Р1', 'Е', 'С1', 'У', 'Р2', 'С2']
unique_char = set(permutations(letters))
for char in unique_char:
    nice = True
    for i in range(len(char) -1):
        if (char[i][0] == char[i+1][0]):
            nice = False
            break
    if nice:
        cnt += 1
print(cnt)