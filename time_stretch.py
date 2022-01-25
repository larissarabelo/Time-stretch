import os
import librosa
from IPython.display import Audio
y, sr=librosa.load("audio.wav", sr=None)

y_shorter=librosa.effects.time_stretch(y,1.11)
#it shows the audio 11% shorter
Audio(y_shorter, rate=sr)
y_longer=librosa.effects.time_stretch(y,0.89)
#it shows the audio 11% longer 
Audio(y_longer, rate=sr)
