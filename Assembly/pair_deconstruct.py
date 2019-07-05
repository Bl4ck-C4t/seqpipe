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
    s = ""
    for x in ls:
        s += f'({x})\n'
    print(s)
    for x in sorted(ls):
        print(x)
