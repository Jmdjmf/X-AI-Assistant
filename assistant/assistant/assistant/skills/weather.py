import requests

def get_weather(text):
    text = text.lower()

    if "weather" not in text:
        return None

    city = "Delhi"

    words = text.split()

    if "in" in words:
        index = words.index("in")
        if index + 1 < len(words):
            city = " ".join(words[index + 1:])

    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return response.text

    except Exception:
        pass

    return "Sorry Sir, I couldn't fetch the weather."
