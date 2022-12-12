from functools import reduce
from math import lcm

from input import monkeys

mlcm = lcm(*[m['mod'] for m in monkeys])
print (mlcm)

for round in range(10000):
  print (round)
  for i, monkey in enumerate(monkeys):
    for item in monkey['items']:
      new = monkey['operation'](item) % mlcm
      j = monkey['test'](new)
      monkeys[j]['items'].append(new)
    monkey['count'] += len(monkey['items'])
    monkey['items'] = []


print( reduce(lambda x,y: x*y, sorted([m['count'] for m in monkeys], reverse=True)[:2]) )