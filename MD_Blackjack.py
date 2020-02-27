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
botPoints = 0
playerPoints = 0

def addPoints(card):
    if (card == "As"):
        return 11
    elif (card == "Walet"):
        return 10
    elif (card == "Dama"):
        return 10
    elif (card == "Król"):
        return 10
    else:
        return int(card)

def takeCard(talia, sumOfPoints):
    noRepetition = 1
    cardNr = ""
    cardColor = ""

    while noRepetition:
        noRepetition = 0
        cardNr = figura[randint(0,12)]
        cardColor = kolor[randint(0,3)]
        choosenCard = cardNr + " " + cardColor
        for i in taliaBota:
            if(choosenCard == i):
                noRepetition = 1

        for i in taliaGracza:
            if(choosenCard == i):
                noRepetition = 1
    talia.append(choosenCard)
    return sumOfPoints + addPoints(cardNr)

def botAction(sumOfPoints):
    if (sumOfPoints < 18):
        sumOfPoints = takeCard(taliaBota, sumOfPoints)
        return 0, sumOfPoints
    else:
        return 1, sumOfPoints

while True:
    print ("Kto zaczyna?\n1. Ty\n2. Bot")
    whoStarts = input()
    if (whoStarts != "1" and whoStarts != "2"):
        system('cls')
        print ("Zła liczba")
    else:
        break

passBot = 0
passPlayer = 0

if(whoStarts == "2"):
    pasBot, botPoints = botAction(botPoints)

while True:
    system('cls')
    print ("Bot: ")
    print(taliaBota)
    print(" Suma: " + str(botPoints))
    print ("Gracz: ")
    print(taliaGracza)
    print(" Suma: " + str(playerPoints))

    if (playerPoints > 21):
        print("Przegrana")
        break

    if (botPoints > 21):
        print("Wygrana")
        break

    if (passPlayer == 1 and passBot == 1):
        if(botPoints > playerPoints):
            print("Przegrana")
            break
        elif(playerPoints > botPoints):
            print("Wygrana")
            break
        else:
            print("Remis")
            break

    print ("Wybierz akcję:\n1. Dobierz kartę\n2. Pas")

    while True:
        if(passPlayer == 0):
            chose = input()
            if(chose == "1"):
                playerPoints = takeCard(taliaGracza, playerPoints)
                break
            elif (chose == "2"):
                passPlayer = 1
                break
            else:
                print("Zły znak!")
        else:
            break

    passBot, botPoints = botAction(botPoints)
