import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()
outfile = open("output.txt", "w")
run = True


try:

    with speech_recognition.Microphone() as mic:

        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)

        text = recognizer.recognize_google(audio)
        text = text.lower()

        print(f"Recognized {text}")

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
