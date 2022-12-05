import re

stacks = {
  '1': ['N','B','D','T','V','G','Z','J'],
  '2': ['S','R','M','D','W','P','F'],
  '3': ['V','C','R','S','Z'],
  '4': ['R','T','J','Z','P','H','G'],
  '5': ['T','C','J','N','D','Z','Q','F'],
  '6': ['N','V','P','W','G','S','F','M'],
  '7': ['G','C','V','B','P','Q'],
  '8': ['Z','B','P','N'],
  '9': ['W','P','J'],
}

with open('input.txt') as f:
  _, instructions = f.read().split('\n\n')

  for line in instructions.split('\n'):
    num, sfrom, sto = re.findall(r'\d+', line)

    for i in range(int(num)):
      stacks[sto].append(stacks[sfrom].pop())

  print(''.join([s[-1] for s in stacks.values()]))