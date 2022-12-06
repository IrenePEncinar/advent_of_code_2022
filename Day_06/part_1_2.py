def get_distinct(stream, n):
  for i, code in enumerate(zip(*[stream[i:] for i in range(n)])):
    if len(set(code)) == n:
      return i+n

with open('input.txt') as f:
  s = f.read()
  print(1, get_distinct(s,4))
  print(2, get_distinct(s,14))