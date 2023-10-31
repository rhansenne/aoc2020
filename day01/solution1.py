import itertools
for c in itertools.combinations([int(x) for x in  open('input.txt', 'r').readlines()],2):
    if sum(c)==2020:
        print(c[0]*c[1])