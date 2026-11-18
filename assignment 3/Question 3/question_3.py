"""Q3: Compare cellular infrastructure and ad hoc multi-hop connectivity."""
from collections import deque

def path(graph, source, target):
    todo = deque([(source, [source])]); visited = {source}
    while todo:
        node, route = todo.popleft()
        if node == target: return route
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor); todo.append((neighbor, route + [neighbor]))
    return None

cellular = {'A':['BS1'], 'BS1':['A','CORE'], 'CORE':['BS1','BS2'], 'BS2':['CORE','D'], 'D':['BS2']}
adhoc = {'A':['B'], 'B':['A','C'], 'C':['B','D'], 'D':['C']}
for name, graph in [('cellular', cellular), ('ad hoc', adhoc)]:
    print(f'{name} route A->D: {path(graph, "A", "D")}')
adhoc['B'].remove('C'); adhoc['C'].remove('B')
print(f'ad hoc after B-C failure: {path(adhoc, "A", "D")}')
print('Topology illustrates infrastructure dependence and multi-hop failure.')
