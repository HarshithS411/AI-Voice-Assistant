import os
import eel
from playsound import playsound

# Define the function to play the assistant sound
def playAssistantsound():
    music_dir = "C:\\Users\\BLESSTO\\OneDrive\\Documents\\AI-Voice-Assistant\\www\\assets\\www_assets_audio_start_sound.mp3"
    playsound(music_dir)

# Initialize eel and play the sound
eel.init("www")
playAssistantsound()

# Start the eel application with Microsoft Edge as the browser
eel.start('index.html', mode='edge', host='localhost', block=True)
