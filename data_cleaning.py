import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("../dataset/healthcare_data.csv")

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Show column names
print("\nColumn Names:")
print(df.columns)

# Dataset information
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Total rows after cleaning
print("\nTotal Rows After Removing Duplicates:")
print(df.shape)

# Save cleaned dataset
df.to_csv("../dataset/cleaned_healthcare_data.csv", index=False)

print("\nCleaned dataset saved successfully.")