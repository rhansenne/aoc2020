fullist=[]
ingredients=set()
allergens={}
for l in open('input.txt', 'r').readlines():
    ingr=set(l[:l.index(' (')].split(' '))
    fullist.extend(ingr)
    ingredients.update(ingr)
    for allerg in l[l.index('(contains ')+10:l.index(')')].split(', '):
        if allerg in allergens:
            allergens[allerg]=allergens[allerg].intersection(ingr)
        else:
            allergens[allerg]=ingr
tot=0            
for ingr in ingredients:
    noallerg=True
    for i in allergens.values():
        if ingr in i:
            noallerg=False
    if noallerg:
        tot+=fullist.count(ingr)
print(tot)        