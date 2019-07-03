from linear_sequence import *
from eulerian_cycle import *
from kmer_graph import *

def UniversalBinary(k):
    n = 2 ** k
    patterns = [f'{i:0{k}b}' for i in range(n)]
    # print(patterns)
    db = DeBruijn(patterns)
    plt.figure(1)
    nx.draw_networkx(db, with_labels=True, node_color="blue", pos=nx.kamada_kawai_layout(db), font_color="red")
    path = EulerianCycle(db)
    text = PathToGenome(path)
    return text


if __name__ == '__main__':
    k = int(input())
    print(UniversalBinary(k))
    plt.show()