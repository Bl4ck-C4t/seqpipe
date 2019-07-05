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


def DeBruijn(patterns):
    g = nx.MultiDiGraph()
    i = 0
    for read in patterns:
        sub_reads = read.split("|")
        g.add_edge(f'{preffix(sub_reads[0])}|{preffix(sub_reads[1])}', f'{suffix(sub_reads[0])}|{suffix(sub_reads[1])}',
                   val=read)
    return g


if __name__ == '__main__':
    patterns = []
    while True:
        try:
            patterns.append(input())
        except EOFError as e:
            break
    g = DeBruijn(patterns)
    for node in g.adjacency():
        if len(node[1]) > 0:
            print(f'{node[0]} -> {",".join(displayConnections(node[1]))}')
    plt.figure(1)
    nx.draw_networkx(g, with_labels=True, node_color="blue", pos=nx.kamada_kawai_layout(g), font_color="red")
    plt.show()
