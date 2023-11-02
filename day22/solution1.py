activelist=pl1=[]
pl2=[]
for l in open('input.txt', 'r').readlines():
    if len(l)>1 and not ':' in l:
        activelist.append(int(l))
    if 'Player 2:' in l:
        activelist=pl2

def round():
    if pl1[0]>pl2[0]:
        pl1.append(pl1.pop(0))
        pl1.append(pl2.pop(0))
    else:
        pl2.append(pl2.pop(0))
        pl2.append(pl1.pop(0))

while not (len(pl1)==0 or len(pl2)==0):
    round()
score=0
winninglist=pl1+pl2
for i,c in enumerate(winninglist):
    score+=(len(winninglist)-i)*c
print(score)