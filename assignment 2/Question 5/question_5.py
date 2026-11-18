import math
def af(elements, angle_deg):
    psi = math.pi*math.sin(math.radians(angle_deg))
    if abs(psi)<1e-12: return 1.0
    return abs(math.sin(elements*psi/2)/(elements*math.sin(psi/2)))
for n in (2,4,8,16):
    first = None
    for angle in range(5,61):
        response = max(af(n,angle),1e-12)
        sir = -20*math.log10(response)
        if sir >= 10:
            first = angle
            break
    print(f"N={n}, first_sampled_separation_at_10dB={first} degrees, "
          f"SIR_at_30deg={-20*math.log10(max(af(n,30),1e-12)):.2f} dB")
print("Ideal broadside half-wavelength array, one equal-power interferer.")
