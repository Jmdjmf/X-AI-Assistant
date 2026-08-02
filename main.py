from assistant.chat import ChatEngine
from assistant.commands import CommandEngine
from assistant.learning import learn
from assistant.knowledge import answer

chat = ChatEngine()
commands = CommandEngine()

print("=" * 50)
print("           X AI Assistant")
print("=" * 50)
print("Type 'exit' to close X.\n")

while True:

    text = input("Sir : ").strip()

    if not text:
        continue

    if text.lower() in ["exit", "quit", "bye"]:
        print("X : Goodbye Sir. Have a great day!")
        break

    # Learn personal information
    learned = learn(text)

    if learned:
        print("X :", learned)
        continue

    # Answer from personal knowledge
    personal = answer(text)

    if personal:
        print("X :", personal)
        continue

    # Execute built-in commands
    result = commands.execute(text)

    if result:
        print("X :", result)
        continue

    # Ask Gemini AI
    reply = chat.reply(text)

    print("X :", reply)
