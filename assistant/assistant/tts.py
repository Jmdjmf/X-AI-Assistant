import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


class TTS:
    def speak(self, text):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-preview-tts",
                contents=text,
                config=types.GenerateContentConfig(
                    response_modalities=["AUDIO"]
                ),
            )

            with open("x_voice.wav", "wb") as f:
                f.write(response.candidates[0].content.parts[0].inline_data.data)

            print("🔊 Voice saved as x_voice.wav")

        except Exception as e:
            print("TTS Error:", e)
