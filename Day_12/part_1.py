S = [-1,-1]
E = [-1,-1]
heightmap = []

with open('input.txt') as f:
  for i, line in enumerate(f.read().strip().split('\n')):
    heightmap.append([c for c in line])
    
    if S[1] == -1: 
      try:
        S[1] = line.index('S')
        S[0] = i
        heightmap[i][S[1]] = 'a'
      except:
        continue

    if E[1] == -1: 
      try:
        E[1] = line.index('E')
        E[0] = i
        heightmap[i][E[1]] = 'z'
      except:
        continue

explored = set()
to_explore = [(*S, 0)]

while True:
  x, y, depth = to_explore.pop(0)
  
  if [x, y] == E:
    print('Distance: ', depth)
    break

  if (x,y) in explored: 
    continue
  
  explored.add((x,y))
  h = heightmap[x][y]

  # Left
  if y >= 1 and ord(heightmap[x][y-1]) <= ord(h) + 1:
    to_explore.append((x,y-1,depth+1))
  
  # Bottom
  if x < len(heightmap) - 1 and ord(heightmap[x+1][y]) <= ord(h) + 1:
    to_explore.append((x+1,y,depth+1))

  # Right
  if y < len(heightmap[0]) - 1 and ord(heightmap[x][y+1]) <= ord(h) + 1:
    to_explore.append((x,y+1,depth+1))

  # Top
  if x >= 1 and ord(heightmap[x-1][y]) <= ord(h) + 1:
    to_explore.append((x-1,y,depth+1))
  
