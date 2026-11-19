cold=['create process','initialize ART','load classes','create Application','create Activity','inflate UI','first frame']
warm=['reuse live process and ART','resume or create Activity','render frame']
for name,steps in [('cold',cold),('warm',warm)]:
 print(name.upper(), '->', ' -> '.join(steps))
print('If process was killed, the next launch is cold even after recent use.')
