
import random

def randomWord():
    content = []

    with open("sentences.txt", "r") as word:
        content = word.read().splitlines()

    chose = random.choice(content)
    return chose
