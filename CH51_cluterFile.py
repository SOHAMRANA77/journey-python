import os

# Rename files in the "Photos" directory
# os.rename("photos", "Photos")  # This line renames the directory "photos" to "Photos"

# List all files in the "Photos" directory
Files = os.listdir("Photos")

i = 1  # Initialize a counter for renaming files
for File in Files:
    # Check if the file has a ".png" extension
    if File.endswith(".png"):
        print(File)  # Print the original file name

        # Rename the file using a numeric index and ".png" extension
        os.rename(f"Photos/{File}", f"Photos/pngegg{i}.png")

        i += 1  # Increment the counter for the next file
