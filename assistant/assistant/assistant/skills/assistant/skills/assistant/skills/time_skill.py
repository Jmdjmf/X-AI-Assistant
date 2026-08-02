import datetime

def get_time(text):

    text = text.lower()

    if "time" not in text:
        return None

    now = datetime.datetime.now()

    return f"The current time is {now.strftime('%I:%M %p')}, Sir."
