import networkx as nx


def preffix(r):
    k = len(r)
    return r[:k - 1]


def suffix(r):
    k = len(r)
    return r[-(k - 1):]


def displayConnections(connections):
    ls = []
    for x in connections.keys():
        for y in range(len(connections[x])):
            ls.append(x)
    return ls


patterns = []
while True:
    try:
        patterns.append(input())
    except EOFError as e:
        break

k = len(patterns[0]) - 1
# nodes = [[suffix(read), preffix(read)] for read in patterns]
nodes = set([x for read in patterns for x in [suffix(read), preffix(read)]])
g = nx.MultiDiGraph()
for read in patterns:
    g.add_edge(preffix(read), suffix(read), val=read)

for node in g.adjacency():
    if len(node[1]) > 0:
        print(f'{node[0]} -> {",".join(displayConnections(node[1]))}')
