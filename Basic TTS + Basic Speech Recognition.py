import speech_recognition as sr
import pyttsx3
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(user_agent='MyProjectName (merlin@example.com)', language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
# Initialize the recognizer
#Recogniser() provides methods to recognise speech from audio data
recognizer = sr.Recognizer()

engine = pyttsx3.init() # object creation

# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 30)     # setting up new voice rate
print(rate)
# VOLUME
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print (volume)                          # printing current volume level
engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1
# VOICE
voices = engine.getProperty('voices')       # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female


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
        engine.say("Hello World!")
    elif text == "what is dark souls?":
        page = text.replace("what" "is", " ")
        print(page)
        pagebeinggrabbed = wiki_wiki.page(page)
        print(f"{page} - Exists: {pagebeinggrabbed.exists()}")
        if pagebeinggrabbed.exists():
            engine.say(f"Page - Title: {pagebeinggrabbed.title}Page - Summary: {pagebeinggrabbed.summary[0:60]} {pagebeinggrabbed.canonicalurl}")
        else:
            engine.say("sorry, we could not find that for you")

            
except sr.UnknownValueError:
    print("Sorry, I couldn't understand the audio.")
#prints an error message with the details when reaching recognition service
except sr.RequestError as e:
    print(f"Could not request results; {e}")


#engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()