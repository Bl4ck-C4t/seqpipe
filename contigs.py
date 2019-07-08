import networkx as nx
import matplotlib.pyplot as plt
from Assembly.deassemble import deassemble
from Assembly.assemble import PathToGenome
from max_non_branch_paths import non_branch_paths
from GraphGenerators.kmer_graph import DeBruijn


def split(ls):
    ls2 = []
    for gene in ls:
        ls2 += deassemble(gene, 2)
    return ls2


if __name__ == '__main__':
    ls = []
    while True:
        try:
            ls.append(input())
        except EOFError as e:
            break

    g = DeBruijn(ls)
    paths = list(non_branch_paths(g))
    paths = [PathToGenome(x) for x in paths]
    print(" ".join(paths))
