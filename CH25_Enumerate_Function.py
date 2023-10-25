# index = 0
# for mark in marks:
#     print(mark)
#     if index == 5:
#         print("LOL")
#     index +=1

# List of marks
marks = [55, 56, 88, 69, 48, 99, 85, 75, 65, 84, 66]

# Iterate over the list using enumerate to get both index and value
for index, mark in enumerate(marks, start=1):
    # Check if the current index is 6
    if index == 6:
        print("LOL")
    else:
        # Print the index and the corresponding mark
        print(index, mark)

