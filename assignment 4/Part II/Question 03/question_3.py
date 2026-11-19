import time,statistics,gc

def primes(n):
 return sum(all(i%d for d in range(2,int(i**.5)+1)) for i in range(2,n))
def allocate(n):
 data=[{'x':i,'text':str(i)} for i in range(n)]
 return len(data)
for name,fn in [('cpu primes',lambda:primes(5000)),('allocation',lambda:allocate(10000))]:
 samples=[]
 for _ in range(5):
  start=time.perf_counter(); result=fn(); samples.append((time.perf_counter()-start)*1000)
 print(f'{name}: result={result}; median={statistics.median(samples):.2f} ms')
 gc.collect()
print('Python-only workload benchmark: not ART JIT/AOT, Android GC, or scrolling evidence')
