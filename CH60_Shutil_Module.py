import os
import shutil

# Copies a file from the source to the destination
shutil.copy(src="lines.txt", dst="lines1.txt")

# Copies a file from the source to the destination while preserving metadata
shutil.copy2(src="lines.txt", dst="lines2.txt")

# Recursively copies an entire directory from the source to the destination
shutil.copytree(src="Photos", dst="myphotos")

# Moves a file or directory from the source location to the destination location
shutil.move("100 days of code/DAy - 10/soham", "100 days of code/DAy - 11/soham")

# Removes a directory and its contents recursively
shutil.rmtree("myphotos")

# Removes a file
os.remove("lines2.txt")
