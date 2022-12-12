from functools import reduce

from input import monkeys


for round in range(20):
  for i, monkey in enumerate(monkeys):
    for item in monkey['items']:
      new = monkey['operation'](item) // 3
      j = monkey['test'](new)
      monkeys[j]['items'].append(new)
    monkey['count'] += len(monkey['items'])
    monkey['items'] = []


print( reduce(lambda x,y: x*y, sorted([m['count'] for m in monkeys], reverse=True)[:2]) )