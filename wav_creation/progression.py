import wave
import struct
import math
import time

sample_rate = 44100
volume = 0.35
chord_duration = 1.2  # seconds per chord

# Chord progression (Hz)
progression = [
    [220, 261.6, 329.6],   # Am
    [293.7, 349.2, 440],   # Dm
    [196, 246.9, 392],     # G
    [261.6, 329.6, 392]    # C
]

def envelope(i, total):
    attack = int(0.08 * total)
    release = int(0.15 * total)

    if i < attack:
        return i / attack
    elif i > total - release:
        return (total - i) / release
    else:
        return 1.0

def generate_chord(freqs, duration):
    frames = []
    total = int(sample_rate * duration)

    for i in range(total):
        sample = sum(
            math.sin(2 * math.pi * f * i / sample_rate)
            for f in freqs
        ) / len(freqs)

        sample *= envelope(i, total)
        frames.append(struct.pack('<h', int(sample * volume * 32767)))

    return b''.join(frames)

with wave.open("progression.wav", "w") as wav:
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(sample_rate)

    for _ in range(2):  # repeat progression twice
        for chord in progression:
            wav.writeframes(generate_chord(chord, chord_duration))

print("🎶 progression.wav created")
