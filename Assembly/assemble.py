# print(ls)
def preffix(r):
    k = len(r)
    return r[:k - 1]


def suffix(r):
    k = len(r)
    return r[-(k - 1):]


def PathToGenome(path):
    path = path.split("->")
    k = len(path[0])
    genome = path[0]
    for i in range(len(path)-1):
        # if preffix(path[i + 1]) != suffix(path[i]):
        #     raise Exception(f"Part mismatch: {path[i]} -/> {path[i + 1]}")
        genome += path[i + 1][k - 1]
    return genome


if __name__ == '__main__':
    ls = []
    while True:
        try:
            ls.append(input())
        except EOFError as e:
            break
    print(PathToGenome("->".join(ls)))
