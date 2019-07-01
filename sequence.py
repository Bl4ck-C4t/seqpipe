ls = []
while True:
	try:
		ls.append(input())
	except EOFError as e:
		break
	
print(ls)
k = len(ls[0])
genome = ""
for node in ls:
	genome += node[k-1:]

print(genome)