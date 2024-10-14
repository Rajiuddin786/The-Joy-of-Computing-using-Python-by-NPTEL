import speech_recognition as sr

Audio_File = ("Example.wav")

r=sr.Recognizer() #Initialization

with sr.AudioFile(Audio_File) as source:
    audio = r.record(source) #Read Audio File

try:
    print('Audio File Contains',r.recognize_google_cloud(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition Could Not Understand Audio")
except sr.RequestError:
    print("Could not get the result from google Speech Recognition")