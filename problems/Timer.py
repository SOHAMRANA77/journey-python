import time


def start_timer(timer_name, duration):
    print(f"Timer for {timer_name} is running for {duration} minutes.")
    time.sleep(duration * 60)
    print(f"{timer_name} timer is done!")


print(1)
print(time.sleep(1 * 60))
print(2)
