# def swapNumber(a: int, b: int) -> tuple:
#     a = a ^ b
#     b = a ^ b
#     a = a ^ b
#     return a, b
#
# a, b = input("Enter two integers separated by space: ").split()
# a = int(a)
# b = int(b)
# swapped_a, swapped_b = swapNumber(a, b)
# print("Swapped values:", swapped_a, swapped_b)
def swap_number(a: int, b: int) -> None:
    a = a ^ b  # XOR operation to swap a and b
    b = a ^ b
    a = a ^ b
    print(a, b)  # Print the swapped values


a, b = input("Enter two integers separated by space: ").split()  # Take user input for two integers
a = int(a)  # Convert to integer
b = int(b)  # Convert to integer
swap_number(a, b)  # Call the function to swap the numbers


""""
a = 6
b = 7
print(a, b)
c = a
a = b
b = c
print(a, b)
"""
