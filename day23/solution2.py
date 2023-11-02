llist={}
cups=[int(x) for x in [*open('input.txt', 'r').readline()]]
lowest=min(cups)
highest=1000000
cups+=[x for x in range(max(cups)+1,highest+1)]
for i in range(0,len(cups)):
    llist[cups[i]]=cups[(i+1)%len(cups)]
current_cup=cups[0]
for r in range(10000000):
    rem1=llist[current_cup]
    rem2=llist[rem1]
    rem3=llist[rem2]
    llist[current_cup]=llist[rem3]
    dest_cup=current_cup
    while dest_cup in (rem1,rem2,rem3,current_cup):
        dest_cup=(dest_cup-1) if dest_cup>lowest else highest
    after_dest=llist[dest_cup]
    llist[dest_cup]=rem1
    llist[rem3]=after_dest
    current_cup=llist[current_cup]
print(llist[1]*llist[llist[1]])    