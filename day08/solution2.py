def execute(instr):
    acc=line=0
    visited=set()
    loop=False
    while True:
        if line in visited:
            loop=True
            break
        if line >= len(instr):
            break
        visited.add(line)
        if instr[line][:3]=='acc':
            acc+=int(instr[line][4:])
        if instr[line][:3]=='jmp':
            line+=int(instr[line][4:])
        else:
            line+=1
    return loop,acc

instructions=[f.strip() for f in open('input.txt', 'r').readlines()]
lastchanged=0
while lastchanged<len(instructions):
    changed_instructions=instructions.copy()
    if instructions[lastchanged][:3]=='nop':
        changed_instructions[lastchanged]='jmp'+instructions[lastchanged][3:]
    elif instructions[lastchanged][:3]=='jmp':
        changed_instructions[lastchanged]='nop'+instructions[lastchanged][3:]
    lastchanged+=1
    loop,acc=execute(changed_instructions)
    if not loop:
        print(acc)
        break