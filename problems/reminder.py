import time
import pyttsx3
from win10toast import ToastNotifier

toster = ToastNotifier()


def send_notification(timer_name, message):
    global toster
    toster.show_toast(timer_name, message, duration=10)


def get_duration(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Duration should be a positive integer.")
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def timer(duration, timer_name, hours, minutes, engine):
    if hours == 0:
        message = f"{timer_name}'s Timer started for {minutes} minutes."
    elif minutes == 0:
        message = f"{timer_name}'s Timer started for {hours} hours."
    else:
        message = f"{timer_name}'s Timer started for {hours} hours and {minutes} minutes."

    print(message)
    send_notification(timer_name,message)
    # engine.say(message)
    # engine.runAndWait()
    time.sleep(duration)
    end_message = f"Timer for {timer_name} finished!"
    send_notification(timer_name,end_message)
    print(end_message)
    # engine.say(end_message)
    # engine.runAndWait()


if __name__ == "__main__":
    try:
        work_timeHr = get_duration("Enter work duration in hours: ")
        work_timeM = get_duration("Enter work duration in minutes: ")
        break_timeHr = get_duration("Enter break duration in hours: ")
        break_timeM = get_duration("Enter break duration in minutes: ")

        workT = (work_timeHr * 3600) + (work_timeM * 60)
        breakT = (break_timeHr * 3600) + (break_timeM * 60)

        engine = pyttsx3.init()
        while True:
            timer(workT, "Work", work_timeHr, work_timeM, engine)
            timer(breakT, "Break", break_timeHr, break_timeM, engine)

    except ValueError as ve:
        print("Error:", str(ve))
