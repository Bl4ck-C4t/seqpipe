from typing import List

from Peptide_Assembler import transcribe
from compl_dict import ComplDict

compl = ComplDict()
compl['G'] = 'C'
compl['T'] = 'A'


def codes_for(dna: str, peptide: str) -> bool:
    rev_compl_dna_string = "".join([compl[x] for x in dna[::-1]])

    rna1 = dna.replace("T", "U")
    rna2 = rev_compl_dna_string.replace("T", "U")
    peptide1 = transcribe(rna1)
    peptide2 = transcribe(rna2)
    return peptide in (peptide1, peptide2)


def get_substrings(gene, peptide) -> List[str]:
    offset = len(peptide) * 3
    dna_substrings = []
    for i in range(0, len(gene) - offset + 1):
        dna_string = gene[i:i + offset]

        if codes_for(dna_string, peptide):
            dna_substrings.append(dna_string)

    return dna_substrings


# print(len(dna_substrings))


if __name__ == "__main__":
    gene = input("Enter gene: ")
    peptide = input("Enter peptide: ")
    dna_substrings = get_substrings(gene, peptide)
    for dna in dna_substrings:
        print(dna)
