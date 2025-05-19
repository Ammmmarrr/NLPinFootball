import pandas as pd
import re

# Load commentary and heatmap data
comments = pd.read_csv("commentary.csv")
zones = pd.read_csv("heatmap_data.csv")
zone_coverage = dict(zip(zones["zone"], zones["coverage"]))

# Rules to catch tactical patterns
patterns = {
    "right_defence": [
        "vinicius.*left", "alexander.*isolated", "left flank", "taa.*caught"
    ],
    "central_midfield": [
        "midfield.*stretched", "modric.*central", "fabinho.*isolated", "press too high"
    ],
    "left_defence": [
        "robertson.*high", "no support on left", "overload on right", "diaz.*not tracking"
    ]
}

suggestions = {
    "right_defence": "Bring support to the right-back zone.",
    "central_midfield": "Midfield looks outnumbered. Add cover.",
    "left_defence": "Tell winger to track back and support left-back."
}

results = []

for line in comments["text"]:
    text = line.lower()
    for zone, triggers in patterns.items():
        for phrase in triggers:
            if re.search(phrase, text):
                if zone_coverage.get(zone, 1) == 0:
                    results.append((line, zone, suggestions.get(zone)))

# Output to file
with open("output.txt", "w") as f:
    for original, zone, tip in results:
        f.write(f"- COMMENT: {original}\n")
        f.write(f"  ISSUE DETECTED: {zone}\n")
        f.write(f"  SUGGESTION: {tip}\n\n")

print("Done. Check output.txt for basic suggestions.")
