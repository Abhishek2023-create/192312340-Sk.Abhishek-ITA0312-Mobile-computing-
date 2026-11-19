controls={'permissions':'least privilege','tokens':'private encrypted storage','updates':'signature verification','network':'HTTPS/TLS','components':'nonexported unless necessary','logs':'exclude patient records and secrets'}
for asset,control in controls.items(): print(f'{asset}: {control}')
checks={'cleartext_enabled':False,'world_readable_token':False,'unprotected_exported_component':False}
for name,value in checks.items(): print(f'policy {name}={value}: {"FAIL" if value else "PASS"}')
assert not any(checks.values())
print('Static example only; no APK manifest, proxy trace, or physical-device audit')
