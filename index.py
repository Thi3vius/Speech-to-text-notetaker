import speech_recognition as sr
import pyttsx3 

r = sr.Recognizer()

def record_text():
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            # Prepare recognizer to receive input 
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input 
            audio2 = r.listen(source2)

            # using google to recognize the audio
            MyText = r.recognize_google(audio2)
            return MyText
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
    return ""  # Return an empty string on error

def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True:
    text = record_text()
    print("Recognized:", text)  # Print recognized text
    output_text(text)
    speak_text(text)  # Optional: Convert to speech
    print("Wrote text to file and spoke aloud")