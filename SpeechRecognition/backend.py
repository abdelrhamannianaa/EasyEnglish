import difflib
import random
def tryout(wordSpoken, correctPhrase):
    lowerChoice = wordSpoken.lower()
    lowerAnswer = correctPhrase.lower()

    similarity = difflib.SequenceMatcher(None, lowerChoice, lowerAnswer).ratio()

    if similarity >= 0.9:
        return True
    else:
        return False
    
with open('output.txt', 'r') as file:
    userInput = file.readline()


with open('sentences.txt', 'r') as file:
    correctSentences = file.readlines()

chosenPhrase = random.choice(correctSentences)

if(tryout(userInput, "vincent is not") == True):
        print("Correct!")
else:
    print("Incorrect!")



