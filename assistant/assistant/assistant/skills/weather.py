%%writefile assistant/skills/weather.py
import requests

def get_weather(text):
    text = text.lower()

    if "weather" not in text:
        return None

    city = "Delhi"

    words = text.split()

    if "in" in words:
        i = words.index("in")
        if i + 1 < len(words):
            city = " ".join(words[i + 1:])

    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return response.text

    except Exception:
        return "Sorry Sir, Weather service is unavailable."

    return "Sorry Sir, Weather service is unavailable."
