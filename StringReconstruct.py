from Assembly.assemble import *
from Paths.eulerian_path import *
from GraphGenerators.kmer_graph import *
import networkx as nx
import matplotlib.pyplot as plt

def StringReconstruction(Patterns):
    db = DeBruijn(Patterns)
    plt.figure(1)
    nx.draw_networkx(db, with_labels=True, node_color="blue", pos=nx.kamada_kawai_layout(db), font_color="red")
    plt.show()
    path = EulerianPath(db)
    text = PathToGenome(path)
    return text


if __name__ == '__main__':
    input()
    patterns = []
    while True:
        try:
            patterns.append(input())
        except EOFError as e:
            break
    print(StringReconstruction(patterns))
    # plt.show()
