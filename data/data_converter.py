import pandas as pd

# Define column names as per NASA CMAPSS spec
cols = ['unit', 'cycle'] + [f'op_set{i}' for i in range(1, 4)] + [f'sensor{i}' for i in range(1, 22)]

# Load and convert
df = pd.read_csv('data/train_FD001.txt', sep='\s+', header=None)
df.columns = cols

# Save as CSV
df.to_csv('data/train_FD001.csv', index=False)
print("Conversion complete ✅")

