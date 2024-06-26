graph = {
   'A': ['B', 'C', 'F'],
   'B': ['D', 'E'],
   'C': [],
   'D': [],
   'E': [],
   'F': []
}

visited = []

def dfs(graph, start):
   if start not in visited:
      visited.append(start)
   for neighbor in graph[start]:
      if neighbor not in visited:
         dfs(graph, neighbor)

start_node = 'A'
dfs(graph, start_node)

for node, _ in graph.items():
   if node in visited:
      print(node,'was visited')
   else:
      print(node,'was not visited')
      
print('\nOrder of visitation was: ')
[print(node, end=' ') for node in visited]

#Time Complexity: O(b^m), where:
#● b is the branching factor (average number of children per node).
#● m is the maximum depth of the search tree