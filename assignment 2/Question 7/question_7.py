import math
import random
random.seed(2026)
users, subcarriers, trials, snr = 8,64,1000,10.0
min_share = subcarriers//(2*users)
def jain(r):
    return sum(r)**2/(len(r)*sum(x*x for x in r))
def evaluate(gains, guaranteed):
    rates = [[math.log2(1+snr*g) for g in row] for row in gains]
    assigned = [-1]*subcarriers
    if guaranteed:
        # Stage 1: round-robin guaranteed allocation, one unassigned carrier at a time.
        for k in range(users*min_share): assigned[k] = k%users
    for k in range(subcarriers):
        if assigned[k]<0: assigned[k]=max(range(users),key=lambda u:rates[u][k])
    user_rates=[0.0]*users
    counts=[0]*users
    for k,u in enumerate(assigned):
        user_rates[u]+=rates[u][k]
        counts[u]+=1
    return sum(user_rates),min(user_rates),jain(user_rates),sum(c==0 for c in counts),min(counts)
metrics = [[0.0]*5 for _ in range(2)]
for _ in range(trials):
    gains=[[random.expovariate(1) for _ in range(subcarriers)] for _ in range(users)]
    for policy in (0,1):
        result=evaluate(gains,policy==1)
        for j,value in enumerate(result): metrics[policy][j]+=value/trials
for name,row in zip(('best-subcarrier','minimum-share'),metrics):
    print(f"{name}: sum_rate={row[0]:.2f}, min_rate={row[1]:.2f}, "
          f"Jain={row[2]:.3f}, zero_users={row[3]:.3f}, min_alloc={row[4]:.1f}")
print(f"minimum guaranteed carriers per user={min_share}; paired trials={trials}")
