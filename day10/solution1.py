diff1=prev=0
diff3=1
for adapter in sorted([int(l) for l in open('input.txt', 'r').readlines()]):
    diff=adapter-prev
    if diff==1:
        diff1+=1 
    elif diff==3:
        diff3+=1 
    prev=adapter
print(diff1*diff3)
