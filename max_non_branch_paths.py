import networkx as nx
import matplotlib.pyplot as plt


def non_branch_paths(g):
    paths = []
    for node in g:
        path = []
        if not (g.out_degree(node) == 1 and g.in_degree(node) == 1):
            if g.out_degree(node) > 0:
                for edge in g.out_edges(node):
                    path.append(edge[0])
                    path.append(edge[1])
                    curr_node = edge[1]
                    while g.out_degree(curr_node) == 1 and g.in_degree(curr_node) == 1:
                        next_edge = list(g.out_edges(curr_node))[0]
                        curr_node = next_edge[1]
                        path.append(curr_node)
                    # path = [x for n in path for x in n]
                    paths.append("->".join(path))
                    path.clear()
    for edges in g.selfloop_edges():
        pass
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

    nx.draw_networkx(g, with_labels=True, node_color="blue", pos=nx.kamada_kawai_layout(g), font_color="red")
    plt.show()
    for path in non_branch_paths(g):
        print(path)
