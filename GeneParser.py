from sys import argv
import re


class WrongFormat(RuntimeError):
    pass


reg = r'(?P<chromosome>\w+)\s+(?P<source>\w+\.\w+)\s+(?P<feature>\w+)\s+(?P<start>\d+)\s+(?P<end>\d+)\s+' \
      r'(?P<score>.+|\.)\s+(?P<sign>\+|\-)\s+(?P<frame>.+?|\.)\s+(?P<additional>.+)'
entries_reg = r'(?P<key>\w+)\s+(?P<value>\".+?\")'


class Transcript:
    def __init__(self, gene_id, chromosome, feature, start, end, score, sign, frame, additional):
        self.gene_id = gene_id
        self.chromosome = chromosome
        self.feature = feature
        self.start = start
        self.end = end
        self.score = score
        self.sign = sign
        self.frame = frame
        self.additional = additional

    def __str__(self):
        return self.additional["transcript_id"]

    def __repr__(self):
        return str(self)


class GeneModel:
    def __init__(self, gene_id):
        self.gene_id = gene_id
        self.transcripts = []

    def __eq__(self, other):
        return self.gene_id == other.gene_id

    def __str__(self):
        return self.gene_id

    def __repr__(self):
        return str(self)


all_genomes = []
if len(argv) > 1:
    with open(argv[1], "r") as f:
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
            trans = Transcript(entries["gene_id"], gene_match.group("chromosome"), gene_match.group("feature"),
                               gene_match.group("start"), gene_match.group("end"), gene_match.group("score"),
                               gene_match.group("sign"), gene_match.group("frame"), entries)
            a.transcripts.append(trans)
            print(f"Added transcript {entries['transcript_id']} to gene {entries['gene_id']}")
            # print(gene_match.group("source"))
else:
    print('Specify filename!')

print(f"All genomes read: {', '.join([str(x) for x in all_genomes])}")