from assistant.profile import UserProfile

profile = UserProfile()


def answer(question):

    q = question.lower()

    if "what is my name" in q or "who am i" in q:
        name = profile.get("name")

        if name:
            return f"Your name is {name}, Sir."

        return "I don't know your name yet, Sir."

    if "favorite color" in q:
        color = profile.get("favorite_color")

        if color:
            return f"Your favorite color is {color}, Sir."

        return "I don't know your favorite color yet, Sir."

    if "where do i live" in q:
        country = profile.get("country")

        if country:
            return f"You live in {country}, Sir."

        return "I don't know where you live yet, Sir."

    return None
