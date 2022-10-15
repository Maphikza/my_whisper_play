from pydub import AudioSegment
from pydub.playback import play

audio = AudioSegment.from_file("speech.m4a", "m4a")
play(audio)

