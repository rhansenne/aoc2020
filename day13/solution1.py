import re
schedule = [[int(d) for d in re.findall('(\d+)', line)] for line in open('input.txt', 'r').readlines()]
bus,wait=0,float('inf')
for id in schedule[1]:
    w = id-schedule[0][0]%id
    if w<wait:
        bus,wait=id,w
print(wait*bus)