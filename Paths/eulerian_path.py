import networkx as nx
from Paths import eulerian_cycle as ec


# nx.eulerize(g)
# ls = list(nx.eulerian_circuit(g))
# path = ls[0][0] + "->" + ls[0][1]
# for x in ls[1:]:
#     path += "->" + x[1]
# print(path)
def balanceGraph(g):
    for node in g.nodes:
        if g.out_degree(node) < g.in_degree(node):
            for node2 in g.nodes:
                if g.out_degree(node2) > g.in_degree(node2):
                    g.add_edge(node, node2)
                    return (node2, node)


def EulerianPath(g):
    start, end = balanceGraph(g)

    path = ec.EulerianCycle2(g, start=start)
    return "->".join(path[:-1].split("->"))


def AllEulerianPaths(g):
    start, end = balanceGraph(g)
    paths = ["->".join(cycle[:-1]) for cycle in ec.AllEulerianCycles(g) if cycle[0] == start and cycle[-2] == end]
    return paths


if __name__ == '__main__':
    g = nx.MultiDiGraph()
    while True:
        try:
            pair = input().split(" -> ")
            pair[1] = pair[1].split(",")
            for n2 in pair[1]:
                g.add_edge(pair[0], n2)
        except EOFError as e:
            break
    print(EulerianPath(g))
