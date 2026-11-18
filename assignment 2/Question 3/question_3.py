import math
import random
random.seed(2026)
def walsh(n):
    rows = [[1]]
    while len(rows) < n:
        rows = [r + r for r in rows] + [r + [-x for x in r] for r in rows]
    return rows
for length in (8, 16, 64):
    codes = walsh(length)
    cross = sum(a*b for a,b in zip(codes[0], codes[1])) / length
    print(f"L={length}, processing_gain={10*math.log10(length):.2f} dB, cross_corr={cross:.2f}")
    for users in (2, 4, 8):
        errors = 0
        bits = 1000
        for _ in range(bits):
            symbols = [random.choice((-1, 1)) for _ in range(users)]
            chips = [sum(symbols[u]*codes[u][j] for u in range(users)) + random.gauss(0, 1.5)
                     for j in range(length)]
            decision = sum(chips[j]*codes[0][j] for j in range(length))
            errors += (decision * symbols[0] < 0)
        print(f"  users={users}, user0_BER={errors/bits:.4f}")
print("Ideal synchronous orthogonal codes; near-far with misalignment is not simulated.")
