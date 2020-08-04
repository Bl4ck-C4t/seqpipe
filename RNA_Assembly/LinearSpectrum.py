def LinearSpectrum(peptide):
    masses = dict()
    with open("integer_mass_table.txt") as f:
        for line in f:
            amino, mass = line.split(" ")
            masses[amino] = int(mass)

    preffix_masses = [0]
    for i in range(0, len(peptide)):
        mass = masses[peptide[i]]
        preffix_masses.append(preffix_masses[-1] + mass)
    spectrum = [0]
    for i in range(0, len(peptide)):
        for j in range(i+1, len(peptide)+1):
            spectrum.append(preffix_masses[j] - preffix_masses[i])

    return sorted(spectrum)

def CyclicSpectrum(peptide):
    masses = dict()
    with open("integer_mass_table.txt") as f:
        for line in f:
            amino, mass = line.split(" ")
            masses[amino] = int(mass)

    preffix_masses = [0]
    for i in range(0, len(peptide)):
        mass = masses[peptide[i]]
        preffix_masses.append(preffix_masses[-1] + mass)
    peptide_mass = preffix_masses[-1]
    spectrum = [0]
    for i in range(0, len(peptide)):
        for j in range(i+1, len(peptide)+1):
            spectrum.append(preffix_masses[j] - preffix_masses[i])
            if i > 0 and j < len(peptide):
                spectrum.append(peptide_mass - spectrum[-1])
    return sorted(spectrum)


if __name__ == "__main__":
    peptide = input("Enter peptide: ")
    masses = CyclicSpectrum(peptide)
    print(" ".join([str(x) for x in masses]))
