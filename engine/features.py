from playsound import playsound
import eel

# Playing assistant sound function
@eel.expose
def play_assistant_sound():
    music_dir = "www//assets//www_assets_audio_start_sound.mp3"  # Use forward slashes
    playsound(music_dir)
