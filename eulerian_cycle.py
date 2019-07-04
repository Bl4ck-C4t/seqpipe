import networkx as nx
import matplotlib.pyplot as plt
import threading


def EulerianCycle(g):
    ls = list(nx.eulerian_circuit(g))
    path = ls[0][0] + "->" + ls[0][1]
    for x in ls[1:]:
        path += "->" + x[1]
    return path


def reset_edges(g):
    for edge in g.edges:
        g.edges[edge]['v'] = False


def all_next_nodes(g, path):
    nodes = []
    for node in path:
        if len(list(filter(lambda x: x[2] is False, g.out_edges(node, data='v')))) > 0:
            nodes.append(node)
    return nodes


def find_next_node(g, path):
    nodes = all_next_nodes(g, path)
    if len(nodes) > 0:
        return nodes[0]
    return None


def combine(path, full_path):
    if len(path) == 0:
        path += full_path
        return
    else:
        path += full_path[1:]

def AllEulerianCycles2(g, start=None):
    if start is None:
        start = list(g.nodes)[0]
    reset_edges(g)
    path = []
    curr_node = start
    paths = []
    while True:
        full_path = performCycle(g, curr_node)
        combine(path, full_path)
        # next_node = find_next_node(g, path)
        for next_node in all_next_nodes(g, path):

            if next_node is None:
                return "->".join(path)
            new_path = []
            ind = -(path[::-1].index(next_node) + 1)
            new_path += path[ind:]
            new_path += path[1:ind + 1]
            path = new_path
            curr_node = next_node


def EulerianCycle2(g, start=None):
    if start is None:
        start = list(g.nodes)[0]
    reset_edges(g)
    path = []
    curr_node = start
    while True:
        full_path = performCycle(g, curr_node)
        combine(path, full_path)
        next_node = find_next_node(g, path)
        if next_node is None:
            return "->".join(path)
        new_path = []
        ind = -(path[::-1].index(next_node) + 1)
        new_path += path[ind:]
        new_path += path[1:ind + 1]
        path = new_path
        curr_node = next_node


def performCycle(g, start):
    curr_node = start
    path = [start]
    while True:
        next_edges = list(filter(lambda x: x[2] is False, g.out_edges(curr_node, data='v')))
        if len(next_edges) == 0:
            # cycle completed
            return path
        next_edge = next_edges[0]
        curr_node = next_edge[1]
        g.edges[next_edge]['v'] = True
        # path.append(g[next_edge[0]][next_edge[1]][0]['val'])
        path.append(curr_node)

def AllEulerianCycles(g):
    return set([EulerianCycle2(g, node) for node in g])



def draw_thread(g):
    nx.draw_networkx(g, with_labels=True, pos=nx.kamada_kawai_layout(g), font_color="red", node_color="blue")
    plt.show()


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

    # x = threading.Thread(target=draw_thread, args=(g))

    nx.draw_networkx(g, with_labels=True, pos=nx.kamada_kawai_layout(g), font_color="red", node_color="blue")
    plt.show()
    print(EulerianCycle2(g))
    print(AllEulerianCycles(g))
