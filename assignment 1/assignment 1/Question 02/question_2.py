import math
R=0.5
for n in (4,7,12):
 print(f"N={n}, channels={336//n}, reuse_km={R*math.sqrt(3*n):.3f}")
