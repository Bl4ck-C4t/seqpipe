# print(ls)

def PathToGenome(path):
    path = path.split("->")
    k = len(path[0])
    genome = path[0]
    for i in range(len(path) - 1):
        genome += path[i + 1][k - 1]
    return genome


if __name__ == '__main__':
    ls = []
    while True:
        try:
            ls.append(input())
        except EOFError as e:
            break
    print(PathToGenome(ls))
