# String formatting in Python

# Using string formatting with placeholders and .format()
letter = "As a {0}, I'm passionate about {1}. I reside in {2}."
profession = "Software developer"
interest = "Python Language"
location = "Vadodara"
print(letter.format(profession, interest, location))

# Using f-strings for string formatting
print(f"As a {profession}, I'm passionate about {interest}. I reside in {location}.")

# Using f-strings to show literal curly braces
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

# Using f-strings with precision for a floating-point number
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)

# Checking the type of an f-string
print(type(f"{2 * 30}"))
