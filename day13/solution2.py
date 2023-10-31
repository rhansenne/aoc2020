from sympy.ntheory.modular import crt
schedule = [line.split(',') for line in open('input.txt', 'r').readlines()][1]
ids=[]
mods=[]
for pos, id in enumerate(schedule):
    if id != 'x':
        id=int(id)
        ids.append(id)
        mods.append((id-pos)%id)
print(crt(ids,mods)[0])