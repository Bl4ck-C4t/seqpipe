import networkx as nx
import matplotlib.pyplot as plt
import eulerian_cycle as ec

# nx.eulerize(g)
# ls = list(nx.eulerian_circuit(g))
# path = ls[0][0] + "->" + ls[0][1]
# for x in ls[1:]:
#     path += "->" + x[1]
# print(path)
def EulerianPath(g):
    start = ""
    for node in g.nodes:
        if g.out_degree(node) < g.in_degree(node):
            for node2 in g.nodes:
                if g.out_degree(node2) > g.in_degree(node2):
                    g.add_edge(node, node2)
                    start = node2
    # nx.draw_networkx(g, with_labels=True, pos=nx.kamada_kawai_layout(g), font_color="red", node_color="blue")
    # plt.show()
    path = ec.EulerianCycle2(g, start=start)
    # path = ls[0][0] + "->" + ls[0][1]
    # for x in ls[1:-1]:
    #     path += "->" + x[1]
    return path


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
