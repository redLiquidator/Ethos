import wave
import struct
import math
import random

sample_rate = 44100
volume_bass = 0.45
volume_chord = 0.30

base_bass_duration = 0.32
base_breath_duration = 0.08
base_chord_duration = 0.78

# Progression: (bass_freq, chord_freqs)
progression = [
    (110, [220, 261.6, 329.6]),   # A → Am
    (146.8, [293.7, 349.2, 440]), # D → Dm
    (98, [196, 246.9, 392]),      # G
    (130.8, [261.6, 329.6, 392])  # C
]

def envelope(i, total, attack_ratio=0.1, release_ratio=0.25):
    attack = int(attack_ratio * total)
    release = int(release_ratio * total)

    if i < attack:
        return i / attack
    elif i > total - release:
        return (total - i) / release
    else:
        return 1.0

def generate_tone(freq, duration, volume):
    frames = []
    total = int(sample_rate * duration)

    for i in range(total):
        sample = math.sin(2 * math.pi * freq * i / sample_rate)
        sample *= envelope(i, total)
        frames.append(struct.pack('<h', int(sample * volume * 32767)))

    return b''.join(frames)

def generate_chord(freqs, duration, volume):
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

def generate_silence(duration):
    total = int(sample_rate * duration)
    return b'\x00\x00' * total

def humanize(base, amount=0.03):
    """amount = max variation in seconds"""
    return max(0.02, base + random.uniform(-amount, amount))

with wave.open("bass_chord_human.wav", "w") as wav:
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(sample_rate)

    for _ in range(2):
        for bass, chord in progression:
            bass_dur = humanize(base_bass_duration)
            breath_dur = humanize(base_breath_duration, 0.02)
            chord_dur = humanize(base_chord_duration)

            wav.writeframes(generate_tone(bass, bass_dur, volume_bass))
            wav.writeframes(generate_silence(breath_dur))
            wav.writeframes(generate_chord(chord, chord_dur, volume_chord))

print("🎶 bass_chord_human.wav created")
