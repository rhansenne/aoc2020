def handshake(sn,loopsize):
    v=1
    for i in range(loopsize):
        v=v*sn%20201227
    return v

def loopsize(sn,puk):
    loopsize=1
    v=1
    while True:
        v=v*7%20201227
        if v==puk:
            return loopsize
        loopsize+=1
        
puks=[int(l) for l in open('input.txt', 'r').readlines()]
print(handshake(puks[0],loopsize(7,puks[1])))