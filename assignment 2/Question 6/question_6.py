weights = {'spectral':.25,'bursty':.20,'interference':.20,'mobility':.20,'simplicity':.15}
# The source provides one overall rating per technique/deployment, not five criterion ratings.
# Preserve those ratings; do not invent a per-criterion matrix.
ratings = {
    'wide-area voice': {'SDMA':3,'TDMA':4,'FDMA':4,'CDMA':4,'OFDMA':4},
    'tactical link': {'SDMA':2,'TDMA':2,'FDMA':2,'CDMA':5,'OFDMA':3},
    'stadium downlink': {'SDMA':4,'TDMA':2,'FDMA':2,'CDMA':3,'OFDMA':5},
    '5000 sensors': {'SDMA':2,'TDMA':4,'FDMA':2,'CDMA':4,'OFDMA':3},
}
print('Criteria weights:',weights)
for scenario,scores in ratings.items():
    best = max(scores.values())
    winners = [tech for tech,score in scores.items() if score==best]
    print(f"{scenario}: highest overall rating={best}, candidates={', '.join(winners)}")
print('Criterion-weighted sensitivity cannot be computed without criterion-level scores.')
