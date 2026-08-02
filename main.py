"""
X AI Assistant
Professional Main Engine
Version 1.0
"""

from assistant.speech import SpeechEngine
from assistant.brain import Brain
from assistant.commands import CommandManager
from assistant.chat import ChatEngine
from assistant.automation import Automation
from assistant.ai import AIEngine
from assistant.memory import Memory

speech = SpeechEngine()
brain = Brain()
commands = CommandManager()
automation = Automation()
ai = AIEngine()
memory = Memory()
chat = ChatEngine()

print("=" * 60)
print("        X AI Assistant Professional")
print("=" * 60)

print("Status : Ready")
print("Assistant : Hello, Sir.")
print("Version : 1.0")
print()

speech.start()

while True:

    command = input("Sir : ").strip()

    if command.lower() == "exit":
        speech.stop()
        print("X : Goodbye, Sir.")
        break

    memory.save(command)

    action = commands.detect(command)

    if action == "OPEN_YOUTUBE":
        automation.open_youtube()
        continue

    elif action == "OPEN_GOOGLE":
        automation.open_google()
        continue

    elif isinstance(action, tuple):

        if action[0] == "SEARCH":
            automation.search_google(action[1])
            continue

        elif action[0] == "TYPE":
            print("Typing:", action[1])
            continue

    response = chat.reply(command)

    print("X :", response)
