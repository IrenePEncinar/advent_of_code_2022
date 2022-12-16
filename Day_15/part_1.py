def manhattan(p1, p2):
  x1, y1 = p1
  x2, y2 = p2
  return abs(x2-x1) + abs(y2-y1)

from re import findall
def parse_input(filename):
  sensors = {}
  beacons = set()
  with open(filename) as f:
    for line in f.read().strip().split('\n'):
      x1, y1, x2, y2 = [int(n) for n in findall('-*\d+', line)]
      beacons.add((x2,y2))
      sensors[(x1,y1)] = manhattan((x1,y1),(x2,y2))

  return sensors, beacons

if __name__== '__main__':
  sensors, beacons = parse_input('input.txt')

  xmin = min([min([s[0] for s in sensors.keys()]), min(b[0] for b in beacons)])
  xmax = max([max([s[0] for s in sensors.keys()]), max(b[0] for b in beacons)])

  y = 2000000
  
  no_beacons = [int(any((manhattan(k, (x,y)) <= v for k, v in sensors.items()))) if (x,y) not in beacons else 0 for x in range(xmin, xmax+1000000)]

  print(sum(no_beacons))