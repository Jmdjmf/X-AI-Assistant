"""
memory.py
Simple memory module
"""

memory = []

def add_memory(role, text):
    memory.append({
        "role": role,
        "text": text
    })

def get_memory():
    return memory

def clear_memory():
    memory.clear()
