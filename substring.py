k = int(input())
genome = input()
ls = []
for i in range(len(genome)-k+1):
	ls.append(genome[i:i+k])
for x in sorted(ls):
	print(x)


