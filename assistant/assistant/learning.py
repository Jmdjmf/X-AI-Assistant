from assistant.profile import UserProfile

profile = UserProfile()

def learn(text):
    text = text.lower()

    if text.startswith("my name is "):
        profile.set("name", text.replace("my name is ", "").strip())
        return "I will remember your name, Sir."

    if text.startswith("my favorite color is "):
        profile.set(
            "favorite_color",
            text.replace("my favorite color is ", "").strip()
        )
        return "I will remember your favorite color, Sir."

    if text.startswith("i live in "):
        profile.set(
            "country",
            text.replace("i live in ", "").strip()
        )
        return "I will remember where you live, Sir."

    return None
