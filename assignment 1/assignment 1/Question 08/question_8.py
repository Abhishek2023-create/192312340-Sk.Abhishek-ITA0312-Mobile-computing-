import math
def erlang_b(m,a):
 b=1.0
 for k in range(1,m+1): b=a*b/(k+a*b)
 return b
assert abs(.5*math.sqrt(21)-2.2913)<.001
assert abs(10*math.log10(21**2/6)-18.663)<.01
assert erlang_b(48,0)==0
print("Reuse-distance test: PASS")
print("SIR sanity test: PASS")
print("Erlang-B zero-traffic test: PASS")
