import time

# Define a function using a while loop
def using_while():
    i = 0
    while i < 5:
        print(i)
        print("while")
        i += 1

# Define a function using a for loop
def using_for():
    for i in range(5):
        print(i)
        print("for")

# Measure time taken for using_for() execution
start_time = time.time()
using_for()
t1 = time.time() - start_time

# Measure time taken for using_while() execution
start_time = time.time()
using_while()
t2 = time.time() - start_time

# Print the execution times for comparison
print("# Print the execution times for comparison")
print(f"t1 = {t1}s", f"t2 = {t2}s")

# Get and format the current time
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d  %H-%M-%S", current_time)

# Print the formatted time
print(formatted_time)

# Define a dictionary to store formatted time components
formatted_time_dict = {
    "Year": time.strftime("%Y", current_time),
    "Month": time.strftime("%m", current_time),
    "Day": time.strftime("%d", current_time),
    "Hour (24-hour)": time.strftime("%H", current_time),
    "Minute": time.strftime("%M", current_time),
    "Second": time.strftime("%S", current_time),
    "AM/PM": time.strftime("%p", current_time),
    "Hour (12-hour)": time.strftime("%I", current_time)
}

# Print the formatted time components
for label, value in formatted_time_dict.items():
    print(f"{label}: {value}")
