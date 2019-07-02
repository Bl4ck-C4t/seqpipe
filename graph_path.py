ls = []
while True:
	try:
		ls.append(input())
	except EOFError as e:
		break

def preffix(r):
	k = len(r)
	return r[:k-1]

def suffix(r):
	k = len(r)
	return r[-(k-1):]

def find_path(r, ls):
	# path = f'{r} -> '
	paths = []
	for x in ls:
		if suffix(r) == preffix(x):
			paths.append(x)
	if len(paths) == 0:
		return None
	else:
		return f'{r} -> {",".join(paths)}'

paths = []
k = len(ls[0])
for read in ls:
	path = find_path(read, ls)
	if path is not None and path not in paths:
		paths.append(path)

for path in paths:
	print(path)
# print(suffix("TAA"))
# print(preffix("TAA"))

