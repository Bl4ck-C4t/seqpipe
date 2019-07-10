from sys import argv
import re


class WrongFormat(RuntimeError):
    pass


reg = r'(?P<chromosome>\w+)\s+(?P<source>\w+\.\w+)\s+(?P<feature>\w+)\s+(?P<start>\d+)\s+(?P<end>\d+)\s+' \
      r'(?P<score>.+|\.)\s+(?P<sign>\+|\-)\s+(?P<frame>.+?|\.)\s+(?P<additional>.+)'
reg2 = r'(?P<chromosome>\w+)\s+(?P<start>\d+)\s+(?P<end>\d+)\s+(?P<additional>.+)'
entries_reg = r'(?P<key>\w+)\s+(?P<value>\".+?\")'
# entries_reg2 = r'(?P<name>\w+)\s+(?P<score>.+|\.)\s+(?P<strand>\w+\-|\+)\s+(?P<thickStart>\d+)\s+(?P<thickEnd>\d+)' \
#               r'\s+(?P<itemRgb>(\d+,\d+,\d+)|0)\s+(?P<blockCount>\d+)'
entries_reg2 = r"(.+?)\s+"
reg3 = r'(?P<bin>\d+)\s+(?P<name>\w+)\s+(?P<chrom>\w+)\s+(?P<sign>\+|\-)\s+(?P<txStart>\d+)\s+(?P<txEnd>\d+)' \
       r'\s+(?P<cdsStart>\d+)\s+(?P<cdsEnd>\d+)\s+(?P<exonCount>\d+)\s+(?P<exonStarts>.+?)\s+(?P<exonEnds>.+?)' \
       r'\s+(?P<score>\d+)\s+(?P<name2>.+?)\s+(?P<cdsStartStat>\w+)\s+(?P<cdsEndStat>\w+?)\s+(?P<exonFrames>.+)'


class Transcript:
    def __init__(self, additional):
        self.additional = additional

    def __str__(self):
        if "transcript_id" not in self.additional.keys():
            return self.additional["name"]
        return self.additional["transcript_id"]

    def __repr__(self):
        return str(self)


class BasicGeneModel:
    def __init__(self, gene_id):
        self.gene_id = gene_id

    def __str__(self):
        return self.gene_id

    def __repr__(self):
        return str(self)


class GeneModel(BasicGeneModel):
    def __init__(self, gene_id):
        super().__init__(gene_id)
        self.transcripts = []

    def __str__(self):
        return self.gene_id

    def __repr__(self):
        return str(self)


class Parser:
    @staticmethod
    def gtf(fname):
        all_genomes = []
        with open(fname, "r") as f:
            for line in f:
                gene_match = re.search(reg, line)
                if gene_match is None:
                    raise WrongFormat("Wrong file format given")
                entries = re.findall(entries_reg, gene_match.group("additional"))
                entries = dict(entries)
                try:
                    a = next(g for g in all_genomes if g.gene_id == entries["gene_id"])
                except StopIteration:
                    a = GeneModel(entries["gene_id"])
                    all_genomes.append(a)
                for key in gene_match.groupdict().keys():
                    entries[key] = gene_match.group(key)
                trans = Transcript(entries)
                a.transcripts.append(trans)
                print(f"Added transcript {entries['transcript_id']} to gene {entries['gene_id']}")
        return all_genomes

    @staticmethod
    def bed(fname):
        all_genomes = []
        fields = ["name", "score", "strand",
                  "thickStart", "thickEnd", "itemRgb",
                  "blockCount", "blockSizes", "blockStarts"]
        with open(argv[1], "r") as f:
            for line in f:
                gene_match = re.search(reg2, line)
                if gene_match is None:
                    raise WrongFormat("Wrong file format given")
                entries = gene_match.group("additional").rsplit("\t")
                entries = dict(zip(fields, entries))

                a = BasicGeneModel(entries["name"])
                # print(f"Added new gene {entries['name']}")
                a.data = entries
                all_genomes.append(a)

        return all_genomes

    @staticmethod
    def full(fname):
        all_genomes = []
        with open(fname, "r") as f:
            for line in f:
                gene_match = re.search(reg3, line)
                if gene_match is None:
                    raise WrongFormat("Wrong file format given")
                try:
                    a = next(g for g in all_genomes if g.gene_id == gene_match.group("name2"))
                except StopIteration:
                    a = GeneModel(gene_match.group("name2"))
                    all_genomes.append(a)
                trans = Transcript(gene_match.groupdict())
                a.transcripts.append(trans)
                # print(f"Added transcript {gene_match.group('name')} to gene {gene_match.group('name2')}")
        return all_genomes


#
# r'(?P<bin>\d+)\s+(?P<name>\w+)\s+(?P<chrom>\w+)\s+(?P<sign>\+|\-)\s+(?P<txStart>\d+)\s+(?P<txEnd>\d+)' \
#        r'\s+(?P<cdsStart>\d+)\s+(?P<cdsEnd>\d+)\s+(?P<exonCount>\d+)\s+(?P<exonStarts>.+?)\s+(?P<exonEnds>.+?)' \
#        r'\s+(?P<score>\d+)\s+(?P<name2>.+?)\s+(?P<cdsStartStat>\w+)\s+(?P<cdsEndStat>\w+?)\s+(?P<exonFrames>.+)'
class Translator:
    @staticmethod
    def full(fname, genes):
        with open(fname, "r") as f:
            for gene in genes:
                for transcript in gene.transcripts:
                    ent = transcript.additional
                    f.write(f"{ent['bin']} {ent['name']} {ent['chrom']} {ent['sign']} {ent['txStart']} {ent['txEnd']} "
                            f"{ent['cdsStart']} {ent['cdsEnd']} {ent['exonCount']} {ent['exonStarts']} "
                            f"{ent['exonEnds']} {ent['score']} {ent['name2']} {ent['cdsStartStat']} "
                            f"{ent['cdsEndStat']} {ent['exonFrames']}\n")
        print(f"Object written to file '{fname}'")


if __name__ == '__main__':
    all_genomes = set()
    if len(argv) > 1:
        extension = argv[1][argv[1].index(".") + 1:]
        if extension == "gtf":
            all_genomes = Parser.gtf(argv[1])
        elif extension == "bed":
            all_genomes = Parser.bed(argv[1])
        elif extension == "full":
            all_genomes == Parser.full(argv[1])
            Translator.full("genes.full", all_genomes)
        all_genomes = set(all_genomes)

        print(f"All genomes read: {', '.join([str(x) for x in all_genomes])}")

    else:
        print('Specify filename!')
