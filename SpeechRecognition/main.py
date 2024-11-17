
from backend import *





print("your chosen word is ")
chosenWord = chosenPhrase()
oFilepath = input("Please input where the output file is located: ")
print(f"the phrase to repeat is: {chosenWord}")


speechRecognition()

print(tryout(chosenWord,userInput(oFilepath)))


