from pydub import AudioSegment
from pathlib import Path

# instead of overlay, we’ll concatenate (+) each stem — meaning one plays after the previous finishes.
# sequential mixer — script chained both WAVs back-to-back into a single continuous file
# === Load stems ===
folder = Path("stems")
stems = [AudioSegment.from_file(p) for p in folder.glob("*.wav")]
if not stems:
    raise FileNotFoundError("No WAV files found in the 'stems/' folder!")

# === Sequential mixing ===
mix = AudioSegment.silent(duration=0)
for i, s in enumerate(stems):
    s = s.fade_in(300).fade_out(300)
    mix += s  # concatenate instead of overlay
    print(f"→ Added stem {i+1} sequentially (length: {len(s)/1000:.2f}s)")

# === Export ===
output = Path("mixed_output_sequential.wav")
mix.export(output, format="wav")
print(f"\n✅ Sequential mix saved as: {output}")
