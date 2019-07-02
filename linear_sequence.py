ls = []
while True:
	try:
		ls.append(input())
	except EOFError as e:
		break

	
# print(ls)
k = len(ls[0])
genome = ls[0]
for i in range(len(ls)-1):
	genome += ls[i+1][k-1]

print(genome)