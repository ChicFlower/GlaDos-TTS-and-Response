#sr allows us to more easily reference the libary
import speech_recognition as sr

# Initialize the recognizer
#Recogniser() provides methods to recognise speech from audio data
recognizer = sr.Recognizer()

# Use the microphone as source
with sr.Microphone() as source:
    print("Please say something:")
    # Adjust for ambient noise
    recognizer.adjust_for_ambient_noise(source)
    # Listen for audio
    #listen() captures audio
    audio = recognizer.listen(source)

try:
    # Recognize speech using Google Web Speech API using recognize_google(audio)
    text = recognizer.recognize_google(audio)
    if text == "good morning":
        print("good morning! :)")
except sr.UnknownValueError:
    print("Sorry, I couldn't understand the audio.")
#prints an error message with the details when reaching recognition service
except sr.RequestError as e:
    print(f"Could not request results; {e}")