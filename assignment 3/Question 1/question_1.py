"""Q1: Simplified two-access-point mobility and packet delivery model."""
import random
random.seed(31)
for speed in (1, 3, 6):
    handoffs = delivered = lost = 0
    attachment = 'A'
    for t in range(120):
        location = (t * speed) % 100
        target = 'A' if location < 50 else 'B'
        if target != attachment:
            handoffs += 1
            attachment = target
            lost += 1  # one packet lost during modeled handoff
        elif random.random() < 0.02:
            lost += 1  # independent wireless loss
        else:
            delivered += 1
    print(f'speed={speed}, handoffs={handoffs}, delivered={delivered}, lost={lost}, PDR={delivered/120:.2%}')
print('Illustrative handoff model; not measured network data.')
