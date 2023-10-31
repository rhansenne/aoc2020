import re
batch=[]
passport={}
for line in  open('input.txt', 'r').readlines():
    if len(line)==1:
        batch.append(passport)
        passport={}
    else:
        for l in line.split(' '):
            pair=l.split(':')
            passport[pair[0]]=pair[1].strip()
batch.append(passport)
v=0
pattern_4digits = re.compile("^\d{4}$")
pattern_hgt = re.compile("^[0-9]+cm|[0-9]+in$")
pattern_hcl = re.compile("^#[0-9,a-f][0-9,a-f][0-9,a-f][0-9,a-f][0-9,a-f][0-9,a-f]$")
pattern_ecl = re.compile("^(amb|blu|brn|gry|grn|hzl|oth)$")
pattern_pid = re.compile("^\d{9}$")
for passport in batch:
    valid=True
    if not 'byr' in passport or not bool(re.match(pattern_4digits, passport['byr'])) or not 1920 <= int(passport['byr']) <= 2002:
        valid=False
    if not 'iyr' in passport or not bool(re.match(pattern_4digits, passport['iyr'])) or not 2010 <= int(passport['iyr']) <= 2020:
        valid=False
    if not 'eyr' in passport or not bool(re.match(pattern_4digits, passport['eyr'])) or not 2020 <= int(passport['eyr']) <= 2030:
        valid=False
    if not 'hgt' in passport or not bool(re.match(pattern_hgt, passport['hgt'])) or not ( (passport['hgt'][3:5]=='cm' and 150 <= int(passport['hgt'][0:3]) <= 193) or (passport['hgt'][2:4]=='in' and 59 <= int(passport['hgt'][0:2]) <= 76)):
        valid=False
    if not 'hcl' in passport or not bool(re.match(pattern_hcl, passport['hcl'])):
        valid=False
    if not 'ecl' in passport or not bool(re.match(pattern_ecl, passport['ecl'])):
        valid=False
    if not 'pid' in passport or not bool(re.match(pattern_pid, passport['pid'])):
        valid=False
    if valid:
        v+=1
print(v)