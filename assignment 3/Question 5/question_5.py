"""Q5: Demonstrate sequence-number-aware DSDV-style route selection."""
route = {'destination':'D', 'next_hop':'B', 'hops':2, 'sequence':16}
updates = [
    {'next_hop':'C','hops':2,'sequence':16},
    {'next_hop':'C','hops':3,'sequence':18},
    {'next_hop':'B','hops':1,'sequence':16},
    {'next_hop':'C','hops':2,'sequence':20},
]
print('Initial route:', route)
for update in updates:
    fresh = update['sequence'] > route['sequence']
    shorter = update['sequence'] == route['sequence'] and update['hops'] < route['hops']
    if fresh or shorter: route.update(update); action = 'ACCEPT'
    else: action = 'IGNORE'
    print(f'{action}: {update} => next_hop={route["next_hop"]}, hops={route["hops"]}, seq={route["sequence"]}')
for nodes in (10, 25, 50):
    print(f'nodes={nodes}, illustrative periodic broadcasts per round={nodes}')
print('This is a route-update example, not a complete DSDV protocol.')
