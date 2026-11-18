"""Q4: Mobile healthcare session continuity during network changes."""
networks = [('Ward Wi-Fi', 30, 0), ('Corridor Wi-Fi', 60, 2), ('Cellular', 95, 4)]
packets_per_step = 100
for network, registration_ms, wireless_losses in networks:
    interval_ms = 1000
    # One packet each 10 ms, with outage during registration.
    handoff_loss = min(packets_per_step, registration_ms // 10)
    delivered = max(0, packets_per_step - handoff_loss - wireless_losses)
    print(f'{network}: registration={registration_ms} ms, delivered={delivered}/{packets_per_step}, PDR={delivered/packets_per_step:.1%}')
print('Use authenticated registration, encryption, retries, and local buffering for real patient data.')
print('These are hypothetical figures, not clinical or field measurements.')
