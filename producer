import requests
import base64

# -----------------------------
# 1. YOUR PRODUCER CONTROLS
# -----------------------------
tempo = 92
duration = 90  # seconds
style = "bossa"

# Producer logic (NOT creative prompting)
if style == "bossa":
    api_prompt = "calm bossa nova, soft rhythm, acoustic guitar, warm tone"
elif style == "funk":
    api_prompt = "soft funk groove, relaxed tempo, warm bass"
else:
    api_prompt = "calm instrumental music"

# -----------------------------
# 2. MUSIC API REQUEST
# (example structure – adapt URL & payload)
# -----------------------------
API_URL = "https://example-music-api.com/generate"
API_KEY = "PUT_YOUR_API_KEY_HERE"

payload = {
    "prompt": api_prompt,
    "tempo": tempo,
    "duration": duration,
    "format": "wav"
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("Sending request to music API...")
response = requests.post(API_URL, json=payload, headers=headers)

if response.status_code != 200:
    raise Exception(f"API error: {response.text}")

# -----------------------------
# 3. SAVE AUDIO FILE
# -----------------------------
# Assume API returns base64-encoded audio
audio_base64 = response.json()["audio"]
audio_bytes = base64.b64decode(audio_base64)

with open("output.wav", "wb") as f:
    f.write(audio_bytes)

print("Done. Saved output.wav")
