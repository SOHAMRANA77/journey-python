# a = input("enter the number for multiplication chart :\t")
# b = input("enter the number for range :\t")
#
# try:
#     for i in range(1,int(b)+1):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print(e)
# finally:
#     print("i am always executed")
# Function to generate a multiplication chart
def maat():
    n = input("Enter the number for the multiplication chart: ")
    b = input("Enter the number for the range: ")
    try:
        for i in range(1, int(b) + 1):
            print(f"{int(n)} X {i} = {int(n) * i}")
    except Exception as e:
        print(e)
        return 1
    finally:
        print("This block is always executed")
        return "Y"


# Calling the function and capturing the return value
a = maat()

# Printing the return value from the function
print("Return value from function:", a)

