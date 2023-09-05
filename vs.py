import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import tempfile
import os
import pyttsx3
    
# Function to recognize speech and convert it to text
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = recognizer.listen(source)
        try:
            recognized_text = recognizer.recognize_google(audio_data)
            return recognized_text
        except sr.UnknownValueError:
            return None

# Function to translate text
def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

# Function to convert text to speech
def text_to_speech(text, output_file, lang_code):
    tts = gTTS(text, lang=lang_code)
    tts.save(output_file)

# Input voice file (in the source language)
engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
print("SPEAK NOW")
speak("listening .....")
# Recognize speech from the input voice
recognized_text = recognize_speech()

if recognized_text:
    speak(recognized_text)
    print(f"Recognized Text: {recognized_text}")
    speak("would you like to translate this")
    comfirm = recognize_speech()
    if comfirm!="no" :
        pass
    else:
        exit()
    # Define the target language for translation
    speak("tell your desired language")
    target_language = recognize_speech()
    target = target_language[0:2].lower()
    # Translate the recognized text to the target language
    translated_text = translate_text(recognized_text, target)

    print(f"Translated Text: {translated_text}")

    # Convert translated text to speech in the target language
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        temp_filename = temp_file.name
        text_to_speech(translated_text, temp_filename, target)

    print(f"Translated Speech saved as: {temp_filename}")

    # Play the translated speech (platform-dependent, you may need to modify)
    try:
        os.system(f"start {temp_filename}")  # For Windows
    except Exception as e:
        print("Unable to play the audio. Error:", str(e))
else:
    print("Unable to recognize speech from the input audio.")
