basic_rules={}
composite_rules={}
messages=[]
for l in open('input.txt', 'r').readlines():
    if l.count('\"') > 0:
        basic_rules[l[:l.index(':')]]=l[l.index(':')+3:-2]
    elif l.count(':') > 0:
        composite_rules[l[:l.index(':')]]=[d.split(' ') for d in l[l.index(':')+2:-1].split(' | ')]
    elif len(l)>1:
        messages.append(l.strip())

def validate(m,rule,pos, depth):
    if rule in basic_rules:
        nextpos=[]
        for p in pos:
            if len(m)>p and basic_rules[rule]==m[p]:
                nextpos.append(p+1)
        return nextpos
    else:
        valid_positions=[]
        for subset in composite_rules[rule]:
            subsetvalid=True
            nextpos=pos.copy()
            for subrule in subset:
                v = validate(m,subrule,nextpos,depth+1)
                if len(v)==0:
                    subsetvalid=False
                    break
                nextpos=v
            if subsetvalid:
                valid_positions+=nextpos
        return valid_positions
    return []

numvalid=0
for m in messages:
    if len(m) in validate(m,'0',[0],0):
        numvalid+=1
print(numvalid)
