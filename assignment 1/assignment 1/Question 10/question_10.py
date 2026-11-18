import math,random
random.seed(42)
n=7; exponent=4
sir_theory=10*math.log10((3*n)**(exponent/2)/6)
# Demonstration: vary interferer distances by 10% around nominal D.
q=math.sqrt(3*n)
samples=[]
for _ in range(1000):
 distances=[q*random.uniform(.9,1.1) for _ in range(6)]
 samples.append(10*math.log10(1/sum(d**(-exponent) for d in distances)))
print(f"analytical_SIR={sir_theory:.2f} dB")
print(f"simulated_mean_SIR={sum(samples)/len(samples):.2f} dB")
print("Monte Carlo trials=1000, seed=42")
