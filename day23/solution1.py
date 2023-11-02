cups=[int(x) for x in [*open('input.txt', 'r').readline()]]
lowest=min(cups)
highest=max(cups)
current_cup=cups[0]
for r in range(100):
    removed=[]
    for i in range(1,4):
        next_idx=(cups.index(current_cup)+1)%len(cups)
        removed.append(cups[next_idx])
        cups.remove(removed[-1])
    dest_cup=current_cup
    while dest_cup in removed or dest_cup == current_cup:
        dest_cup=(dest_cup-1) if dest_cup>lowest else highest
    cups=cups[:cups.index(dest_cup)+1]+removed+cups[cups.index(dest_cup)+1:]
    current_cup=cups[(cups.index(current_cup)+1)%len(cups)]
result=cups[cups.index(1)+1:]+cups[:cups.index(1)]
print(str(result).strip('[]').replace(', ',''))