import numpy as np
state=[[x.count('#') for x in l.strip()] for l in open('input.txt', 'r').readlines()]
cube = np.zeros((len(state)+14,len(state[0])+14,15), dtype=np.int8)
for x,row in enumerate(state):
    for y,col in enumerate(row):
        cube[7+x][7+y][7]=state[x][y]
for cycle in range(6):
    cube_next=np.copy(cube)
    for x, dim2 in enumerate(cube):
        for y, dim1 in enumerate(dim2):
            for z, val in enumerate(dim1):
                adj_active=np.sum(cube[x-1:x+2,y-1:y+2,z-1:z+2])-val
                if val==1 and not adj_active in (2,3):
                    cube_next[x][y][z]=0
                elif val==0 and adj_active==3:
                    cube_next[x][y][z]=1
    cube=cube_next
print(np.sum(cube))