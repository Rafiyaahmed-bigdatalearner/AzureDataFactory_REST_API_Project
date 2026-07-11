import pandas as pd

# Read raw data from Blob output
df = pd.read_csv("users.txt")

# Remove spaces
df["email"] = df["email"].str.strip()

df["first_name"] = df["first_name"].str.strip()

# Standardize email
df["email"] = df["email"].str.lower()

# Format name
df["first_name"] = df["first_name"].str.title()

# Remove duplicates
df = df.drop_duplicates()

# Add audit columns
df["source_system"] = "ReqRes API"
df["load_date"] = pd.Timestamp.now()

# Save cleaned data
df.to_csv("clean_users.csv", index=False)
