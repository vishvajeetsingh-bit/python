import speech_recognition as sr
#source file should be in the same directory where .py file stored.
AUDIO_FILE = "source file"#source file in .wav format
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
try:
    print("audio file contains" + " " + r.recognize_google(audio))
except sr.UnknownValueError:
    print(" Google Speech Recognition could not understand audio")
except sr.RequestError:
    print("Couldn't get the results from google speech recognition")
