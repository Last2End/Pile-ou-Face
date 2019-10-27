import random

def PileouFace():
    r = random.randint(0, 1) 
    if r == 1:
        return print("Vous êtes tombé sur Pile !")
    if r == 0:
        return print("Vous êtes tombé sur Face !")

PileouFace()
