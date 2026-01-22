from pydub import AudioSegment
from pydub.playback import play
from pathlib import Path
import random

#randomly offsets stems in time (like layered parts),
#randomizes left/right panning,
#adds fade-ins and fade-outs for smoother blending.

# === Load stems ===
folder = Path("stems")
stems = [AudioSegment.from_file(p) for p in folder.glob("*.wav")]
if not stems:
    raise FileNotFoundError("No WAV files found in the 'stems/' folder!")

# === Create a blank base track (long enough to fit everything) ===
duration = max(s.duration_seconds for s in stems) * 1000 + 5000  # 5s extra
mix = AudioSegment.silent(duration=int(duration))

# === Mix stems with random offset, pan, and gain ===
for i, s in enumerate(stems):
    gain = random.uniform(-3, 3)
    offset = random.uniform(0, 2000 * i)  # up to 2s offset per stem index
    s = s + gain

    # apply random panning (L/R)
    pan = random.uniform(-0.6, 0.6)
    s = s.pan(pan)

    # smooth start/end
    s = s.fade_in(500).fade_out(500)

    # overlay it at offset
    mix = mix.overlay(s, position=int(offset))
    print(f"→ Added stem {i+1} with {gain:+.1f} dB gain, pan={pan:+.2f}, offset={offset:.0f}ms")

# === Export result ===
output = Path("mixed_output_advanced.wav")
mix.export(output, format="wav")
print(f"\n✅ Final mix saved as: {output}")
