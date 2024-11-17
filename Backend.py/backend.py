
import difflib
import random
import speech_recognition
import pyttsx3
import os
from sentences import *

def tryout(correctPhrase, wordSpoken):
    lowerChoice = wordSpoken.lower()
    lowerAnswer = correctPhrase.lower()

    similarity = difflib.SequenceMatcher(None, lowerChoice, lowerAnswer).ratio()

    if similarity >= 0.9:
        return True
    else:
        return False

def userInput(recognized_text):
    if recognized_text:
        userInput = recognized_text  
    else:
        userInput = ""  
    return userInput


def chosenPhrase():
    chosenPhrase = random.choice(allSentences)
    return chosenPhrase


def speechRecognition():
    recognizer = speech_recognition.Recognizer()
    
    # Initialize the variable to hold the recognized text
    recognized_text = ""
    
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.3)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"{text}")

            # Set the recognized text as a string
            recognized_text = text

    except speech_recognition.UnknownValueError:
        print("Please say again!")
        recognized_text = ""  # Set to an empty string if recognition fails

    except speech_recognition.RequestError:
        print("Could not request result; {0}".format(speech_recognition.RequestError))
        recognized_text = ""  # Set to an empty string if there's a request error

    # Return the recognized text as a string
    return recognized_text


        
