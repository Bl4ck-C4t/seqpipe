def paired_deassemble(genome, k, d):
    ls = []
    for i in range(len(genome) - (2 * k + d) + 1):
        gn = genome[i:i + k]
        # ls.append(genome[i:i + k])
        gn += "|" + genome[i + d + k:i + k + k + d]
        ls.append(gn)
    return ls


# s = ""
# for x in sorted(ls):
#     s += f'({x}) '
# print(s)
if __name__ == '__main__':
    k, d = list(map(lambda x: int(x), input().split(" ")))
    genome = input()
    ls = paired_deassemble(genome, k, d)
    for x in ls:
        print(x)
