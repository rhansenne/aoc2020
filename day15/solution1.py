starting_numbers = open('input.txt', 'r').readlines()[0].split(',')
last_spoken={}
for t, n in enumerate(starting_numbers):
    last_spoken[int(n)]=[t]
    last=int(n)
for turn in range(len(starting_numbers), 2020):
    if len(last_spoken[last])==1:
        last=0
        if 0 in last_spoken:
            last_spoken[0].append(turn)
        else:
            last_spoken[0]=[turn]
    else:
        last=last_spoken[last][-1]-last_spoken[last][-2]
        if last in last_spoken:
            last_spoken[last].append(turn)
        else:
            last_spoken[last]=[turn]
print(last)