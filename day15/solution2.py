starting_numbers = open('input.txt', 'r').readlines()[0].split(',')
last_spoken={}
for t, n in enumerate(starting_numbers):
    last_spoken[int(n)]=[t,-1]
    last=int(n)
for turn in range(len(starting_numbers), 30000000):
    if last_spoken[last][1]==-1:
        last=0
        if 0 in last_spoken:
            last_spoken[0][1]=last_spoken[0][0]
            last_spoken[0][0]=turn
        else:
            last_spoken[0]=[turn,-1]
    else:
        last=last_spoken[last][0]-last_spoken[last][1]
        if last in last_spoken:
            last_spoken[last][1]=last_spoken[last][0]
            last_spoken[last][0]=turn
        else:
            last_spoken[last]=[turn,-1]
print(last)