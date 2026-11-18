"""Q7: Emergency ad hoc network connectivity and mobility stress test."""
import random
from collections import deque

def reachable(graph, start, goal):
    todo = deque([start]); seen = {start}
    while todo:
        node = todo.popleft()
        if node == goal: return True
        for nxt in graph[node]:
            if nxt not in seen: seen.add(nxt); todo.append(nxt)
    return False

for count, mobility in ((10,.05),(25,.15),(50,.30)):
    random.seed(3100 + count)
    success = 0; total_edges = 0; trials = 100
    for _ in range(trials):
        # Fixed radio-range abstraction: nearby IDs are potential neighbours.
        graph = {i:[] for i in range(count)}
        for i in range(count):
            for j in range(i+1, min(count,i+4)):
                if random.random() >= mobility:
                    graph[i].append(j); graph[j].append(i); total_edges += 1
        success += reachable(graph, 0, count-1)
    print(f'nodes={count}, link_failure_probability={mobility:.0%}, end_to_end_reachability={success/trials:.1%}, mean_active_links={total_edges/trials:.1f}')
print('Recommended: ad hoc multi-hop routing; gateway/Mobile IP only when infrastructure reachable.')
print('Results are seeded graph simulations, not real AODV/DSDV measurements.')
