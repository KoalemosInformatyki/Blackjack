from os import system
from random import randint

def botAction(whoStarts):
    if(whoStarts == "2"):
        print("No gram")
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
