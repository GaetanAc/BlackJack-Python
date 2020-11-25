import time
import random

cartes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

random.shuffle(cartes)

print(" BLACK JACK Python")
time.sleep(1)
dealercards = []
playercards = []
time.sleep(1)
while len(dealercards) != 2:
    random.shuffle(cartes)
    dealercards.append(cartes.pop())
    if len(dealercards) == 2:
        print(" Les cartes du dealer sont X ", dealercards[1])

while len(playercards) != 2:
    random.shuffle(cartes)
    playercards.append(cartes.pop())
    if len(playercards) == 2:
        print(" Les cartes de player sont  ", playercards)
        print(" Le total de player est ", sum(playercards))

if sum(dealercards) == 21:
    print(" Dealer gagne par BLACK JACK", dealercards)
    time.sleep(5)
    exit()
if sum(playercards) == 21:
    print(" Player gagne par BLACK JACK ")
    time.sleep(5)
    exit()

def dealer_choice():


    print(" Le dealer possède un total de  " + str(sum(dealercards)) + " avec les cartes ", dealercards)

    if sum(playercards) == sum(dealercards):
        print(" Egalité ")
        exit()

    if sum(dealercards) == 21:
        if sum(playercards) < 21:
            print(" Le dealer gagne ")
        elif sum(playercards) == 21:
            print(" Egalité ")
        else:
            print(" Le dealer gagne ")

    elif sum(dealercards) < 21:
        if sum(dealercards) > sum(playercards):
            print("Dealer gagne")
        elif sum(dealercards) < sum(playercards):
            random.shuffle(cartes)
            dealercards.append(cartes.pop())
            print(" Le dealer possède un total de  " + str(sum(dealercards)) + " après avoir tiré ", dealercards)
            if sum(dealercards) > 21:
                print(" Vous êtes le vainqueur")
            elif sum(dealercards) == 21 and sum(playercards) < 21:
                print(" Le dealer gagne avec les cartes " +  str(sum(dealercards)) + " pour un total de ", dealercards)
            elif sum(dealercards) == 21 and sum(playercards) == 21 :
                print(" Egalité ")
            while sum(dealercards) < 21:
                random.shuffle(cartes)
                dealercards.append(cartes.pop())
                print(" Le dealer possède un total de " + str(sum(dealercards)) + " après avoir tiré ", dealercards)
                if sum(dealercards) > 21:
                    print(" Vous êtes le vainqueur")
                elif sum(dealercards) == 21 and sum(playercards) < 21:
                    print(" Le dealer gagne avec un total de " +  str(sum(dealercards)) + " avec les cartes", dealercards)
                elif sum(dealercards) > sum(playercards):
                    print (" Le dealer gagne avec un total de " +  str(sum(dealercards)) + " avec les cartes ", dealercards)
                elif sum(dealercards) == 21 and sum(playercards) == 21:
                    print(" Egalité ")


while sum(playercards) < 21:

    k = int(input(" Appuyer sur 1 pour tirer /0 pour rester "))
    if k == 1:
        random.shuffle(cartes)
        playercards.append(cartes.pop())
        print(" Vous avez un total de  " + str(sum(playercards))+ " avec les cartes ", playercards)
        if sum(playercards) > 21:
            print(" Le dealer gagne ")
            time.sleep(5)
        elif sum(playercards) == 21:
            print(" Vous êtes le vainqueur  !! ")
            time.sleep(5)

    else:
        dealer_choice()
        time.sleep(5)
        break