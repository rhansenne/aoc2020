import itertools
numbers=[int(f.strip()) for f in open('input.txt', 'r').readlines()]
for i, n in enumerate(numbers[25:]):
    combinations=list(itertools.combinations(numbers[i:i+25], 2))
    valid=False
    for c in combinations:
        if n==sum(c):
            valid=True
    if not valid:
        break
for i, num in enumerate(numbers):
    for l in range(2,len(numbers)):
        s = sum(numbers[i:i+l])
        if s==n:
            print(min(numbers[i:i+l])+max(numbers[i:i+l]))
        if s>n:
            break