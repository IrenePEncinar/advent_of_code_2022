def compare(a, b):
  if isinstance(a, int) and isinstance(b, int):
    return -1 if a == b else int(a < b)
  elif isinstance(a, int) and isinstance(b, list):
    return compare([a], b)
  elif isinstance(a, list) and isinstance(b, int):
    return compare(a, [b]) 
  elif isinstance(a, list) and isinstance(b, list):
    for (x, y) in zip(a, b):
      if (c:= compare(x, y)) != -1:
        return c
    return compare(len(a), len(b))

with open('input.txt') as f:
  pairs = [pair.split('\n') for pair in f.read().strip().split('\n\n')]
  
  right = 0

  for i, pair in enumerate(pairs):
    right += (i+1)*abs(c) if (c:= compare(eval(pair[0]),eval(pair[1]))) else 0

  print(right)