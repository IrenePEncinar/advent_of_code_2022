# Starting point
H = [0, 0]
T = [0, 0]

positions = set()
positions.add(tuple(T))

with open('input.txt') as f:
  for line in f.read().split('\n'):
    d, num = line.split(' ')

    for i in range(int(num)):
      match d:
        case 'R':
          H[0] += 1
        case 'U':
          H[1] += 1
        case 'L':
          H[0] -= 1
        case 'D':
          H[1] -= 1

      x = H[0] - T[0]
      y = H[1] - T[1]
      if abs(x) > 1 or abs(y) > 1:
        T[0] += x//abs(x) if (abs(x) > 1) or (abs(x) == 1 and abs(y) > 1) else 0
        T[1] += y//abs(y) if (abs(y) > 1) or (abs(y) == 1 and abs(x) > 1) else 0
        positions.add(tuple(T))

print(len(positions))