import re

# Meta-characters in regular expressions:
# . (dot) - Matches any character except a newline.
# \d - Matches any digit (0-9).
# \D - Matches any non-digit.
# \w - Matches any alphanumeric character (word character).
# \W - Matches any non-alphanumeric character.
# \s - Matches any whitespace character (space, tab, newline).
# \S - Matches any non-whitespace character.
# ^ - Matches the start of the string.
# $ - Matches the end of the string.
# [...] - Matches any one of the characters inside the brackets.
# [^...] - Matches any character NOT inside the brackets.
# * - Matches 0 or more occurrences of the preceding pattern.
# + - Matches 1 or more occurrences of the preceding pattern.
# ? - Matches 0 or 1 occurrence of the preceding pattern (optional).
# {n} - Matches exactly n occurrences of the preceding pattern.
# {n,} - Matches n or more occurrences of the preceding pattern.
# {n,m} - Matches between n and m occurrences of the preceding pattern.
# | - Alternation, matches either the pattern on the left or the pattern on the right.
# () - Groups patterns together, can be used for capturing and applying quantifiers.

# Example:
# pattern = r'\d+'  # Matches one or more digits.

text = '''He ordered his regular breakfast. Two eggs NNomething sunnyside up, hash browns, and two strips of bacon. 
He continued to look at the menu wondering if this would be the day he added something new. This was also part of the 
routine. A few Aomething seconds of hesitation to see if something  AAomething else would be added to the order 
before demuring and saying that would be all. It was the same exact Something meal that he had ordered every day for 
the past two years.'''
pattern = "he"

# match = re.search(pattern, text)
# print(match)
matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)
matches = re.finditer(pattern, text)
for m in matches:
    print(m.span(), text[m.span()[0]:m.span()[1]])
    # print(type(m), m, m.span())

# pattern = r"[A-za-z]omething"
# matches = re.findall(pattern, text)
# print(matches)
# pattern = r"[A-za-z]+omething"
# matches = re.findall(pattern, text)
# print(matches)
