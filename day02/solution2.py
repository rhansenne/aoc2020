valid=0
for pw in [(int(x[0:x.index('-')]),int(x[x.index('-')+1:x.index(' ')]),x[x.index(' ')+1],x[x.index(':')+1:].strip()) for x in  open('input.txt', 'r').readlines()]:
    if (pw[3][pw[0]-1]==pw[2]) != (pw[3][pw[1]-1]==pw[2]):
        valid+=1
print(valid)