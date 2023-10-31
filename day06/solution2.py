total=0
answers=set()
nextSet=True
for line in open('input.txt', 'r').readlines():
    if line=='\n':
        total+=len(answers)
        answers.clear()
        nextSet=True
    elif nextSet:
        answers.update([*line.strip()])
        nextSet=False
    else:
        answers = answers.intersection(set([*line.strip()]))
total+=len(answers)
print(total)