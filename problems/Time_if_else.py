import time
timestamp = time.strftime('%H:%M:%S')
hourstamp = int(time.strftime('%H'))
# hourstamp = int(input())
mintamp = int(time.strftime('%M'))
sectamp = int(time.strftime('%S'))
print(timestamp)
print(hourstamp)
print(mintamp)
print(sectamp)


# Print the current time
print(f"Current time: {hourstamp:02}:{mintamp:02}:{sectamp:02}")

if 5 <= hourstamp <= 11:
    print("Good Morning")
elif 11 < hourstamp <= 18:
    print("Good Afternoon")
elif 18 < hourstamp <= 22:
    print("Good Evening")
elif hourstamp == 0 and mintamp == 0:
    print("Midnight")
else:
    print("Good night")
"""

import time

def start_timer(timer_name, duration):
    print(f"Timer for {timer_name} is running for {duration} minutes.")
    time.sleep(duration * 60 * 60)
    print(f"{timer_name} timer is done!")

def main():
    total_duration = float(input("Enter the total duration you want to work (in hours): "))
    work_hour = float(input("Enter the work hour per cycle (in hours): "))
    break_hour = float(input("Enter the break hour per cycle (in hours): "))

    cycle_duration = work_hour + break_hour  # Total duration of each cycle

    # Calculate the number of full cycles and the remaining time
    full_cycles = int(total_duration // cycle_duration)
    remaining_time = total_duration - (full_cycles * cycle_duration)

    # Run the full cycles
    for i in range(full_cycles):
        start_timer("Work", work_hour)
        start_timer("Break", break_hour)

    # Run the remaining time if there is any
    if remaining_time > 0:
        start_timer("Work", min(remaining_time, work_hour))
        remaining_time -= work_hour

    if remaining_time > 0:
        start_timer("Break", min(remaining_time, break_hour))

if __name__ == "__main__":
    main()


"""