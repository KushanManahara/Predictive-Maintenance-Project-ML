# File path: scripts/preprocess.py

import pandas as pd

# Load the dataset
train_df = pd.read_csv("../data/train.csv")
test_df = pd.read_csv("../data/test.csv")


# handle missing values
train_df.fillna(method="ffill", inplace=True)
test_df.fillna(method="ffill", inplace=True)


# Convert 'Product ID' and 'Type' to categorical numeric values
train_df["Product ID"] = train_df["Product ID"].astype("category").cat.codes
train_df["Type"] = train_df["Type"].astype("category").cat.codes

test_df["Product ID"] = test_df["Product ID"].astype("category").cat.codes
test_df["Type"] = test_df["Type"].astype("category").cat.codes


# save the prerocessed dataset
train_df.to_csv("../data/train_cleaned.csv", index=False)
test_df.to_csv("../data/test_cleaned.csv", index=False)
