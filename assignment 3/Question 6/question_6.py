"""Q6: Simplified AODV-style RREQ/RREP and route failure handling."""
from collections import deque
network = {'S':['A','B'], 'A':['S','D'], 'B':['S','C'], 'C':['B','D'], 'D':['A','C']}
def discover(source, destination):
    queue = deque([(source,[source])]); visited = {source}; rreq = 0
    while queue:
        node, route = queue.popleft(); rreq += 1
        if node == destination: return route, rreq
        for nxt in network[node]:
            if nxt not in visited:
                visited.add(nxt); queue.append((nxt,route+[nxt]))
    return None, rreq
route, requests = discover('S','D')
print(f'RREQ discovery: {requests} processed; RREP path={route}')
network['A'].remove('D'); network['D'].remove('A')
print('Link A-D failed: RERR issued; rediscovering route')
route, requests = discover('S','D')
print(f'New RREQ processed={requests}; RREP path={route}')
print('Simplified BFS demonstration, not full AODV timers/sequence numbers.')
