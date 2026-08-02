from assistant.chat import ChatEngine

chat = ChatEngine()

print("=" * 50)
print("X AI Assistant Test")
print("=" * 50)

while True:

    user = input("Sir : ")

    if user.lower() == "exit":
        print("X : Goodbye, Sir.")
        break

    reply = chat.reply(user)

    print("X :", reply)
