import networkx as nx
import matplotlib.pyplot as plt
import heapq

def dijkstra(graph, start):
  distances = {node : float('infinity') for node in graph}
  distances[start] = 0
  queue = [ (0, start) ]
  while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
  return distances



G = nx.Graph()
G.add_edge('A', 'B', weight = 4)
G.add_edge('A', 'C', weight = 2)
G.add_edge('B', 'C', weight = 5)
G.add_edge('B', 'D', weight = 10)
G.add_edge('C', 'E', weight = 3)
G.add_edge('E', 'D', weight = 4)
G.add_edge('D', 'F', weight = 11)

distances = dijkstra(G, 'A')
print(distances)

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()