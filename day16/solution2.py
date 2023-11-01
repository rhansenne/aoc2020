import re
ranges={}
tickets=[]
fields_order={}
yours=False
nearby=False
for line in open('input.txt', 'r').readlines():
    range = re.findall("(\d+)-(\d+)",line)
    if len(range)>0:
        ranges[line[:line.index(':')]]=[(int(range[0][0]),int(range[0][1])),(int(range[1][0]),int(range[1][1]))]
    if nearby:
        tickets.append([int(l) for l in line.split(',')])
    elif yours:
        your_ticket=[int(l) for l in line.split(',')]
        yours=False
    if 'nearby' in line:
        nearby=True    
    if 'your' in line:
        yours=True    
for i, field in enumerate(ranges.keys()):
    fields_order[i]=[f for f in ranges.keys()]
for ticket in tickets:
    ticket_valid=True
    for v in ticket:
        valid=False
        for range in ranges.values():
            if range[0][0]<=v<=range[0][1] or range[1][0]<=v<=range[1][1]:
                valid=True
        if not valid:
            ticket_valid=False
    if ticket_valid:
        for i, v in enumerate(ticket):
            for field in fields_order[i]:
                if not ranges[field][0][0]<=v<=ranges[field][0][1] and not ranges[field][1][0]<=v<=ranges[field][1][1]:
                    fields_order[i].remove(field)
while(True):
    modified=False
    for key,value in fields_order.items():
        if len(value)==1:
            for key2,value2 in fields_order.items():
                if key != key2 and value[0] in value2:
                    value2.remove(value[0])
                    modified=True
    if not modified:
        break
mult=1                        
for key,value in fields_order.items():
    if 'departure' in value[0]:
        mult*=your_ticket[key]
print(mult)