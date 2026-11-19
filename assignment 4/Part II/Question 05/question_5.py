import math
# Illustrative relative energy units; not actual mAh or device readings.
for mode,wakeups,radio_activations,cpu_factor in [('continuous',120,120,1.0),('batched',12,12,0.8),('idle/deferred',3,3,0.6)]:
 energy=0.04*wakeups+0.3*radio_activations+2*cpu_factor
 print(f'{mode}: wakeups={wakeups}, radio_sessions={radio_activations}, relative_energy={energy:.2f}')
print('Use adb batterystats/Perfetto on a device for real Doze, DVFS, and wakelock evidence.')
