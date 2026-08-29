import pandas as pd
from pathlib import Path

# Get the main project folder
project_dir = Path(__file__).resolve().parent.parent

# Create the correct raw data directory
data_dir = project_dir / "data" / "raw"
data_dir.mkdir(parents=True, exist_ok=True)

# UCI Adult dataset URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

# Column names
columns = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "income"
]

# Download dataset
df = pd.read_csv(
    url,
    names=columns,
    skipinitialspace=True
)

# Save inside our project
output_path = data_dir / "adult.csv"
df.to_csv(output_path, index=False)

print("Dataset downloaded successfully!")
print("Shape:", df.shape)
print("Saved to:", output_path)