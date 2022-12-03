def get_priority(c):
  return o - 38 if (o := ord(c)) < 97 else o - 96

with open('input.txt') as f:
  lines = f.read().split('\n')
  print(sum([get_priority(next(iter(set(g[0]).intersection(set(g[1])).intersection(set(g[2]))))) for g in zip(lines[::3], lines[1::3],lines[2::3])]))