from assistant.chat import ChatEngine
from assistant.voice import Voice
from assistant.listener import Listener

chat = ChatEngine()
voice = Voice()
listener = Listener()

print("===== X AI Assistant =====")
voice.speak("Hello Sir, I am X. How can I help you?")

while True:
    text = listener.listen()

    if text == "":
        continue

    if text.lower() in ["exit", "quit", "bye", "goodbye"]:
        voice.speak("Goodbye Sir.")
        break

    reply = chat.reply(text)
    voice.speak(reply)
