with open('input.txt') as f:
	print(max([sum([int(x) for x in line.split('\n')]) for line in f.read().strip().split('\n\n')]))
