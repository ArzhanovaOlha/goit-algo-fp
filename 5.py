import uuid
import heapq
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


class Node:
  def __init__(self, key, color = 'skyblue'):
    self.left = None
    self.right = None
    self.val = key
    self.color = color 
    self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) 
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root,colors):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} 

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()

def build_tree(heap, index = 0):
  if index >= len(heap):
    return None
  node = Node(heap[index])
  left_index = 2 * index + 1
  right_index = 2 * index + 2
  node.left = build_tree(heap, left_index)
  node.right = build_tree(heap, right_index)
  return node

def color_generate(step, total_steps):
  base_color = [135, 206, 250]
  darken = step / (2 * total_steps)
  new_color = [int(c*(0.5+darken)) for c in base_color]
  return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'

def dfs(root, total_steps):
  visited = deque()
  stack = [root]
  colors = {}
  step = 0

  while stack:
    node = stack.pop()
    if node.left:
      stack.append(node.left)
    if node.right:
      stack.append(node.right)
    
    if node not in visited:
        visited.append(node)
        node.color = color_generate(step, total_steps)
        colors.update({ node.id : node.color })
        step += 1

  return colors

def bfs(root, total_steps):
  visited = deque()
  queue = deque()
  queue.append(root)
  colors = {}
  step = 0

  while queue:
      node = queue.popleft()
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
      
      if node not in visited:
        visited.append(node)
        node.color = color_generate(step, total_steps)
        colors.update({ node.id : node.color })
        step += 1

  return colors

def count_nodes(node):
  if node is None:
    return 0
  return 1 + count_nodes(node.left) + count_nodes(node.right)

heap_list  = [1,15,3,5,13,2,7,12,8,10,6,11,14,4,9]
heapq.heapify(heap_list)

heap_tree_root = build_tree(heap_list)
total_steps = count_nodes(heap_tree_root)


dfs_colors = dfs(heap_tree_root, total_steps)
draw_tree(heap_tree_root,dfs_colors)
bfs_colors = bfs(heap_tree_root,total_steps)
draw_tree(heap_tree_root,bfs_colors)