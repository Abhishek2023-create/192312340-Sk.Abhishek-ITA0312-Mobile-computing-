import math
import random
import cmath
random.seed(2026)
n, users, trials, snr = 64, 8, 1000, 10.0
inner = sum(cmath.exp(2j*math.pi*(0-1)*i/n) for i in range(n))/n
print(f"subcarrier 0/1 inner product magnitude={abs(inner):.3e}")
def jain(r):
    return sum(r)**2/(len(r)*sum(x*x for x in r)) if sum(r) else 0
results = {name: [0.0, 0.0] for name in ('contiguous','interleaved','best')}
for _ in range(trials):
    gains = [[random.expovariate(1) for _ in range(n)] for _ in range(users)]
    rates = [[math.log2(1+snr*g) for g in row] for row in gains]
    for name in results:
        per_user = [0.0]*users
        for k in range(n):
            u = k//8 if name=='contiguous' else k%users if name=='interleaved' else max(range(users),key=lambda i:rates[i][k])
            per_user[u] += rates[u][k]
        results[name][0] += sum(per_user)/trials
        results[name][1] += jain(per_user)/trials
for name,(rate,fairness) in results.items():
    print(f"{name}: mean_sum_rate={rate:.2f}, mean_Jain={fairness:.3f}")
