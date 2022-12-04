def to_set(s):
  n1, n2 = s.split('-')
  return set(range(int(n1), int(n2)+1))

def get_sets(line):
  return [to_set(s) for s in line.split(',')]

def overlaps(sets):
  return bool(sets[0].intersection(sets[1]))

with open('input.txt') as f:
  print (sum([overlaps(get_sets(line)) for line in f.read().split('\n')]))