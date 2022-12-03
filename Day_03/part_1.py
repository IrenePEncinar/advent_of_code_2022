def get_priority(c):
  return o - 38 if (o := ord(c)) < 97 else o - 96

with open('input.txt') as f:
  print(sum([get_priority(next(iter(set(l[:len(l)//2]).intersection(set(l[len(l)//2:]))))) for l in f.read().split('\n')]))