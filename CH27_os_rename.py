# Import the os module for file system operations
import os

# Rename directories for each day from 1 to 100
for i in range(1, 101):
    old_name = f"100 days of code//DAY{i}"
    new_name = f"100 days of code//DAy - {i}"
    os.rename(old_name, new_name)
