import requests
from pathlib import Path
import os

# === Configuration ===
API_URL = "https://api.stability.ai/v2beta/audio/stable-audio-2/text-to-audio"
API_KEY = "sk-3xvjwemqVqA6f8yIFeUAhTW1xovfKfVY6ITZIzngGHvXVLCM"
# 🎵 Your music prompt
prompt = "bossa jazz no voice, acoustic guitar, latin percussion"

# 🎯 Designated output folder
output_dir = Path("/Users/jinjoolee/Documents/ethos/generated_music")
output_dir.mkdir(parents=True, exist_ok=True)  # create folder if missing

# 💾 Auto-name the file based on prompt
safe_name = "_".join(prompt.split()[:4])  # use first few words
output_file = output_dir / f"{safe_name}.wav"

# === API Request ===
response = requests.post(
    API_URL,
    headers={
        "authorization": f"Bearer {API_KEY}",
        "accept": "audio/*"
    },
    files={"none": ""},
    data={
        "prompt": prompt,
        "output_format": "wav",
        "duration": 30,
        "model": "stable-audio-2.5"
    },
)

# === Handle Response ===
if response.status_code == 200:
    output_file.write_bytes(response.content)
    print(f"✅ Music generated: {output_file}")
else:
    print("❌ Error:", response.status_code, response.text)