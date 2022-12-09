# Starting point
HT = [[0, 0] for i in range(10)]

positions = set()
positions.add(tuple(HT[9]))

with open('input.txt') as f:
  for line in f.read().split('\n'):
    d, num = line.split(' ')

    for i in range(int(num)):
      match d:
        case 'R':
          HT[0][0] += 1
        case 'U':
          HT[0][1] += 1
        case 'L':
          HT[0][0] -= 1
        case 'D':
          HT[0][1] -= 1

      for H, T in zip(HT[:-1], HT[1:]):  
        x = H[0] - T[0]
        y = H[1] - T[1]
        if abs(x) > 1 or abs(y) > 1:
          T[0] += x//abs(x) if (abs(x) > 1) or (abs(x) == 1 and abs(y) > 1) else 0
          T[1] += y//abs(y) if (abs(y) > 1) or (abs(y) == 1 and abs(x) > 1) else 0
      
      positions.add(tuple(HT[9]))

print(len(positions))