def count(mass):
    masses = set()
    with open("integer_mass_table.txt") as f:
        for line in f:
            _, ms = line.split(" ")
            masses.add(int(ms))
def LinearCount(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res + 1


if __name__ == "__main__":
    mass = int(input("Enter mass: "))
    print(count(mass))
