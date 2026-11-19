def decide(battery,network,motion,charging=False):
 if motion=='EMERGENCY': return '2s','priority upload when connected' if network!='OFFLINE' else 'encrypted queue'
 if network=='OFFLINE': return '30s','encrypted queue'
 if charging and network=='WIFI': return '5s','upload queued batch'
 if battery<15: return '300s','emergency-only upload'
 if battery<=30 and motion=='STATIONARY': return '120s','defer until queue/age threshold'
 if network=='WIFI' and motion=='MOVING': return '10s','batch every 2min'
 if network=='LTE' and motion=='MOVING': return '15s','batch every 5min'
 return '60s','scheduled batch'
cases=[(80,'WIFI','MOVING',False),(70,'LTE','MOVING',False),(20,'LTE','STATIONARY',False),(10,'LTE','STATIONARY',False),(90,'WIFI','STATIONARY',True),(50,'OFFLINE','MOVING',False),(8,'LTE','EMERGENCY',False)]
for args in cases:
 print(f'{args} -> sample={decide(*args)[0]}, action={decide(*args)[1]}')
assert decide(8,'LTE','EMERGENCY')[0]=='2s'
print('Policy simulation only; not measured phone energy or patient records')
