def deassemble(genome, k):
    ls = []
    for i in range(len(genome) - k + 1):
        ls.append(genome[i:i + k])
    return ls


if __name__ == '__main__':
    k = int(input())
    genome = input()

    for x in sorted(deassemble(genome, k)):
        print(x)
