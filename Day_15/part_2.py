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

def search(sensors, beacons, max_val):
  for y in range(max_val+1):
    x = 0
    while x <= max_val:
      if (x,y) in beacons:
        break
      diff = [v - manhattan(k, (x,y)) for k, v in sensors.items()]
      if all([d<0 for d in diff]):
        return (x, y)
      x += max(diff) + 1
    print(y)

if __name__== '__main__':
  sensors, beacons = parse_input('input.txt')

  MAX = 4000000

  x, y = search(sensors, beacons, MAX)

  print((x,y), x*MAX+y)
