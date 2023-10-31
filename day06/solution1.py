total=0
answers=set()
for line in open('input.txt', 'r').readlines():
    if line=='\n':
        total+=len(answers)
        answers=set()
    else:
        answers.update([*line.strip()])
total+=len(answers)
print(total)