forest = []
with open('input.txt') as f:
  for line in f.read().split('\n'):
    forest.append([int(c) for c in line])

h = len(forest)
w = len(forest[0])
score = 0

for i, r in enumerate(forest):
  for j, elem in enumerate(r):
    # Top
    score_t = next((y+1 for y, x in enumerate((forest[k][j] for k in range(i-1,-1,-1))) if x >= elem), i)

    # Right
    score_r = next((y+1 for y, x in enumerate((forest[i][k] for k in range(j+1,w))) if x >= elem), w-j-1)

    # Bottom
    score_b = next((y+1 for y, x in enumerate((forest[k][j] for k in range(i+1,h))) if x >= elem), h-i-1)

    # Left
    score_l = next((y+1 for y, x in enumerate((forest[i][k] for k in range(j-1,-1,-1))) if x >= elem), j)

    score_elem = score_t * score_r * score_b * score_l
    score = score_elem if score_elem > score else score

# Printing
print(score)
