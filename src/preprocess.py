import pandas as pd
from utils import get_data_path

# Load raw data
df = pd.read_csv(get_data_path("iris.csv"))

# Example preprocessing: map species to numeric labels
if "species" in df.columns:
    df["target"] = df["species"].astype("category").cat.codes

# Save processed file as iris_processed.csv
df.to_csv(get_data_path("iris_processed.csv"), index=False)

print(f"✅ Data saved to {get_data_path('iris_processed.csv')}")
print(df.head())
