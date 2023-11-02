ingredients=set()
allergens={}
for l in open('input.txt', 'r').readlines():
    ingr=set(l[:l.index(' (')].split(' '))
    ingredients.update(ingr)
    for allerg in l[l.index('(contains ')+10:l.index(')')].split(', '):
        if allerg in allergens:
            allergens[allerg]=allergens[allerg].intersection(ingr)
        else:
            allergens[allerg]=ingr
identified=set()
for ingr in ingredients:
    noallerg=True
    for i in allergens.values():
        if ingr in i:
            noallerg=False
    if noallerg:
        identified.add(ingr)
allidentified=False        
while not allidentified:
    allidentified=True
    next_identified=set()
    for r in identified:
        for i in allergens.values():
            if len(i)>1 and r in i:
                i.remove(r)
            if len(i)==1:
                next_identified.update(i)
            else:
                allidentified=False
    identified=next_identified
ingr_list=[]
for a in sorted(list(allergens.keys())):
    ingr_list.extend(allergens[a])
print(','.join(ingr_list))