import wave
import struct
import math

sample_rate = 44100
duration = 1.0
volume = 0.35

# A minor chord (bossa-friendly)
chord = [220, 261.6, 329.6]

def envelope(i, total):
    attack = int(0.1 * total)
    release = int(0.2 * total)

    if i < attack:
        return i / attack
    elif i > total - release:
        return (total - i) / release
    else:
        return 1.0

def generate_chord(freqs, duration):
    frames = []
    total_samples = int(sample_rate * duration)

    for i in range(total_samples):
        sample = 0
        for freq in freqs:
            sample += math.sin(2 * math.pi * freq * i / sample_rate)

        sample /= len(freqs)
        env = envelope(i, total_samples)
        frames.append(struct.pack('<h', int(sample * env * volume * 32767)))

    return b''.join(frames)

with wave.open("chord_soft.wav", "w") as wav:
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(sample_rate)

    for _ in range(4):
        wav.writeframes(generate_chord(chord, duration))

print("🌿 chord_soft.wav created")
