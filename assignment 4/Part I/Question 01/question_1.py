layers=['Hardware','Linux kernel and drivers','Hardware abstraction layer','Native libraries and services','Android Runtime (ART)','Application framework','Applications']
for i,layer in enumerate(layers,1): print(f'{i}. {layer}')
print('API request: App -> Framework -> Binder -> System service -> HAL/kernel')
print('Security: UID sandbox, SELinux, runtime permissions; power: PowerManager + kernel')
