import requests


def get_weather(text):

    text = text.lower()

    if "weather" not in text:
        return None

    city = "Delhi"

    url = f"https://wttr.in/{city}?format=3"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return response.text

    except Exception:
        pass

    return "Sorry Sir, I couldn't get the weather right now."
