"""
speech.py
Real Voice Recognition Module
"""

import speech_recognition as sr


class SpeechEngine:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.status = "Idle"

    def start(self):
        self.status = "Listening"
        print("🎤 Listening, Sir...")

    def stop(self):
        self.status = "Stopped"
        print("🛑 Stopped listening, Sir.")

    def listen(self):
        with sr.Microphone() as source:

            print("Speak now, Sir...")

            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)

            print("You:", text)

            return text

        except sr.UnknownValueError:
            return ""

        except Exception:
            return ""
