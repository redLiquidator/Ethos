import wave
import struct
import math

sample_rate = 44100
volume_bass = 0.45
volume_chord = 0.30

bass_duration = 0.35
chord_duration = 0.85

# Progression: (bass_freq, chord_freqs)
progression = [
    (110, [220, 261.6, 329.6]),   # A → Am
    (146.8, [293.7, 349.2, 440]), # D → Dm
    (98, [196, 246.9, 392]),      # G
    (130.8, [261.6, 329.6, 392])  # C
]

def envelope(i, total, attack_ratio=0.08, release_ratio=0.15):
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

with wave.open("bass_chord.wav", "w") as wav:
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(sample_rate)

    for _ in range(2):  # repeat progression twice
        for bass, chord in progression:
            wav.writeframes(generate_tone(bass, bass_duration, volume_bass))
            wav.writeframes(generate_chord(chord, chord_duration, volume_chord))

print("🎵 bass_chord.wav created")
