# NLPinFootball

# Tactical Suggestions from Commentary 

This is a lightweight Python script that checks football commentary for signs of tactical problems, using basic pattern matching and zone coverage data. It's meant to show how even simple text rules can help highlight issues during a match.

## What's Inside

- main.py - main logic to process commentary
- commentary.csv - sample match events (manually curated)
- heatmap_data.csv - fake zone coverage values (0 = weak)
- output.txt - result of the analysis

## How to Run

1. Make sure you have Python and pandas installed.
2. Run main.py.
3. Open `output.txt` to see which areas were flagged and what the suggestion was.
