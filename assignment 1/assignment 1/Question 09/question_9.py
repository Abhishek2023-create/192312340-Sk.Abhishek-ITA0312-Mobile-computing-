import math
def erlang_b(m,a):
 b=1.
 for k in range(1,m+1): b=a*b/(k+a*b)
 return b
for m in (24,48,84):
 for a in (20,40,60):
  print(f"channels={m}, load={a}, blocking={100*erlang_b(m,a):.3f}%")
