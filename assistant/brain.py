from assistant.learning import learn
from assistant.knowledge import answer
from assistant.commands import CommandEngine
from assistant.chat import ChatEngine


class Brain:

    def __init__(self):
        self.chat = ChatEngine()
        self.commands = CommandEngine()

    def process(self, text):

        # Learn new information
        learned = learn(text)
        if learned:
            return learned

        # Answer from personal knowledge
        personal = answer(text)
        if personal:
            return personal

        # Execute commands
        command = self.commands.execute(text)
        if command:
            return command

        # Ask Gemini AI
        return self.chat.reply(text)
