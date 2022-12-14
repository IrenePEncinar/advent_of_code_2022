from functools import cmp_to_key

def compare(a, b):
  if isinstance(a, int) and isinstance(b, int):
    return (a > b) - (a < b)
  elif isinstance(a, int) and isinstance(b, list):
    return compare([a], b)
  elif isinstance(a, list) and isinstance(b, int):
    return compare(a, [b]) 
  elif isinstance(a, list) and isinstance(b, list):
    for (x, y) in zip(a, b):
      if (c:= compare(x, y)) != 0:
        return c
    return compare(len(a), len(b))

with open('input.txt') as f:
  lists = [eval(line) for line in f.read().strip().replace('\n\n', '\n').split('\n')]
  
  d1 = [[2]]
  d2 = [[6]] 
  lists.append(d1)
  lists.append(d2)

  ordered = sorted(lists, key=cmp_to_key(compare))

  i1 = ordered.index(d1)
  i2 = ordered.index(d2, i1)

  print((i1+1)*(i2+1))