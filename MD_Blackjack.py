import time
from os import system
from random import seed
from random import randint

seed(time.time())

figura = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Walet", "Dama", "Król"]
kolor = ["Pik", "Kier", "Trefl", "Karo"]
taliaGracza = []
taliaBota = []
noRepetition = False

def takeCard(talia):
    while noRepetition:
        cardNr = figura[randint(0,12)]
        cardColor = kolor[randint(0,3)]
        for 
    talia.append(cardNr + cardColor)


def botAction(whoStarts):
    if(whoStarts == "2"):
        takeCard(taliaBota)
        takeCard(taliaBota)
        takeCard(taliaBota)
        takeCard(taliaBota)
        takeCard(taliaBota)
        takeCard(taliaBota)
        takeCard(taliaBota)
        takeCard(taliaBota)
        takeCard(taliaBota)
        takeCard(taliaBota)
        takeCard(taliaBota)
        takeCard(taliaBota)
        takeCard(taliaBota)
        takeCard(taliaBota)
        takeCard(taliaBota)
        takeCard(taliaBota)
        print(taliaBota)
        return
    else:
        return

while True:

    print ("Kto zaczyna?\n1. Ty\n2. Bot")
    whoStarts = input()
    if (whoStarts != "1" and whoStarts != "2"):
        system('cls')
        print ("Zła liczba")
    else:
        break

system('cls')

botAction(whoStarts)
