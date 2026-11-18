attendees=25000; traffic_per_user=.05; event_area=1
traffic=attendees*traffic_per_user
baseline_density=100000*.025/12
print(f"Event traffic={traffic:.0f} Erlangs")
print(f"Event density={traffic/event_area:.0f} Erlangs/km^2")
print(f"Density ratio={traffic/baseline_density:.1f}x")
print("Recommendation: temporary event cells and sectorisation")
