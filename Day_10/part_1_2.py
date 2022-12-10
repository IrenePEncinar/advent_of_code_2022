X = 1
xhist = []
xhist.append(X)

with open('input.txt') as f:
  for line in f.read().split('\n'):
    if len(cmd := line.split(' ')) == 2:
      if cmd[0] == 'addx':
        xhist.append(X)
        xhist.append(X)
        X += int(cmd[1])

    elif cmd[0] == 'noop':
      xhist.append(X)


print('Part 1:',sum([i*xhist[i] for i in (20,60,100,140,180,220)]))

# Part 2
for i, x in enumerate(xhist[1:]):
  pos = i % 40
  print('#' if abs (pos - x) <=1 else '.', end='\n' if pos == 39 else '')
