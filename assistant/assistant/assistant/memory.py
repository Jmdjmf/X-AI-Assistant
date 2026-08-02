"""
memory.py
Memory Manager
"""

class Memory:

    def __init__(self):
        self.history = []

    def save(self, text):
        self.history.append(text)

    def get_history(self):
        return self.history

    def clear(self):
        self.history.clear()
