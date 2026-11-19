systems={'Android':'FCM + Doze/background limits','iOS':'APNs + constrained background execution','Windows':'OS notifications + app-model-specific background tasks'}
for system,policy in systems.items(): print(f'{system}: {policy}')
for app_alive in (True,False):
 print(f'app_alive={app_alive}: durable server queue + system push; background callback not guaranteed')
print('Design: TLS, encrypted local state, idempotent fetch after user opens app')
