"""Q2: Simplified Mobile IPv4 registration, tunnelling, and handoff overhead."""
HOME = '10.0.0.7'
care_of = ['172.16.1.7', '172.16.2.7', '172.16.3.7']
packet_bytes = 1000
ipip_header_bytes = 20  # illustrative IPv4-in-IPv4 header
for step, coa in enumerate(care_of, 1):
    registration_ms = 40 + 10 * step
    tunnel_bytes = packet_bytes + ipip_header_bytes
    print(f'move={step}: MN home={HOME}, HA binding={coa}, registration={registration_ms} ms')
    print(f'  CN -> HA -> tunnel({coa}) -> MN; packet={tunnel_bytes} B; overhead={ipip_header_bytes/tunnel_bytes:.2%}')
print('Agent registration and forwarding are logical examples, not real IP packets.')
