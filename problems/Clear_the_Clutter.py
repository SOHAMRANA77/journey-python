"""
Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png
images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file
formats. For example:

sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png
design.png --> 4.png
name.png --> 5.png
"""
"""
# import os
#
# dot_prod = input("Enter File Type")
import os
from collections import Counter


def count_file_types(folder_path):
    file_types = Counter()

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            _, exte_nsion = os.path.splitext(file)
            file_types[exte_nsion] += 1

    return file_types


if __name__ == "__main__":
    folder_path = "C:\\Users\\soham\\OneDrive\\Pictures\\New folder"  # Replace with the actual folder path
    file_types_count = count_file_types(folder_path)

    print("File types and their counts:")
    for extension, count in file_types_count.items():
        print(f"{extension}: {count}")
"""

import os
import shutil


def move_files_by_extension(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Get the file extension
            _, extension = os.path.splitext(file)

            # Create the destination folder if it doesn't exist
            dest_folder = os.path.join(destination_folder, extension[1:])
            os.makedirs(dest_folder, exist_ok=True)

            # Move the file to the respective folder based on its extension
            shutil.move(os.path.join(root, file), os.path.join(dest_folder, file))


if __name__ == "__main__":
    # Replace with the actual source and destination folder paths
    source_folder = "C:\\Users\\soham\\OneDrive\\Pictures\\Camera Roll\\Sohyem (@sohyem_rana) • Instagram photos and " \
                    "videos_files"
    destination_folder = "C:\\Users\\soham\\OneDrive\\Pictures\\Camera Roll\\photo"

    # Move files based on their extensions
    move_files_by_extension(source_folder, destination_folder)
