instructions=[f.strip() for f in open('input.txt', 'r').readlines()]
acc=line=0
visited=set()
while True:
    if line in visited:
        break
    visited.add(line)
    if instructions[line][:3]=='acc':
        acc+=int(instructions[line][4:])
    if instructions[line][:3]=='jmp':
        line+=int(instructions[line][4:])
    else:
        line+=1
print(acc)