

from backend import *


#C:\Users\a_nie\fnChck\EasyEnglish\SpeechRecognition\sentences.txt
#C:\Users\a_nie\fnChck\EasyEnglish\output.txt
userPoints = 0
questionCount = int(input("How many practice questions would you like? "))

# iFilePath = input("Please enter where you will be pulling the phrase from: ")

# oFilepath = input("Please input where the output file is located: ")


incorrectAnswers = []
exit = False
while(questionCount > 0 and (not exit)):
    livesPerQ = 3
    chosenWord = chosenPhrase()
    print(f"the phrase to repeat is: {chosenWord}")
    
    userAnswer = userInput(speechRecognition())
    correctAnswer = chosenWord
    if userAnswer == "exit":
        exit = True
    else:
        answer = False
        while not answer and livesPerQ > 0:
            answer = tryout(chosenWord,userAnswer)
            if answer:
                userPoints+= 1
                print("Correct Answer")
            else:
                print("Incorrect Answer")
                userAnswer = userInput(speechRecognition())
                livesPerQ-= 1

    questionCount-= 1

print(f"your total score is {userPoints}")

# for answer in incorrectAnswers:
#     print(answer)


    
