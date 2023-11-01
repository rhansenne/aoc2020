import numpy as np
tiles={}
nr=0
for l in open('input.txt', 'r').readlines():
    if l[0]=='T':
        nr=int(l[5:-2])
        tiles[nr]=[]
    elif len(l)>1:
        tiles[nr].append([x.count('#') for x in l.strip()])
for nr,tile in tiles.items():
    tiles[nr]=np.array(tiles[nr])

def match(side):
    flipside=np.flip(side)
    occ=0
    for nr,tile in tiles.items():
        if np.array_equal(side,tile[0]) or np.array_equal(flipside,tile[0]) \
        or np.array_equal(side,tile[-1]) or np.array_equal(flipside,tile[-1]) \
        or np.array_equal(side,tile[:,0]) or np.array_equal(flipside,tile[:,0]) \
        or np.array_equal(side,tile[:,-1]) or np.array_equal(flipside,tile[:,-1]):
            occ+=1
    return occ>1

prod=1
for nr,tile in tiles.items():
    matchingsides=0
    if match(tile[0]):
        matchingsides+=1
    if match(tile[-1]):
        matchingsides+=1
    if match(tile[:,0]):
        matchingsides+=1
    if match(tile[:,-1]):
        matchingsides+=1
    if matchingsides==2:
        prod*=nr
print(prod)

    