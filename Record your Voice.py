#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install sounddevice wavio')

import sounddevice as sd
import wavio

def record_audio(duration, filename):
    print("Recording audio...")
    audio_data = sd.rec(int(duration * 44100), samplerate=44100, channels=2, dtype='int16')
    sd.wait()
    print("Recording complete.")
    
    print("Saving audio to WAV file...")
    wavio.write(filename, audio_data, 44100, sampwidth=2)
    print(f"Audio saved to {filename}.")

if __name__ == "__main__":
    recording_duration = 5  # Recording duration in seconds
    output_filename = "recorded_audio.wav"

    record_audio(recording_duration, output_filename)

