import networkx as nx


def preffix(r):
    k = len(r)
    return r[:k - 1]


def suffix(r):
    k = len(r)
    return r[-(k - 1):]


def break_down(genome, k):
    return [genome[i:i + k] for i in range(len(genome) - k + 1)]


k = int(input())
genome = input()

edges = break_down(genome, k)

g = nx.DiGraph()
for edge in edges:
    n1 = preffix(edge)
    n2 = suffix(edge)
    g.add_node(n1)
    g.add_node(n2)
    g.add_edge(n1, n2, val=edge)


print(g)
for node in g.adjacency():
    if len(node[1]) > 0:
        print(f'{node[0]} -> {",".join(node[1].keys())}')
