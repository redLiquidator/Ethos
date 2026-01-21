import requests
from pathlib import Path
import os

# === Configuration ===
API_URL = "https://router.huggingface.co/models/facebook/musicgen-small"
API_KEY = os.getenv("HF_TOKEN_STABLEAUDIO")

prompt = "bossa jazz instrumental, gentle acoustic guitar, latin percussion"
duration = 30  # seconds
output_file = Path("generated_music/musicgen_bossa.wav")

# === Create output folder ===
output_file.parent.mkdir(parents=True, exist_ok=True)

# === Request ===
print(f"🎧 Generating: '{prompt}' ({duration}s)...")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "audio/wav"
}

response = requests.post(API_URL, headers=headers, json={
    "inputs": prompt,
    "parameters": {"duration": duration}
})

# === Handle response ===
if response.status_code == 200:
    output_file.write_bytes(response.content)
    print(f"✅ Music generated and saved at: {output_file}")
else:
    print(f"❌ Error {response.status_code}: {response.text}")
