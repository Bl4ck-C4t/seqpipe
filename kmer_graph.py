import networkx as nx
import matplotlib.pyplot as plt


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

g = nx.MultiDiGraph()
i = 0
for read in patterns:
    g.add_edge(preffix(read), suffix(read), val=read)


for node in g.adjacency():
    if len(node[1]) > 0:
        print(f'{node[0]} -> {",".join(displayConnections(node[1]))}')
pos = nx.spring_layout(g)
# nx.draw_networkx_nodes(g, pos, node_color='r', node_size=350)
# nx.draw_networkx_edges(g, pos, width=1.0, alpha=0.5)
# nx.draw_networkx_labels(g, pos, labels, font_size=10)
plt.figure(1)
nx.draw_networkx(g, with_labels=True, pos=nx.kamada_kawai_layout(g), font_color="red")
# plt.figure(2)
# nx.draw_networkx(g, with_labels=True, pos=nx.circular_layout(g), font_color="red")
# plt.figure(3)
# nx.draw_networkx(g, with_labels=True, pos=nx.spring_layout(g), font_color="red")
# plt.figure(4)
# nx.draw_networkx(g, with_labels=True, pos=nx.fruchterman_reingold_layout(g), font_color="red")
plt.show()
