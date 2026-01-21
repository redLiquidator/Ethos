from huggingface_hub import InferenceClient
from pathlib import Path
import os

# ✅ Free working model (Stable Audio) echo $HF_TOKEN\n
MODEL = "stabilityai/stable-audio-open-small"
API_KEY = os.getenv("HF_TOKEN")

client = InferenceClient(model=MODEL, token=API_KEY)

prompt = "bossa nova jazz instrumental with gentle acoustic guitar and light percussion"
output_path = Path("generated_music/free_bossa.wav")
output_path.parent.mkdir(exist_ok=True)

print(f"🎧 Generating from model: {MODEL}")

try:
   # ✅ Correct API method
    audio = client.text_to_audio(prompt)
    
    # Save bytes to file
    output_path.write_bytes(audio)
    print(f"✅ Saved: {output_path}")
except Exception as e:
    print(f"❌ Generation failed: {e}")
