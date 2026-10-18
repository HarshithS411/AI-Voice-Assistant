import os
import eel
from playsound import playsound


def playAssistantSound():
    # Get the project folder path
    project_dir = os.path.dirname(os.path.abspath(__file__))

    # Create the audio file path
    music_dir = os.path.join(
        project_dir,
        "www",
        "assets",
        "audio",
        "start_sound.mp3"
    )

    print("Looking for:", music_dir)

    if os.path.exists(music_dir):
        print("Audio file found!")
        playsound(music_dir)
    else:
        print("ERROR: Audio file does not exist!")
        print("Please check:")
        print("www/assets/audio/start_sound.mp3")


def start():
    # Initialize Eel
    eel.init("www")

    # Play startup sound
    playAssistantSound()

    # Open the GUI in Microsoft Edge
    os.system(
        'start msedge.exe --app="http://localhost:8000/index.html"'
    )

    # Start Eel
    eel.start(
        "index.html",
        mode=None,
        host="localhost",
        block=True
    )


if __name__ == "__main__":
    start()