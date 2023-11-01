expressions=[l.replace(' ','').strip() for l in open('input.txt', 'r').readlines()]
pos=0

def solve(expr):
    global pos
    res=0
    plus=True
    while pos<len(expr):
        c=expr[pos]
        pos+=1
        match c:
            case ')':
                return res
            case '(':
                if plus:
                    res+=solve(expr)
                else:
                    res*=solve(expr)
            case '+':
                plus=True
            case '*':
                plus=False
            case _:
                if plus:
                    res+=int(c)
                else:
                    res*=int(c)
    return res

tot=0
for expr in expressions:
    tot+=solve(expr)
    pos=0
print(tot)
