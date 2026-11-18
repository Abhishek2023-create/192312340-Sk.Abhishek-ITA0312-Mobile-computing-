import math
S=336
for n in (3,4,7,12):
 print(f"N={n}: channels/cell={S//n}, reuse ratio={math.sqrt(3*n):.3f}")
