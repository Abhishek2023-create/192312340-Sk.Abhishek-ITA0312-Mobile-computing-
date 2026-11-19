import uuid
server={};pending=[]
for seq in range(1,6): pending.append({'id':str(uuid.uuid5(uuid.NAMESPACE_DNS,f'ruralcare-{seq}')),'seq':seq,'payload':f'test-{seq}'})
for record in pending:
 server.setdefault(record['id'],record)
print(f'first upload: {len(server)} distinct synthetic records')
for record in pending: server.setdefault(record['id'],record)
print(f'retry after lost acknowledgement: {len(server)} records (no duplicates)')
assert len(server)==len(pending)
print('Production requires authenticated encryption, TLS, secure keys and durable transactions; none implemented here')
