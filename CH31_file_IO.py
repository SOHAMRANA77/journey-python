"""
There are various modes in which we can open files.

read (r): This mode opens the file for reading only and
gives an error if the file does not exist. This is the default mode
if no mode is passed as a parameter.

create (x): This mode creates a file and gives an error if the file
already exists.

text (t): Apart from these modes we also need to specify how the file
must be handled. t mode is used to handle text files. t refers to the text
mode. There is no difference between r and rt or w and wt since text mode is
the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

binary (b): used to handle binary files (images, pdfs, etc).
"""
# Explanation of file handling modes and examples

# Reading from a file
F = open("myfile.txt", 'r')  # Open the file in read mode
print(F)
text = F.read()  # Read the content of the file
print(text)
F.close()  # Close the file

# Writing to a file
F = open("myfile.txt", 'w')  # Open the file in write mode (creates a new file if it doesn't exist)
F.write("Author is ChatGPT")  # Write content to the file
F.close()  # Close the file

# Appending to a file
F = open("myfile.txt", 'a')  # Open the file in append mode (creates a new file if it doesn't exist)
F.write("\nHello")  # Append content to the file
F.close()  # Close the file

# Appending to a file using 'with' statement (automatically closes the file)
with open("myfile.txt", 'a') as F:
    F.write("\nWithout F.close()")  # Append content to the file using 'with' statement
