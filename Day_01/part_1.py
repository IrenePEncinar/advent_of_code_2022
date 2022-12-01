with open('elves_food.txt') as f:
	print(max([sum([int(x) for x in elf_cals.split('\n')]) for elf_cals in f.read().strip().split('\n\n')]))
