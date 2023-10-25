print("Decorators")

# Decorator function
def greet(fx):
    def mfx(*args, **kwargs):
        print("\nGood Morning")
        fx(*args, **kwargs)  # Calls the original function
        print("Thanks for using this Function")

    return mfx

# Function decorated with 'greet'
@greet
def Hello():
    print("Hello")

# Function decorated with 'greet'
@greet
def mul(a, b):
    print(a + b)

# Calls the decorated function 'Hello'
Hello()
# Output:
# Good Morning
# Hello
# Thanks for using this Function

# Calls the decorated function 'mul'
mul(2, 1)
# Output:
# Good Morning
# 3
# Thanks for using this Function
