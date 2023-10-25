# change the directory
# os.chdir("\\Users")
# print(os.getcwd())
# Import the os module for file system operations
import os

print(os.getcwd())
# List the contents of the "100 days of code" directory
folder = os.listdir("100 days of code")

# Print the current working directory
print(os.getcwd())

# Iterate through each folder in the "100 days of code" directory
for folder_name in folder:
    # Check if the folder is empty (contains no files or subdirectories)
    if not os.listdir(f"100 days of code\\{folder_name}"):
        print(f"The folder '{folder_name}' is empty.")

