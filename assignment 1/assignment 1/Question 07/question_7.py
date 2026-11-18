import math
initial_cells=19
initial_capacity=729.4
demand=2500
rounds=max(0,math.ceil(math.log(demand/initial_capacity,4)))
print(f"minimum_rounds={rounds}")
print(f"cells={initial_cells*4**rounds}")
print(f"capacity={initial_capacity*4**rounds:.1f} Erlangs")
