from linear_sequence import *
from eulerian_cycle import *
from kmer_graph import *
from sys import argv


def UniversalBinary(k):
    n = 2 ** k
    patterns = [f'{i:0{k}b}' for i in range(n)]
    # print(patterns)
    db = DeBruijn(patterns)
    plt.figure(1)
    nx.draw_networkx(db, with_labels=True, node_color="blue", pos=nx.kamada_kawai_layout(db), font_color="red")
    path = EulerianCycle2(db)
    text = PathToGenome(path)
    return text[:-(k - 1)]


if __name__ == '__main__':
    k = int(input())
    print(UniversalBinary(k))
    if len(argv) > 1 and argv[1] == '-s':
        plt.show()

# 0000110010111101
# 1110110010100001
