from assistant.brain import Brain

brain = Brain()

print("=" * 50)
print("          X AI Assistant")
print("=" * 50)
print("Type 'exit' to close X.\n")

while True:

    text = input("Sir : ").strip()

    if not text:
        continue

    if text.lower() in ["exit", "quit", "bye"]:
        print("X : Goodbye Sir.")
        break

    reply = brain.process(text)

    print("X :", reply)
