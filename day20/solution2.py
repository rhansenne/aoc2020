import numpy as np
from enum import Enum

class Side(Enum):
    TOP=1
    RIGHT=2
    BOTTOM=3
    LEFT=4

class Orientation(Enum):
    NORMAL=1
    FLIPPED=-1

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

monster=set()
monster_len=monster_height=0
for linenr, l in enumerate(open('monster.txt', 'r').readlines()):
    for pos,char in enumerate(l):
        if char=='#':
            monster.add((linenr,pos))
            if pos>monster_len:
                monster_len=pos
    monster_height=linenr+1
monster_len+=1
    
def match(side, tile):
    flipside=np.flip(side)
    if np.array_equal(side,tile[0]):
        return Side.TOP,Orientation.NORMAL
    elif np.array_equal(flipside,tile[0]):
        return Side.TOP,Orientation.FLIPPED
    elif np.array_equal(side,tile[:,0]):
        return Side.LEFT,Orientation.NORMAL
    elif np.array_equal(flipside,tile[:,0]):
        return Side.LEFT,Orientation.FLIPPED
    elif np.array_equal(side,tile[-1]):
        return Side.BOTTOM,Orientation.NORMAL
    elif np.array_equal(flipside,tile[-1]):
        return Side.BOTTOM,Orientation.FLIPPED
    elif np.array_equal(side,tile[:,-1]):
        return Side.RIGHT,Orientation.NORMAL
    elif np.array_equal(flipside,tile[:,-1]):
        return Side.RIGHT,Orientation.FLIPPED
    return None

def matching_sides(nr,tile):
    matching=[]
    for side in ((tile[0],Side.TOP),(tile[-1],Side.BOTTOM),(tile[:,0],Side.LEFT),(tile[:,-1],Side.RIGHT)):
        for nr2,tile2 in tiles.items():
            if nr!=nr2 and match(side[0],tile2) is not None:
                matching.append(side[1])
    return matching 

def find_right_match(nr,tile):
    for nr2,tile2 in tiles.items():
        if nr != nr2:
            matching_side=match(tile[:,-1],tile2)
            if matching_side is not None:
                while matching_side[0] != Side.LEFT:
                    tile2=np.rot90(tile2, 1)
                    matching_side=match(tile[:,-1],tile2)
                if matching_side[1]==Orientation.FLIPPED:
                    tile2=np.flip(tile2,axis=0)
                return nr2,tile2
    return None

def find_below_match(nr,tile):
    for nr2,tile2 in tiles.items():
        if nr != nr2:
            matching_side=match(tile[-1],tile2)
            if matching_side is not None:
                while matching_side[0] != Side.TOP:
                    tile2=np.rot90(tile2, 1)
                    matching_side=match(tile[-1],tile2)
                if matching_side[1]==Orientation.FLIPPED:
                    tile2=np.flip(tile2,axis=1)
                return nr2,tile2
    return None

def get_image_row(nr,tile):
    image=tile.copy()[1:-1,1:-1]
    right_match = find_right_match(nr,tile)
    while right_match is not None:
        image=np.append(image,right_match[1][1:-1,1:-1], axis=1)
        right_match = find_right_match(right_match[0],right_match[1])
    return image

image=None
# find corner
for nr,tile in tiles.items():
    matching = matching_sides(nr,tile)
    if len(matching)==2:
        #rotate corner if necessary to serve as top left corner
        while matching!=[Side.BOTTOM,Side.RIGHT]:
            tile=np.rot90(tile,1)
            matching = matching_sides(nr,tile)
        while tile is not None:
            #extend with right hand pieces                  
            image_row=get_image_row(nr,tile)
            if image is not None:
                image=np.append(image,image_row, axis=0)
            else:
                image=image_row
            #get first piece of next row
            below_match=find_below_match(nr,tile)
            if below_match is not None:
                nr,tile=below_match[0],below_match[1]
            else:
                tile=None        
        break

#find monsters
def monster_matches(image):
    monstermatches=0
    for x in range(len(image)-monster_height):
        for y in range(len(image[0])-monster_len):
            imagepart = image[x:x+monster_height,y:y+monster_len]
            monstermatch=True
            for (i,j) in monster:
                if imagepart[i][j]!=1:
                    monstermatch=False
                    break
            if monstermatch:
                monstermatches+=1
    return monstermatches

monstermatches=0
for i in range(4):
    match=monster_matches(image)
    if match>0:
        monstermatches=match
    image=np.rot90(image,1)
image=np.flip(image,axis=0)    
for i in range(4):
    match=monster_matches(image)
    if match>0:
        monstermatches=match
    image=np.rot90(image,1)   
print(sum(sum(image))-monstermatches*len(monster))            