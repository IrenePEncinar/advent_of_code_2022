monkeys = [
  {
    'items': [50, 70, 89, 75, 66, 66],
    'operation': lambda x: x*5,
    'test': lambda x: 2 if x % 2 == 0 else 1,
    'mod': 2,
    'count': 0
  },
  {
    'items': [85],
    'operation': lambda x: x**2,
    'test': lambda x: 3 if x % 7 == 0 else 6,
    'mod': 7,
    'count': 0
  },
  {
    'items': [66, 51, 71, 76, 58, 55, 58, 60],
    'operation': lambda x: x+1,
    'test': lambda x: 1 if x % 13 == 0 else 3,
    'mod': 13,
    'count': 0
  },
  {
    'items': [79, 52, 55, 51],
    'operation': lambda x: x+6,
    'test': lambda x: 6 if x % 3 == 0 else 4,
    'mod': 3,
    'count': 0
  },
  {
    'items': [69, 92],
    'operation': lambda x: x*17,
    'test': lambda x: 7 if x % 19 == 0 else 5,
    'mod': 19,
    'count': 0
  },
  {
    'items': [71, 76, 73, 98, 67, 79, 99],
    'operation': lambda x: x+8,
    'test': lambda x: 0 if x % 5 == 0 else 2,
    'mod': 5,
    'count': 0
  },
  {
    'items': [82, 76, 69, 69, 57],
    'operation': lambda x: x+7,
    'test': lambda x: 7 if x % 11 == 0 else 4,
    'mod': 11,
    'count': 0
  },
  {
    'items': [65, 79, 86],
    'operation': lambda x: x+5,
    'test': lambda x: 5 if x % 17 == 0 else 0,
    'mod': 17,
    'count': 0
  }
]