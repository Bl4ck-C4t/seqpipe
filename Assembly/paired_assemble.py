from Assembly.assemble import *


def paired_assemble(pairs, d):
    pairs = pairs.split("->")
    pairs = list(map(lambda x: tuple(x.split("|")), pairs))
    ls1 = [p1 for p1, p2 in pairs]
    ls2 = [p2 for p1, p2 in pairs]
    part1 = PathToGenome("->".join(ls1))
    part2 = PathToGenome("->".join(ls2))
    k = len(pairs[0][0])
    # if part1[k+d:] != part2[:-(k+d)]:
    #     raise Exception(f"Part mismatch: {part1} -/> {part2}")
    # print(part1)
    # print(part2)
    return part1 + part2[-(k + d):]
    # return part1 + part2[len(pairs)-k:]
    # return part1 + part2[(2 * k) + d:]


if __name__ == '__main__':
    d = int(input().split(" ")[1])
    ls = []
    while True:
        try:
            ls.append(input())
        except EOFError as e:
            break
    print(paired_assemble("->".join(ls), d))

# TAATGCCATGGGA  3,1 11 is 9
#     GCCATGGGATGTT
# TAATGCCATGGGATGTT
# TAATGCCATGGGAATGTT
# AGCAGCTGCT 2,1 9 is 7
#    AGCTGCTGCA
# AGCAGCTGCTGCA

# AGCAGC 3, 1 4 is 2
#     GCTGCT
# AGCAGCTGCT
#

# TAATGCCATGGGAT 3,2 12 is 9
#      CCATGGGATGTTAG
# TAATGCCATGGGATGTTAG
# TAATGCCATGGGATGTTAG