import csv
from datetime import datetime, timedelta
from collections import defaultdict

# Read the CSV file into a list of dictionaries
with open('phonebook.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    data = list(reader)
# Create a table from the data
table = []
for row in data:
    table.append([row['From Mobile'], row[' To Mobile'], row['Call Duration']])

# Print the table to the console
print("PHONE BOOK TABLE")
print("From Mobile\tTo Mobile\tCall Duration")
for row in table:
    print("{}\t{}\t{}".format(row[0], row[1], row[2]))

# Find the distinct numbers from "From Mobile and To Mobile"
numbers = set()
for row in data:
    numbers.add(row['From Mobile'])
    numbers.add(row[' To Mobile'])

print("\nDistinct Numbers:\n {}".format(numbers))

# Find the distinct numbers who used the Free Plan (Call Duration less than 1 min)
free_numbers = set()
for row in data:
    duration = row['Call Duration']
    hours, minutes, seconds = duration.split(':')
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    if total_seconds < 60:
        free_numbers.add(row['From Mobile'])
        free_numbers.add(row[' To Mobile'])

print("\nDistinct Free Numbers:\n {}".format(free_numbers))

# Find the total call duration with respect to From Mobile and To Mobile
duration = {}
for row in data:
    key = (row['From Mobile'], row[' To Mobile'])
    value = row['Call Duration']
    if key in duration:
        duration[key] += value
    else:
        duration[key] = value
# Find the total call duration with respect to From Number
print("\nTotal Call Duration:")
# Define a dictionary to store the call times for each phone number
call_times = defaultdict(timedelta)

# Open the CSV file and read it into a dictionary
with open('phonebook.csv') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['From Mobile', ' To Mobile', 'Call Duration'])
    next(reader)  # Skip header row
    for row in reader:
        # Parse the call duration into a timedelta object
        call_duration = datetime.strptime(row['Call Duration'], '%H:%M:%S') - datetime(1900, 1, 1)
        # Add the call duration to the call times for the 'From Mobile' number
        call_times[row['From Mobile']] += call_duration
        call_times[row[' To Mobile']] += call_duration

# Print the results in a table format
for number, time in call_times.items():
    print("{:<15} {:<15}".format(number, str(time)))

# Find duplicate numbers and merge their call times
duplicates = set()
unique_numbers = set()

for number in call_times:
    if number in unique_numbers:
        duplicates.add(number)
    else:
        unique_numbers.add(number)

merged_call_times = defaultdict(timedelta)

for number, time in call_times.items():
    if number in duplicates:
        merged_call_times[number] += time
    else:
        merged_call_times[number] = time

# Print the merged results in a table format
print("\n{:<15} {:<15}".format("Number", "Call Time"))


# Find the total income for a day (Cost to be considered for Call Duration greater 1 min)
income = 0.0
for row in data:
    duration = row['Call Duration']
    hours, minutes, seconds = duration.split(':')
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    if total_seconds > 60:
        cost = (total_seconds / 60) * 0.3
        income += cost

print("\nTotal Income: ₹{:.2f}".format(income))
