import pandas as pd
import json

# Load your Excel file
df = pd.read_excel("crops.xlsx")  # change to the actual file name

# Flatten and clean all values across all columns
crop_set = set()

for col in df.columns:
    crop_set.update(df[col].dropna().astype(str).str.strip())

# Sort alphabetically
sorted_crops = sorted(crop_set)

# Export to JSON file
with open("flat_crops.json", "w") as f:
    json.dump(sorted_crops, f, indent=2)

print("✅ flat_crops.json created with", len(sorted_crops), "unique crop names.")