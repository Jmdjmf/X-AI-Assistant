from assistant.chat import ChatEngine
from assistant.commands import CommandEngine

chat = ChatEngine()
commands = CommandEngine()

print("=" * 50)
print("X AI Assistant")
print("=" * 50)

while True:

    text = input("Sir : ")

    if text.lower() in ["exit", "quit", "bye"]:
        print("X : Goodbye Sir.")
        break

    result = commands.execute(text)

    if result:
        print("X :", result)
        continue

    reply = chat.reply(text)

    print("X :", reply)
