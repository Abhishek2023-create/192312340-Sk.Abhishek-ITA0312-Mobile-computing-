import math
def erlang_b(m,a):
 b=1.0
 for k in range(1,m+1): b=a*b/(k+a*b)
 return b
def capacity(m):
 lo,hi=0.,float(2*m)
 for _ in range(70):
  mid=(lo+hi)/2
  if erlang_b(m,mid)>0.02: hi=mid
  else: lo=mid
 return (lo+hi)/2
for n in (4,7):
 m=336//n
 sir=10*math.log10((3*n)**2/6)
 print(f"N={n}, channels={m}, traffic={capacity(m):.2f} Erlangs, SIR={sir:.2f} dB")
