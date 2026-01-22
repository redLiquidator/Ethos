from pydub import AudioSegment
import random
from pathlib import Path

# === Load stems ===
folder = Path("stems")
stems = [AudioSegment.from_file(p) for p in folder.glob("*.wav")]

# === Optional random volume & pan adjustments ===
for i, s in enumerate(stems):
    gain = random.uniform(-3, 3)
    stems[i] = s + gain

# === Mix all stems together. plays in parallel ===
mix = stems[0]
for s in stems[1:]:
    mix = mix.overlay(s)

# === Normalize volume and export ===
mix = mix.normalize()
output = Path("mixed_output.wav")
mix.export(output, format="wav")
print(f"✅ Mixed track saved as: {output}")