band_khz = 2000
fdma_channels = band_khz // 25
tdma_carriers = band_khz // 200
slots = tdma_carriers * 8
print(f"FDMA: {fdma_channels} channels, payload equivalent {fdma_channels * 21} kHz")
print(f"TDMA: {slots} nominal slots, {slots * .90:.1f} usable slot-equivalents")
for duty in (1.0, .1, .7):
    print(f"duty={duty:.0%}, dedicated FDMA utilisation={duty:.0%}, "
          f"scheduled TDMA active-time fraction={duty:.0%}")
print("The TDMA model assumes released slots can serve other users.")
