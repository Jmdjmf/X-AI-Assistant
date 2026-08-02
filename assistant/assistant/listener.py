import speech_recognition as sr

class Listener:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 300
        self.recognizer.pause_threshold = 0.8

    def listen(self):
        with sr.Microphone() as source:
            print("🎤 Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            print("Sir :", text)
            return text

        except sr.UnknownValueError:
            return ""

        except Exception as e:
            print(e)
            return ""
