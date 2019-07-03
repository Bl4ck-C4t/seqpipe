import networkx as nx
import matplotlib.pyplot as plt

def preffix(r):
    k = len(r)
    return r[:k - 1]


def suffix(r):
    k = len(r)
    return r[-(k - 1):]


def break_down(genome, k):
    return [genome[i:i + k] for i in range(len(genome) - k + 1)]


def displayConnections(connections):
    ls = []
    for x in connections.keys():
        for y in range(len(connections[x])):
            ls.append(x)
    return ls


k = int(input())
genome = input()

edges = break_down(genome, k)

g = nx.MultiDiGraph()
for edge in edges:
    n1 = preffix(edge)
    n2 = suffix(edge)
    g.add_edge(n1, n2, val=edge)

for node in g.adjacency():
    if len(node[1]) > 0:
        print(f'{node[0]} -> {",".join(displayConnections(node[1]))}')

nx.draw_networkx(g, with_labels=True, pos=nx.kamada_kawai_layout(g), font_color="red", node_color="blue")
plt.show()