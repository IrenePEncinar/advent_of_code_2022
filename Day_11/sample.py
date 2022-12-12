monkeys = [
  {
    'items': [79, 98],
    'operation': lambda x: x*19,
    'test': lambda x: 2 if x % 23 == 0 else 3,
    'mod': 23,
    'count': 0
  },
  {
    'items': [54, 65, 75, 74],
    'operation': lambda x: x+6,
    'test': lambda x: 2 if x % 19 == 0 else 0,
    'mod': 19,
    'count': 0
  },
  {
    'items': [79, 60, 97],
    'operation': lambda x: x**2,
    'test': lambda x: 1 if x % 13 == 0 else 3,
    'mod': 13,
    'count': 0
  },
  {
    'items': [74],
    'operation': lambda x: x+3,
    'test': lambda x: 0 if x % 17 == 0 else 1,
    'mod': 17,
    'count': 0
  }
]