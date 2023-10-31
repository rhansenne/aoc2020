import re
mem={}
for line in open('input.txt', 'r').readlines():
    if line[0:4]=='mask':
        mask=line.strip()[7:]
    else:
        val=list(format(int(re.findall("= (\d+)",line)[0]), '036b'))
        for pos, b in enumerate(mask):
            if b != 'X':
                val[pos]=mask[pos]
        mem[int(re.findall("\[(\d+)\]",line)[0])]=int('0b'+''.join(val),2)
print(sum(mem.values()))