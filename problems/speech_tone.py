import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for pitch, rate, and volume
# Pitch: 0.0 to 1.0 (0.0 is lowest, 1.0 is highest)
# Rate: Speech speed in words per minute (default is 200)
# Volume: 0.0 to 1.0 (0.0 is lowest, 1.0 is highest)
engine.setProperty('pitch', 0.6)  # Adjust the pitch
engine.setProperty('rate', 150)   # Adjust the rate (speech speed)
engine.setProperty('volume', 1.0) # Adjust the volume

# Say something with the adjusted properties
engine.say('Good morning! How are you today?')

# Wait for speech to finish
engine.runAndWait()
