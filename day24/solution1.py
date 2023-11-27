import re
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
print(len(black))        