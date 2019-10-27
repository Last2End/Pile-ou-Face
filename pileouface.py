import random

def PileouFace():
    r = random.randint(0, 1) 
    if r == 1:
        print("Vous êtes tombé sur Pile !")
    else:
        print("Vous êtes tombé sur Face !")

PileouFace()
