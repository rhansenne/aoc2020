map = [x.strip() for x in open('input.txt', 'r').readlines()]
trees=col=0
for row in range(1,len(map)):
    col=(col+3)%len(map[0])
    if map[row][col] == '#':
        trees+=1
print(trees)