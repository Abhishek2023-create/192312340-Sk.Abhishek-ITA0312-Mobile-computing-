import math
area=12; radius=.5; channels=336; cluster=7
cells=math.ceil(area/(3*math.sqrt(3)/2*radius**2))
print(f"Macro reuse N={cluster}")
print(f"Initial cells={cells}, channels/cell={channels//cluster}")
print("Recommended: sectorisation + dynamic assignment + selective microcells")
