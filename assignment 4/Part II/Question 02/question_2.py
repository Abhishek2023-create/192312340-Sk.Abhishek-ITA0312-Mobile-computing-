import json,time,concurrent.futures,statistics
payload=json.dumps({'items':[{'id':i,'value':i*i} for i in range(20000)]})
def work(): return sum(item['value'] for item in json.loads(payload)['items'])
main=[];worker=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
 for _ in range(5):
  t=time.perf_counter(); a=work(); main.append((time.perf_counter()-t)*1000)
  t=time.perf_counter(); b=pool.submit(work).result(); worker.append((time.perf_counter()-t)*1000)
  assert a==b
print(f'main median={statistics.median(main):.2f} ms; worker median={statistics.median(worker):.2f} ms')
print('Python timing is NOT an Android UI-frame, PSS, or CPU Profiler measurement.')
