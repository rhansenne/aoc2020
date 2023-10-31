from functools import lru_cache
adapters=[int(l) for l in open('input.txt', 'r').readlines()]
adapters.sort(reverse=True)
adapters=[adapters[0]+3]+adapters+[0]
connections={}
for i, adapter in enumerate(adapters):
    outputs=[]
    for j in range(1,4):
        if (i+j)<len(adapters) and (adapter-adapters[i+j])<=3:
            outputs.append(adapters[i+j])
    connections[adapter]=outputs

@lru_cache
def count(input):
    if len(connections[input])==0:
        return 1
    else:
        c=0
        for output in connections[input]:
            c+=count(output)
        return c
    
print(count(adapters[0]))