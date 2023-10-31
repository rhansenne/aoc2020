import re
mem={}
for line in open('input.txt', 'r').readlines():
    if line[0:4]=='mask':
        mask=line.strip()[7:]
    else:
        address=int(re.findall("\[(\d+)\]",line)[0])
        address_bin=format(address, '036b')
        xs=mask.count('X')
        addresses=[[] for x in range(pow(2,xs))]
        variations=[format(x, '0'+str(xs)+'b') for x in range(pow(2,xs))]
        xnum=0
        for pos, b in enumerate(mask):
            x=False
            for apos, a in enumerate(addresses):                
                if b=='0':
                    a.append(address_bin[pos])
                elif b=='1':
                    a.append('1')
                else:
                    a.append(variations[apos][xnum])
                    x=True
            if x:
                xnum+=1
        for a in addresses:
            mem[int('0b'+''.join(a),2)]=int(re.findall("= (\d+)",line)[0])
print(sum(mem.values()))