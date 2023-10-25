import pyttsx3

l = ["soham", "kushal", "manav", "rohan"]
engine = pyttsx3.init()
desired_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
# Example voice ID
# desired_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
engine.setProperty('voice', desired_voice_id)
for word in l:
    engine.say(f'Good morning! How are you today? {word}')
    engine.runAndWait()
"""
# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get the available voices
voices = engine.getProperty('voices')

# Print available voices
print('Available voices:')
for voice in voices:
    print('ID:', voice.id, 'Name:', voice.name, 'Langauge:', voice.languages)

# Set a specific voice (if available)
# Change the voice by changing the ID to a valid voice ID from the available voices
desired_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'  # Example voice ID
# desired_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'  # Example voice ID
engine.setProperty('voice', desired_voice_id)
#
# Say something with the desired voice
engine.say('Good morning!')
#
# # Wait for speech to finish
# engine.runAndWait()
"""
