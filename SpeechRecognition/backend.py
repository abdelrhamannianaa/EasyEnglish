import difflib
import random
import speech_recognition
import pyttsx3
import os

def tryout(correctPhrase, wordSpoken):
    lowerChoice = wordSpoken.lower()
    lowerAnswer = correctPhrase.lower()

    similarity = difflib.SequenceMatcher(None, lowerChoice, lowerAnswer).ratio()

    if similarity >= 0.8:
        return True
    else:
        return False

def userInput(oFilepath):
    with open(oFilepath, 'r') as file:
        userInput = file.readline()
    return userInput


def chosenPhrase(iFilePath):
    with open(iFilePath, 'r') as file:
        correctSentences = file.readlines()

    chosenPhrase = random.choice(correctSentences)
    return chosenPhrase


def speechRecognition():
    recognizer = speech_recognition.Recognizer()
    outfile = open("output.txt", "w")
    try:

        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"{text}")

            # if "exit" in text:
            #     print("Exiting...")
            #     run = False
            outfile.write(text)
            outfile.write("\n")

    except speech_recognition.UnknownValueError:
        print("Please say again!")
        recognizer = speech_recognition.Recognizer()

    except speech_recognition.RequestError:
        print("could not request result; {0}".format(speech_recognition.RequestError))
        recognizer = speech_recognition.Recognizer()
        




