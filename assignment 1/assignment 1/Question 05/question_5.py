import math
area=12
for r in (0.5,0.35,0.265):
 cells=math.ceil(area/(3*math.sqrt(3)/2*r*r))
 print(f"radius={r:.3f} km, approximate_cells={cells}")
for users in (1000,10000,20000,100000):
 print(f"users={users}, traffic={users*.025:.1f} Erlangs")
