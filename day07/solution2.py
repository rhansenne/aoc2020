import re
total=0
rules={}
for line in open('input.txt', 'r').readlines():
    rules[re.match('^([a-z]+ [a-z]+) bag',line).group(1)]=re.findall('(\d [a-z]+ [a-z]+) bag',line)

def count(node,quant):
    global total
    total+=quant
    for subbag in rules[node]:
        count(subbag[2:],quant*int(subbag[:1]))
    
count('shiny gold',1)
print(total-1)