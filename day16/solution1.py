import re
ranges=[]
tickets=[]
nearby=False
for line in open('input.txt', 'r').readlines():
    range = re.findall("(\d+)-(\d+)",line)
    if len(range)>0:
        ranges.append([(int(range[0][0]),int(range[0][1])),(int(range[1][0]),int(range[1][1]))])
    if nearby:
        tickets+=[int(l) for l in line.split(',')]
    if 'nearby' in line:
        nearby=True
error_rate=0
for v in tickets:
    valid=False
    for range in ranges:
        if range[0][0]<=v<=range[0][1] or range[1][0]<=v<=range[1][1]:
            valid=True
    if not valid:
        error_rate+=v
print(error_rate)