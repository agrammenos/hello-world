import random
import argparse

n = argparse.ArgumentParser()
n.add_argument("n")
n = n.parse_args()
n = int(n.n)

numbers = []
set1 = []
set2 = []
lexiko = {}
n1 = int(n * (n - 1) / 6)
for i in range(1, n + 1):
    numbers.append(i)
    lexiko[i] = 0
while True:
    if n1 == 0: break
    k = 1
    while k == 1:
        x = random.choice(numbers)
        if(lexiko[x] < (n-1)/2): k = 0
    while k == 0:
        y = random.choice(numbers)
        z = random.choice(numbers)
        if(x == y or y==z or z==x): continue
        for i in range(len(set1)):
            if(x in set1[i] and (y in set1[i] or z in set1[i])): break
        else: k = 1
    for i in range(len(set1)):
        if(y in set1[i] and z in set1[i]):
            lexiko[set1[i][0]] -= 1
            lexiko[set1[i][1]] -= 1
            lexiko[set1[i][2]] -= 1
            set1.remove(set1[i])
            n1 += 1
            break
    else:
        set1.append([x,y,z])
        lexiko[x] += 1
        lexiko[y] += 1
        lexiko[z] += 1
        n1 -= 1
for i in set1:
    m = tuple(sorted(i))
    set2.append(m)
print(sorted(set2))
print(len(set1))
