############################
### Author: Kerim        ###
###                      ###
############################

#!/usr/bin/env python3

from sys import exit
from pip._vendor.distlib.compat import raw_input

## Variables

tplayer_alive = True
bombcarrier_alive = True
AK47 = False

## Storyline

# Level 1

def level_1():
    print ("You spawned in Dust2 on CT side")
    print ("You picked up full armor and a M4A1-S")
    print ("It seems you are on your own. Where are you going?")
    print ("You could go 'A', 'B', or 'mid' ")

    choice = raw_input("> ")

    if "A" in choice:
        level_2()
    elif "B" in choice:
        level_4()
    elif "mid" in choice:
        print("""You go mid and start peeking double doors. You see nothing yet. You hear a loud bang! It is the AWP player in T Spawn. He killed you with his AWP. You died.""")
        game_over()
    else:
        level_1()

# Level 2

def level_2():
    print ("You run to A long and wait for the enemy come from connector.")
    print ("You get flashed and and immediately start shooting")
    print ("Well done the terrorist lies dead on the ground")
    print ("You smoke connector and wait for movement sounds")
    print ("There are no sounds. What do you do next?")
    print ("You could go 'push' to T spawn, Go back to 'car' on A long or go back and head to 'B' ")

    choice = raw_input("> ")

    if "B" in choice:
        print("""You turn around and start pushing B through CT spawn. When you check double doors to see if its clear you get electrocuted with a Zeus. You Died.""")
        game_over()
    elif "push" in choice:
        level_3()
    elif "car" in choice:
        level_5()
    else:
        level_2()

# Level 3

def level_3():

    global tplayer_alive
    global AK47

    if tplayer_alive:
        print ("You push through connector")
        print ("No enemy to see so you make your way up to T spawn")
        print ("You spot a AWP player on T spawn")
        print ("You start walking silently up to the enemy")
        print ("You have a few options what you can do")
        print ("You could try to 'knife' him, 'shoot' him in his head, pick up the 'AK47' that's on the ground or 'pass' him to B side. You could also go 'back' to A long ")
        print ("What do you do?")

        choice = raw_input("> ")

        if "pass" in choice:
            print("""You tried to sneak behind the AWP player. When he turned around to pick his AK47 he noticed you and shot you without scoping. You died. Never try this again!""")
            game_over()
        elif "knife" in choice:
            print ("""You get closer to the player. You pull out your knife and stab him in his back. He died knowing he made a stupid mistake not checking his back.""")
            tplayer_alive = False
            level_4()
        elif "AK47" in choice:
            print ("""You pick up the AK47. Always pick up the AK47. You shoot the enemy with it in his head. That should teach him! Never watch one spot for so long!""")
            tplayer_alive = False
            AK47 = True
            level_4()
        elif "shoot" in choice:
            print(""""You tried to shoot the enemy player. You hit him 2 times but it was not deadly. This was not a smart choice. The enemy player turned around and one shot you. You died! """)
            game_over()
        elif "back" in choice:
            level_2()
        else:
            level_3()

# Level 4

def level_4():

    global bombcarrier_alive

    if bombcarrier_alive:

        print ("You start pushing from T spawn to B tunnels")

        if AK47:
            print ("""You run through the tunnel and pick up your AK47 and start pre firing corners.
The bomb carrier was still waiting for his team mates to clear CT spawn.
He gets to catch all of the bullets that you were firing.
He dies and the bomb falls in front of you. You won this round champ!""")
            bombcarrier_alive = False
            game_over()

        else:

            print ("You can go 'lower' tunnels or pop-flash B site and 'rush' B to give all you have")
            print ("What's it going to be champ?")

        choice = raw_input("> ")

        if "lower" in choice:
            print(""""You head in to the lower tunnels. Thank god it's clear. You start moving through the double doors and start moving to B. You did not noticed the player in CT spawn hiding. He empties his magazine on you. You died.""")
            game_over()
        elif "rush" in choice:
            print("""There we go! You run through the tunnels and pop a flashbang.
Everybody on B side is blind. You spot one enemy behind the car.
You one tap him. Dead as he could be.
Now you rush default side. You see the enemy bomb carrier. You empty your M4A1-S on him.
 You won the round champ!  """)
            bombcarrier_alive = False
            game_over()
        else:
            level_4()

# Level 5

def level_5():

    print("You go back to the car. You spot one player coming from short. You shoot him and see none coming to A side.")
    print("This brings some suspicion. What do you do next? 'push' through CT spawn to B? or go 'connector'?")

    choice = raw_input("> ")

    if "push" in choice:
        print("You start pushing CT. You check double doors. Nobody here. So you go to peek window on B side. When you start peeking, you get headshotted immediately. You lost the round. ")
        game_over()
    elif "connector" in choice:
        level_3()
    else:
        level_5()

## START default

def start():
    level_1()

## GAME OVER

def game_over():

    global tplayer_alive
    global bombcarrier_alive
    global AK47

    tplayer_alive = True
    bombcarrier_alive = True
    AK47 = False

    print ("Do you want to play again? (y / n)")

    choice = ""
    while choice != "y" and choice != "n":
        choice = raw_input("> ")
        if choice == "y":

            start()
        elif choice == "n":
            exit(0)


## Default

start()
