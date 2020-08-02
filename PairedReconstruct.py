from Assembly.paired_assemble import *
from Paths.eulerian_path import *
from GraphGenerators.paired_kmer_graph import *
import networkx as nx
import matplotlib.pyplot as plt


def paired_reconstruction(Patterns, d):
    print("Building graph...")
    db = DeBruijn(Patterns)
    # db = DeBruijn(sorted(Patterns))
    plt.figure(1)
    # nx.draw_networkx(db, with_labels=True, node_color="blue", pos=nx.kamada_kawai_layout(db), font_color="red")
    # plt.show()
    print("Finding paths...")
    paths = AllEulerianPaths(db)
    print("Assembling paths...")
    texts = [paired_assemble(path, d+1) for path in paths]
    return texts


if __name__ == '__main__':
    d = int(input().split(" ")[1])
    patterns = []
    while True:
        try:
            patterns.append(input())
        except EOFError as e:
            break
    results = paired_reconstruction(patterns, d)
    print(f"Found {len(results)} possible assemblies: ")
    for text in results:
        print(text)
        print("-"*10)

    # plt.show()

# AGGGGGGGGGGT