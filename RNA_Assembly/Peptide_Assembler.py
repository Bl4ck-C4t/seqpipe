codon_table = dict()
with open("RNA_codon_table_1.txt") as f:
    for line in f:
        kmer, amino = line.split(" ")
        codon_table[kmer] = amino.rstrip("\n")


def transcribe(rna_string):
    transcript = ""
    for i in range(0, len(rna_string), 3):
        kmer = rna_string[i:i + 3]
        transcript += codon_table[kmer]
    return transcript


if __name__ == "__main__":
    gene = input("Enter gene: ")
    print(transcribe(gene))
