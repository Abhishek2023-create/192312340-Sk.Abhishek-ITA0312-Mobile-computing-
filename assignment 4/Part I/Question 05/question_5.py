states={'ACTIVE':'UI and bounded foreground work','IDLE':'batch eligible jobs','DOZE':'defer network; system maintenance windows','CHARGING':'perform eligible deferred maintenance'}
for name,work in states.items(): print(f'{name}: {work}')
for battery in (80,25,15,10):
 policy='reduce nonurgent sampling and defer upload' if battery<=15 else 'normal/adaptive work'
 print(f'battery={battery}%: {policy}; urgent alert remains eligible')
print('Illustrative policy, not measured battery drain')
