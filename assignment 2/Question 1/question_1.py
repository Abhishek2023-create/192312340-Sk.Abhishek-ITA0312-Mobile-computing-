import random
random.seed(2026)
for availability in (0.9, 0.6, 0.3):
    immediate = delivered = pending = total_delay = 0
    queue = []
    for t in range(1000):
        queue.append(t)
        online = random.random() < availability
        immediate += int(online)
        if online:
            total_delay += sum(t - arrival for arrival in queue)
            delivered += len(queue)
            queue.clear()
    print(f"availability={availability:.0%}, immediate={immediate}, "
          f"queued_delivered={delivered}, pending={len(queue)}, "
          f"mean_queue_delay={total_delay / delivered:.2f} intervals")
