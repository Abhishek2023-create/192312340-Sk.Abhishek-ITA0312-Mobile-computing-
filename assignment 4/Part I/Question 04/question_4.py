controls={'permission':'request dangerous permission only when needed','token':'encrypt in app-private storage with Keystore-backed key','updates':'verify signing identity and trusted distribution','network':'require HTTPS/TLS with certificate validation'}
for defect,fix in controls.items(): print(f'{defect}: {fix}')
assert len(controls)==4
print('Regression: deny contacts permission -> unrelated note editing still works')
print('STATIC DESIGN CHECK ONLY: no Android app or real secrets were tested')
