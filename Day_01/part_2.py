with open('elves_food.txt') as f:
	print(sum(sorted([sum([int(x) for x in elf_cals.split('\n')]) for elf_cals in f.read().strip().split('\n\n')])[-3:]))
