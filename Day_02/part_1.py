with open('input.txt') as f:
	points = {
		'A X': 4,
		'A Y': 8,
		'A Z': 3,
		'B X': 1,
		'B Y': 5,
		'B Z': 9,
		'C X': 7,
		'C Y': 2,
		'C Z': 6
	}
	
	print(sum([points.get(line, 0) for line in f.read().split('\n')]))
