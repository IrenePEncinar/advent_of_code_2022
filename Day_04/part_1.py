def to_set(s):
  n1, n2 = s.split('-')
  return set(range(int(n1), int(n2)+1))

def get_sets(line):
  return [to_set(s) for s in line.split(',')]

def contains(sets):
  return sets[0].issubset(sets[1]) or sets[0].issuperset(sets[1])

with open('input.txt') as f:
  print (sum([contains(get_sets(line)) for line in f.read().split('\n')]))