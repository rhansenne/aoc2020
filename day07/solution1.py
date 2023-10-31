import re
import networkx as nx
total=0
G = nx.DiGraph()
for rule in [re.findall('([a-z]+ [a-z]+) bag',line) for line in open('input.txt', 'r').readlines()]:
    for i in range(1,len(rule)):
        G.add_edge(rule[0],rule[i])
for bag in G.nodes():
    if bag!='shiny gold' and nx.has_path(G,bag,'shiny gold'):
        total+=1
print(total)