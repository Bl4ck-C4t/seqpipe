import networkx
def break_down(genome, k):
	return [genome[i:i+k] for i in range(len(genome)-k+1)]

class Node:
	def __init__(self, val):
		self.value = val
		self.connections = []

	def __repr__(self):
		return self.value

	def __str__(self):
		return self.value

	def __eq__(self, other):
		return self.value == other.value

	def printGraph(graph):
		for node in graph:
			print(f'{str(node)} -> {",".join(map(lambda x: str(x), node.connections))}')

def findEl(el, ls):
	index = 0
	for x in ls:
		if x is el:
			return index
		index+=1
	return None


k = int(input())
genome = input()


reads = break_down(genome, k)
nodes = break_down(genome, k-1)
print(nodes)
# graph = [Node(nodes[x]) for x in range(len(nodes))]
graph = []
for i in range(len(nodes)):
	node = Node(nodes[i])
	if not node in graph or True:
		graph.append(node)
		if i > 0:
			graph[i-1].connections.append(node)
		# node.connections.append(graph[-1])
graph2 = []
i = 0
while i < len(graph):
	node = graph[i]
	if graph.count(node) > 1:
		matches = list(filter(lambda x: x == node and x is not node, graph))
		print(matches)
		for match in matches:
			node.connections += match.connections
			# graph.remove(match)
			del graph[findEl(match, graph)]
			i -= 1
	graph2.append(node)
	i += 1

# print(graph[:-1])
Node.printGraph(graph[:-1])

		


