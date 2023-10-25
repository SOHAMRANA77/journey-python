# Using seek() to set the file pointer and read data from a specific position
# with open("myfile.txt", "r") as f:
#     print(type(f))  # Print the type of file object (IOTextWrapper)
#     f.seek(17)  # Set the file pointer to the 17th byte
#     data = f.read(6)  # Read 6 characters from the specified position
#     print(data)  # Print the read data

# Using seek() and tell() to set the file pointer and get its position
# with open("myfile.txt", "r") as f:
#     f.seek(18)  # Set the file pointer to the 18th byte
#     print(f.tell())  # Print the current file pointer location (byte position)

# Using truncate() to modify the file size
with open("MYfile5", "w") as f:
    f.write("hello,\ni am soham rana OJIWHIUWBFHUIWNWIENFWIOFNIFHEWUFHEPNPIEWOJPWHG")
    f.truncate(18)  # Keep the file length fixed at 18 characters

# Reading and printing the contents of the modified file
with open("MYfile5", "r") as f:
    print(f.read())  # Read and print the contents of the modified file
