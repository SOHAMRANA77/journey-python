# String operations in Python

# Printing a greeting using a variable
name = "soham"
print("Hello,", name)

# Printing strings with quotes
print('he said,"i want to eat an apple"')
print("he said,\"i want to eat an apple\"")

# Using triple quotes for multiline strings
a = """learned about strings in Python, which are text sequences enclosed 
in single or double quotes. I discovered how to create multiline 
strings using triple quotes, access characters with indices, and 
iterate through a string's characters using a for loop to perform 
tasks or print them."""
print(a)

# Various string slicing and indexing operations
print(a[0])
print(a[1])
print(a[0:7])
print(a[0:10:2])

# Using a for loop to iterate through characters in a string
print("\nfor loop")
for char in name:
    print(char)

# More string slicing and indexing
allname = "Soham,harry,shubham"
print(allname[:5])
print(allname[0:6])
print(len(allname))
print(allname[6:19])
print(allname[:])
print(allname[0:-14])
print(allname[-19:-14])
print(allname[:])
print(name[-5:-1])
print(name[-5:-2])

# String case transformations and modifications
print(name.upper())
print(name.lower())
print(name.capitalize())
N = "!!soham!! !!Rana!!"
print(N.rstrip("!"))
print(N.replace("soham", "rana"))
print(N.split(" "))
print(N.center(48))
print(N.count("a"))
print(N.endswith("!!"))
print(N.endswith("!!", 0, 9))
print(N.find("n"))
print(N.index("n"))

# String utility functions
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())
str2 = "   "
print(str1.islower())
print(str1.isprintable())  # /n
print(str2.isspace())
print(str1.istitle())
print(str1.startswith("W"))
print(str1.swapcase())
print(name.title())
