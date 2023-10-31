import re
check=('byr','iyr','eyr','hgt','hcl','ecl','pid')
batch=[]
passport=[]
for line in  open('input.txt', 'r').readlines():
    if len(line)==1:
        batch.append(passport)
        passport=[]
    else:
        passport+=re.findall('([a-z]+):', line)
batch.append(passport)
v=0
for passport in batch:
    valid=True
    for c in check:
        if not c in passport:
            valid=False
    if valid:
        v+=1
print(v)