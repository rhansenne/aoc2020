activelist=pl1=[]
pl2=[]
for l in open('input.txt', 'r').readlines():
    if len(l)>1 and not ':' in l:
        activelist.append(int(l))
    if 'Player 2:' in l:
        activelist=pl2

def round(pl1,pl2,prev_decks):
    deck=pl1+[0]+pl2
    if deck in prev_decks:
        return -1
    prev_decks.append(deck)
    
    pl1card=pl1.pop(0)
    pl2card=pl2.pop(0)
    
    if pl1card<=len(pl1) and pl2card<=len(pl2):
        pl1copy=pl1[:pl1card].copy()
        pl2copy=pl2[:pl2card].copy()
        prev_decks_copy=[]
        winner=0
        while winner!=-1 and not (len(pl1copy)==0 or len(pl2copy)==0):
            winner=round(pl1copy,pl2copy,prev_decks_copy)
        winner=1 if winner<2 else 2            
    else:
        winner=1 if pl1card>pl2card else 2
    
    if winner==1:
        pl1.append(pl1card)
        pl1.append(pl2card)
    else:
        pl2.append(pl2card)
        pl2.append(pl1card)
    return winner

prev_decks=[]
winner=0
while winner!=-1 and not (len(pl1)==0 or len(pl2)==0):
    winner=round(pl1,pl2,prev_decks)
    
score=0
winninglist=pl1 if winner<2 else pl2
for i,c in enumerate(winninglist):
    score+=(len(winninglist)-i)*c
print(score)