class Node(object):
  def __init__(self, name, size=None, children={}, parent=None):
    self.name = name
    self.size = size
    self.children = children
    self.parent = parent

  def is_leaf(self):
    return not self.children

  def add_child(self, name, size=None, children=None):
    self.children[name] = Node(name, size, children, parent=self)

  def __str__(self):
    return '- {name} ({type}, {size})'.format(name=self.name, type='file' if self.is_leaf() else 'dir', size=self.size or '') 


def build_tree(root):
  current_node = root

  with open('input.txt') as f:
    for line in f.read().split('\n'):
      cmd = line.split(' ')
      if cmd[0] == '$':
        if cmd[1] == 'cd':
          if cmd[2] == '/':
            current_node = root
          elif cmd[2] == '..':
            current_node = current_node.parent
          else:
            current_node = current_node.children.get(cmd[2])
      
      elif cmd[0] == 'dir':
        current_node.add_child(cmd[1], children={})
      else:
        current_node.add_child(cmd[1], size=int(cmd[0]))


def print_tree(node, indent=''):
  print(indent, node)
  if not node.is_leaf():
    for child in node.children.values():
      print_tree(child, indent+' ')


def compute_size(node, dirs):
  if node.is_leaf():
    return node.size
  else:
    node.size = sum([compute_size(child, dirs) for child in node.children.values()])
    dirs.append(node)
    return node.size



if __name__== '__main__':

  # Build tree
  root = Node('/', children={})
  build_tree(root)
  print_tree(root)

  # Compute sizes
  dirs = []
  compute_size(root, dirs)
  print('\n')
  print('SOLUTION 1', sum([d.size for d in dirs if d.size <=100000]))
  print('SOLUTION 2', sorted([d.size for d in dirs if d.size >= 30000000 - (70000000 - root.size)])[0] )


