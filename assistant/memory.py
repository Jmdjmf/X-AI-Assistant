import json
import os

MEMORY_FILE = "memory.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def add_memory(user, assistant):
    memory = load_memory()

    memory.append({
        "user": user,
        "assistant": assistant
    })

    # Keep only the last 50 conversations
    memory = memory[-50:]

    save_memory(memory)


def get_memory():
    return load_memory()
