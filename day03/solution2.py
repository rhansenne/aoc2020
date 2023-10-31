map = [x.strip() for x in  open('input.txt', 'r').readlines()]
total=row=col=0
while row<len(map)-1:
    col=(col+1)%len(map[0])
    row+=2
    if map[row][col] == '#':
        total+=1
for cmb in [(1,1),(3,1),(5,1),(7,1)]:
    trees=col=0
    for row in range(0,len(map)-1):
        col=(col+cmb[0])%len(map[0])
        row=row+cmb[1]
        if row < len(map) and map[row][col] == '#':
            trees+=1
    total*=trees
print(total)