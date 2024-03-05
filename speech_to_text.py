import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.AudioFile("Recording.wav") as source:
    audio = recognizer.record(source)

try:
    print("Content of audio file: ", recognizer.recognize_google(audio))

except sr.UnknownValueError:
    print("Can't understand audio")

except sr.RequestError:
    print("Can't get results from google")

except Exception as e:
    print(e)
