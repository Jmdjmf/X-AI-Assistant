from assistant.learning import learn
from assistant.knowledge import answer
from assistant.commands import CommandEngine
from assistant.chat import ChatEngine

from assistant.skills.time_skill import get_time
from assistant.skills.calculator import calculate


class Brain:

    def __init__(self):
        self.chat = ChatEngine()
        self.commands = CommandEngine()

    def process(self, text):

        # Learn new information
        learned = learn(text)
        if learned:
            return learned

        # Personal knowledge
        personal = answer(text)
        if personal:
            return personal

        # Time Skill
        result = get_time(text)
        if result:
            return result

        # Calculator Skill
        result = calculate(text)
        if result:
            return result

        # Commands
        command = self.commands.execute(text)
        if command:
            return command

        # Gemini
        return self.chat.reply(text)
