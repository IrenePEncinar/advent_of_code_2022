with open('input.txt') as f:
	print(sum(sorted([sum([int(x) for x in line.split('\n')]) for line in f.read().strip().split('\n\n')])[-3:]))
