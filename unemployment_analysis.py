   
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("unemployment.csv")

# Clean column names (remove spaces)
df.columns = df.columns.str.strip()

# Clean Date column (remove \t and spaces)
df['Date'] = df['Date'].astype(str).str.replace(r'\t', '', regex=True).str.strip()

# Convert to datetime (auto detect format)
df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)

# Remove unwanted columns (like Unnamed)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

print(df.head())

# Plot graph
plt.figure(figsize=(10,5))
sns.lineplot(x='Date', y='Unemployment Rate', data=df)

plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate")

plt.show()