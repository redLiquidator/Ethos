import wave
import struct
import math

sample_rate = 44100
duration_per_note = 0.4  # seconds
volume = 0.4

# Simple bossa-like notes (Hz)
melody = [
    440,  # A
    493,  # B
    523,  # C
    587,  # D
    523,  # C
    493,  # B
    440   # A
]

def generate_tone(freq, duration):
    frames = []
    total_samples = int(sample_rate * duration)
    for i in range(total_samples):
        value = volume * math.sin(2 * math.pi * freq * i / sample_rate)
        frames.append(struct.pack('<h', int(value * 32767)))
    return b''.join(frames)

with wave.open("melody.wav", "w") as wav:
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(sample_rate)

    for note in melody:
        wav.writeframes(generate_tone(note, duration_per_note))

print("🎶 melody.wav created")
