from Assembly.paired_assemble import *
from Paths.eulerian_path import *
from GraphGenerators.paired_kmer_graph import *
import networkx as nx
import matplotlib.pyplot as plt


def paired_reconstruction(Patterns, d):
    db = DeBruijn(Patterns)
    # db = DeBruijn(sorted(Patterns))
    plt.figure(1)
    # nx.draw_networkx(db, with_labels=True, node_color="blue", pos=nx.kamada_kawai_layout(db), font_color="red")
    # plt.show()
    path = EulerianPath(db)
    text = paired_assemble(path, d+1)
    return text


if __name__ == '__main__':
    d = int(input().split(" ")[1])
    patterns = []
    while True:
        try:
            patterns.append(input())
        except EOFError as e:
            break
    print(paired_reconstruction(patterns, d))
    # plt.show()

# AGGGGGGGGGGT