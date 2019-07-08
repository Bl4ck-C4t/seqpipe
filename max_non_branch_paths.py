import networkx as nx
import matplotlib.pyplot as plt


def one_in_one(g, node):
    return g.out_degree(node) == 1 and g.in_degree(node) == 1


def non_branch_paths(g):
    paths = []
    for node in g:
        path = []
        if not one_in_one(g, node):
            if g.out_degree(node) > 0:
                for edge in g.out_edges(node):
                    path.append(edge[0])
                    path.append(edge[1])
                    curr_node = edge[1]
                    while one_in_one(g, curr_node):
                        next_edge = list(g.out_edges(curr_node))[0]
                        curr_node = next_edge[1]
                        path.append(curr_node)
                    # path = [x for n in path for x in n]
                    paths.append("->".join(path))
                    path.clear()
    for path in isolated_cycles(g):
        paths.append("->".join(path))
    return paths


def isolated_cycles(g):
    used_nodes = set()
    for node in g:
        if node in used_nodes:
            continue
        r = performCycle(g, node)
        if r is None:
            continue
        used_nodes = used_nodes.union(set(r))
        yield r


def performCycle(g, start):
    reset_edges(g)
    curr_node = start
    path = [start]
    while True:
        if not one_in_one(g, curr_node):
            return None
        next_edges = list(filter(lambda x: x[2] is False, g.out_edges(curr_node, data='v')))
        if len(next_edges) == 0:
            # cycle completed
            return path
        next_edge = next_edges[0]
        if next_edge[1] == curr_node:
            for i in range(len(list(filter(lambda x: x[0] == x[1], next_edges)))):
                path.append(curr_node)
                g[curr_node][curr_node][i]['v'] = True
            continue
        curr_node = next_edge[1]
        g.edges[next_edge]['v'] = True
        # path.append(g[next_edge[0]][next_edge[1]][0]['val'])
        path.append(curr_node)


def reset_edges(g):
    for edge in g.edges:
        g.edges[edge]['v'] = False


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
