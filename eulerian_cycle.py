import networkx as nx
import matplotlib.pyplot as plt


def EulerianCycle(g):
    ls = list(nx.eulerian_circuit(g))
    path = ls[0][0] + "->" + ls[0][1]
    for x in ls[1:]:
        path += "->" + x[1]
    return path


def EulerianCycle2(g):
    pass


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
    print(EulerianCycle(g))
    nx.draw_networkx(g, with_labels=True, pos=nx.kamada_kawai_layout(g), font_color="red", node_color="blue")
    plt.show()
