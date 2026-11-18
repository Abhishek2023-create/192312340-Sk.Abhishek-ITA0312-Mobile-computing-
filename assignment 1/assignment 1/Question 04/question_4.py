import math
n=7
for exponent in (2.5,3.2,4):
 sir=10*math.log10((3*n)**(exponent/2)/6)
 print(f"path_loss={exponent}, cell_edge_SIR={sir:.2f} dB")
print("Best: near base station; worst: obstructed cell edge")
