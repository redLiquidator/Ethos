import wave
import struct
import math

sample_rate = 44100
duration = 0.6
volume = 0.3

# Bossa-style chord (A minor)
chord = [220, 261.6, 329.6]  # A2, C4, E4

def generate_chord(freqs, duration):
    frames = []
    total_samples = int(sample_rate * duration)

    for i in range(total_samples):
        sample = 0
        for freq in freqs:
            sample += math.sin(2 * math.pi * freq * i / sample_rate)

        sample = sample / len(freqs)  # normalize
        frames.append(struct.pack('<h', int(sample * volume * 32767)))

    return b''.join(frames)

with wave.open("chord.wav", "w") as wav:
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(sample_rate)

    for _ in range(4):
        wav.writeframes(generate_chord(chord, duration))

print("🎹 chord.wav created")
