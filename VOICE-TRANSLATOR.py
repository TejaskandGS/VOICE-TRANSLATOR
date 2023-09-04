import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
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
  
# Recognize speech from the input voice
input_voice = recognize_speech()

if input_voice:
    print(f"Recognized Text: {input_voice}")

    # Define the target language for translation
    target_language = input("enter your desired langauage ")  # Enter your target language code (e.g., "fr" for French)

    # Translate the recognized text to the target language
    translated_text = translate_text(input_voice, target_language)

    print(f"Translated Text: {translated_text}")

    # Convert translated text to speech in the target language
    output = "hello.mp3"
    output_voice = text_to_speech(translated_text,output,target_language)

    print(f"Translated Speech saved as: {output}")

    # Play the translated speech 
    try:
        playsound.playsound("hello.mp3") 
    except Exception as e:
        print("Unable to play the audio. Error:", str(e))
else:
    print("Unable to recognize speech from the input audio.")


