forest = []
with open('input.txt') as f:
  for line in f.read().split('\n'):
    forest.append([int(c) for c in line])


# Each element in "visible" matrix codes if the element is 
# visible from the 4 directions: clockwise starting from the top
visible = []
count = 0

for i, r in enumerate(forest):
  if i == 0:
    visible.append([ [True, None, None, None] ]*len(forest[0]))
    count += len(forest[0])
    continue
  if i == len(forest)-1:
    visible.append([ [None, None, True, None] ]*len(forest[0]))
    count += len(forest[0])
    continue

  visible.append([])

  for j, elem in enumerate(r):
    visible[i].append([None, None, None, None])

    if j == 0:
      visible[i][j][3] = True
      count += 1
      continue
    if j == len(forest[i])-1:
      visible[i][j][1] = True
      count += 1
      continue
    
    # Top
    if elem > forest[i-1][j]:
      if visible[i-1][j][0]:
        visible[i][j][0] = True
        count += 1
        continue
      else:
        m = max([forest[k][j] for k in range(i-1,-1,-1)])
        if elem > m:
          visible[i][j][0] = True
          count += 1
          continue

    visible[i][j][0] = False

    # Right
    if elem > forest[i][j+1]:
      if elem < forest[i][j-1] and visible[i][j-1][1] == False:
        visible[i][j][1] = False
      else:
        m = max([forest[i][k] for k in range(j+1,len(forest[i]))])
        if elem > m:
          visible[i][j][1] = True
          count += 1
          continue

    visible[i][j][1] = False

    # Bottom
    if elem > forest[i+1][j]:
      if elem < forest[i-1][j] and visible[i-1][j][2] == False:
        visible[i][j][2] = False
      else:
        m = max([forest[k][j] for k in range(i+1,len(forest))])
        if elem > m:
          visible[i][j][2] = True
          count += 1
          continue

    visible[i][j][2] = False


    # Left
    if elem > forest[i][j-1]:
      if visible[i][j-1][3]:
        visible[i][j][3] = True
        count += 1
        continue
      else:
        m = max([forest[i][k] for k in range(j-1,-1,-1)])
        if elem > m:
          visible[i][j][3] = True
          count += 1
          continue

    visible[i][j][3] = False


# Printing
print(count)
