
from backend import *


#C:\Users\a_nie\fnChck\EasyEnglish\SpeechRecognition\sentences.txt
#C:\Users\a_nie\fnChck\EasyEnglish\output.txt

print("your chosen word is ")
iFilePath = input("Please enter where you will be pulling the phrase from: ")
chosenWord = chosenPhrase(iFilePath)
oFilepath = input("Please input where the output file is located: ")
print(oFilepath)
print(f"the phrase to repeat is: {chosenWord}")


speechRecognition()

print(tryout(chosenWord,userInput(oFilepath)))


