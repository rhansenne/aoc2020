import re
from itertools import permutations
black=set()
for l in open('input.txt', 'r').readlines():
    co=(0,0,0)
    for direction in re.findall("ne|nw|se|sw|e|w",l):
        match direction:
            case 'ne':
                co=(co[0]+1,co[1]-1,co[2])
            case 'nw':
                co=(co[0],co[1]-1,co[2]+1)
            case 'se':
                co=(co[0],co[1]+1,co[2]-1)
            case 'sw':
                co=(co[0]-1,co[1]+1,co[2])
            case 'e':
                co=(co[0]+1,co[1],co[2]-1)
            case 'w':
                co=(co[0]-1,co[1],co[2]+1)
    if co in black:
        black.remove(co)
    else:
        black.add(co)

def neighbours(co):
    return set(tuple(map(lambda i, j: i + j, co, p)) for p in permutations([-1,0,1], 3))

for i in range(100):
    white=set()
    black_next=black.copy()
    for b in black:
        b_neighbours=neighbours(b)
        white.update(b_neighbours.difference(black))
        b_neighbours_b=b_neighbours.intersection(black)
        if len(b_neighbours_b)==0 or len(b_neighbours_b)>2:
            black_next.remove(b)
    for w in white:
        if len(neighbours(w).intersection(black))==2:
            black_next.add(w)
    black=black_next
print(len(black))        
