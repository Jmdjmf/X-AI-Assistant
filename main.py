"""
X AI Assistant
Main Program
"""

from assistant.brain import Brain
from assistant.speech import SpeechEngine

brain = Brain()
speech = SpeechEngine()

print("=" * 50)
print("            X AI Assistant")
print("=" * 50)

print("Status : Ready")
print("Assistant : Hello, Sir.")
print("Type 'exit' to close X.\n")

speech.start()

while True:

    command = input("Sir : ")

    if command.lower() == "exit":
        speech.stop()
        print("X : Goodbye, Sir.")
        break

    response = brain.think(command)

    print("X :", response)
