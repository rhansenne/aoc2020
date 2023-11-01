import functools 
expressions=[l.replace(' ','').strip() for l in open('input.txt', 'r').readlines()]
pos=0

def solve(expr):
    global pos
    plus=True
    mults=[0]
    while pos<len(expr):
        c=expr[pos]
        pos+=1
        match c:
            case ')':
                return functools.reduce(lambda a, b: a*b, mults)
            case '(':
                if plus:
                    mults[-1]+=solve(expr)
                else:
                    mults.append(solve(expr))
            case '+':
                plus=True
            case '*':
                plus=False
            case _:
                if plus:
                    mults[-1]+=int(c)
                else:
                    mults.append(int(c))
    return functools.reduce(lambda a, b: a*b, mults)

tot=0
for expr in expressions:
    tot+=solve(expr)
    pos=0
print(tot)
