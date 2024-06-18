# File path: scripts/feature_engineering.py

import pandas as pd

# Load the dataset
train_df = pd.read_csv("../data/train_cleaned.csv")
test_df = pd.read_csv("../data/test_cleaned.csv")

# Feature engineering: Create new features
train_df["Temperature_Diff"] = (
    train_df["Process temperature [K]"] - train_df["Air temperature [K]"]
)
test_df["Temperature_Diff"] = (
    test_df["Process temperature [K]"] - test_df["Air temperature [K]"]
)

# Save the feature-engineered data
train_df.to_csv("../data/train_features.csv", index=False)
test_df.to_csv("../data/test_features.csv", index=False)
