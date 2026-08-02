import json
import os

PROFILE_FILE = "profile.json"


class UserProfile:

    def __init__(self):
        if os.path.exists(PROFILE_FILE):
            with open(PROFILE_FILE, "r") as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save(self):
        with open(PROFILE_FILE, "w") as f:
            json.dump(self.data, f, indent=4)

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def get(self, key):
        return self.data.get(key)

    def all(self):
        return self.data
