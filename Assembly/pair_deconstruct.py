import random
def paired_deassemble(genome, k, d):
    ls = []
    for i in range(len(genome) - (2 * k + d) + 1):
        gn = genome[i:i + k]
        # ls.append(genome[i:i + k])
        gn += "|" + genome[i + d + k:i + k + k + d]
        ls.append(gn)
    return ls


if __name__ == '__main__':
    k, d = list(map(lambda x: int(x), input().split(" ")))
    genome = input()
    ls = paired_deassemble(genome, k, d)
    random.shuffle(ls)
    # s = ""
    # for x in ls:
    #     s += f'({x})\n'
    # print(s)
    print(f'{k} {d}')
    for x in ls:
        print(x)
    with open("../out.txt", "w") as f:
        f.write(f'{k} {d}\n')
        for x in sorted(ls):
            f.write(x + "\n")
