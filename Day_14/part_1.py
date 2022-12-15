def sign(x):
  return x//abs(x) if x != 0 else 1

def parse_input(filename):
  rocks = set()
  with open(filename) as f:
    for path in f.read().strip().split('\n'):
      coords =[eval(c) for c in path.split(' -> ')]
      for (x1, y1), (x2,y2) in zip(coords, coords[1:]):

        for i in range(x1, x2, sign(x2-x1)):
          rocks.add((i,y1))

        for j in range(y1, y2, sign(y2-y1)):
          rocks.add((x1,j))

        rocks.add((x2,y2))

  return rocks

def next_move(s, rocks):
  if not (s[0], s[1]+1) in rocks:
    return (s[0], s[1]+1)
  
  if not (s[0]-1, s[1]+1) in rocks:
    return (s[0]-1, s[1]+1)

  if not (s[0]+1, s[1]+1) in rocks:
    return (s[0]+1, s[1]+1)

  return None


if __name__== '__main__':
  rocks = parse_input('input.txt')
  sand_start = (500,0)
  ymax = max([r[1] for r in rocks])
  units = 0

  stop = False

  # Sand falling
  while not stop:
    s = sand_start
    while s[1] < ymax:
      n = next_move(s, rocks)
      if n is None:
        rocks.add(s)
        units += 1
        print(units)
        break
      s = n
    if s[1] == ymax: 
      stop = True

  print(units)


