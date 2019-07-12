from sys import argv
import re
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import math
from typing import *


class WrongFormat(RuntimeError):
    pass


reg = r'(?P<chromosome>\w+)\s+(?P<source>\w+\.\w+)\s+(?P<feature>\w+)\s+(?P<start>\d+)\s+(?P<end>\d+)\s+' \
      r'(?P<score>.+|\.)\s+(?P<sign>\+|\-)\s+(?P<frame>.+?|\.)\s+(?P<additional>.+)'
reg2 = r'(?P<chromosome>\w+)\s+(?P<start>\d+)\s+(?P<end>\d+)\s+(?P<additional>.+)'
entries_reg = r'(?P<key>\w+)\s+(?P<value>\".+?\")'
# entries_reg2 = r'(?P<name>\w+)\s+(?P<score>.+|\.)\s+(?P<strand>\w+\-|\+)\s+(?P<thickStart>\d+)\s+(?P<thickEnd>\d+)' \
#               r'\s+(?P<itemRgb>(\d+,\d+,\d+)|0)\s+(?P<blockCount>\d+)'
entries_reg2 = r"(.+?)\s+"
reg3 = r'(?P<bin>\d+)\s+(?P<name>.+?)\s+(?P<chrom>\w+)\s+(?P<sign>\+|\-)\s+(?P<txStart>\d+)\s+(?P<txEnd>\d+)' \
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
    def __init__(self, gene_id, strand):
        self.gene_id = gene_id
        self.strand = strand

    def __str__(self):
        return self.gene_id

    def __repr__(self):
        return str(self)


class GeneModel(BasicGeneModel):
    def __init__(self, gene_id, strand):
        super().__init__(gene_id, strand)
        self.transcripts: List[Transcript] = []


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
                    a = GeneModel(entries["gene_id"], entries["sign"])
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

                a = BasicGeneModel(entries["name"], entries["sign"])
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
                if line.startswith("#bin"):
                    continue
                if gene_match is None:
                    raise WrongFormat("Wrong file format given")
                try:
                    a = next(g for g in all_genomes if g.gene_id == gene_match.group("name2"))
                except StopIteration:
                    a = GeneModel(gene_match.group("name2"), gene_match.group("sign"))
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
        with open(fname, "w") as f:
            for gene in genes:
                for transcript in gene.transcripts:
                    ent = transcript.additional
                    f.write(
                        f"{ent['bin']}\t{ent['name']}\t{ent['chrom']}\t{ent['sign']}\t{ent['txStart']}\t{ent['txEnd']} "
                        f"\t{ent['cdsStart']}\t{ent['cdsEnd']}\t{ent['exonCount']}\t{ent['exonStarts']} "
                        f"\t{ent['exonEnds']}\t{ent['score']}\t{ent['name2']}\t{ent['cdsStartStat']} "
                        f"\t{ent['cdsEndStat']}\t{ent['exonFrames']}\n")
        print(f"Object written to file '{fname}'")


class Visualizer:
    @staticmethod
    def generate_scale(mn, mx, a, b) -> Callable[[int], float]:
        scale = lambda x: (((b - a) * (x - mn)) / (mx - mn)) + a
        return scale

    @staticmethod
    def max_and_min_transcript_points(genome: GeneModel) -> Tuple[int, int]:
        ls: List[str] = []
        for trans in genome.transcripts:
            ls += trans.additional["exonStarts"].split(",")[:-1]
            ls += trans.additional["exonEnds"].split(",")[:-1]
        all_positions: List[int] = [int(x) for x in ls]

        return max(all_positions), min(all_positions)

    @staticmethod
    def full(genomes):
        genome: GeneModel = genomes[0]
        strand = genome.transcripts[0].additional["sign"]
        # plt.figure(1)
        for trans, y in zip(genome.transcripts, reversed(range(10))):
            trans: Transcript
            y /= 10
            # plt.arrow(0, y, trans.additional["cdsEnd"], y)
            trans_end = int(trans.additional["txEnd"]) / 100000000 + 0.6
            if strand == "-":
                plt.arrow(0, y, trans_end, 0, width=0.005)
                plt.text(int(trans.additional["txEnd"]) / 100000000 + 0.6, y + 0.04, trans.additional["name"])
                plt.text(int(trans.additional["txEnd"]) / 100000000 + 0.65, y-0.02, trans.additional["chrom"])
            mx, mn = Visualizer.max_and_min_transcript_points(genome)
            scale = Visualizer.generate_scale(mx, mn, 0, trans_end)

            for start, end in zip(trans.additional["exonStarts"].split(",")[:-1],
                                  trans.additional["exonEnds"].split(",")[:-1]):
                pass
                pass
                plt.axes().add_patch(patch.Rectangle((scale(int(start))-0.03, y - 0.04),
                                                     (scale(int(end)) - scale(int(start))) * 5, 0.08))
                # plt.axes().add_patch(patch.Rectangle((int(start)/65000000, y - 0.04),
                #                                      (int(end) / 100000000 - int(start) / 100000000) * 3000, 0.08))
                # plt.axes().add_patch(patch.Rectangle((0.2, 0.4), 0.3, 0.3))
        plt.show()


if __name__ == '__main__':
    all_genomes: list = []
    if len(argv) > 1:
        extension = argv[1][argv[1].index(".") + 1:]
        if extension == "gtf":
            all_genomes = Parser.gtf(argv[1])
        elif extension == "bed":
            all_genomes = Parser.bed(argv[1])
        elif extension == "full":
            all_genomes = Parser.full(argv[1])
            # Translator.full("genes.full", all_genomes)
            Visualizer.full(all_genomes)
        genome_set = set(all_genomes)

        print(f"All genomes read: {', '.join([str(x) for x in genome_set])}")

    else:
        print('Specify filename!')
