import ctypes
import pyttsx3
import time
"""
https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10
create an automated task using Task Scheduler on Windows 10
"""

du_time = 10
while True:
    # Text to be spoken and displayed
    text = "Hey Sohyem, drink water"
    print(1)

    # Speak the text
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

    # Display a message box
    ctypes.windll.user32.MessageBoxW(0, text, "Hey Sohyem", 0x40 | 0x1)
    print(2)
    time.sleep(du_time)
