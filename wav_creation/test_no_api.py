# TEMP: test audio output
import wave
import struct
import math

sample_rate = 44100
frequency = 440  # test tone
duration_sec = 2

with wave.open("output.wav", "w") as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)

    for i in range(int(sample_rate * duration_sec)):
        value = int(32767 * math.sin(2 * math.pi * frequency * i / sample_rate))
        wav_file.writeframes(struct.pack('<h', value))

print("Test audio saved as output.wav")