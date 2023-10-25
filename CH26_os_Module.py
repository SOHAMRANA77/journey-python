# Import the os module for file system operations
import os

# Directory name
f_n = "100 days of code"

# Check if the directory does not exist, then create it
if not os.path.exists(f_n):
    os.makedirs(f_n)
else:
    print("Directory already exists")

# Create directories for each day from 1 to 100
for i in range(1, 101):
    os.makedirs(os.path.join(f_n, f"DAY{i}"))
