#!/usr/bin/env python
# -*- coding: cp1252 -*-
# THIS is a text game that will hopefully evolve!
#
#imports here 
import time
import random

#b
#definitions go here
turnOver = 0
turnValue = 1
Wait = 3

def spaceCopTurnAI():
    SCturn1=1
    SCturn2 = random.randint(3,5)
    SCturn3 = random.randint(1,5)
    preSCturn4 = random.randint(1,2)
    if preSCturn4 == 1:
        SCturn4 = 1
    if preSCturn4 == 2:
        SCturn4 = 5
    SCturn5 = 2

def testdef():
    print "SUCCEFUL LOAD"

def weaponCache():

    global weaponscache
    
    if weaponscache==1:
        weaponslist = " auto cannon(3)"
    if weaponscache==2:
        weaponslist= " auto cannon (3), Strobe ray (4)"
    if weaponscache==3:
        weaponslist= " auto cannon (3), Strobe ray (4), MineField (5)"
    if weaponscache==4:
        weaponslist= " auto cannon (3), Strobe ray (4), MineField (5), generic placeholder (6)"
    if weaponscache==5:
        weaponslist= " auto cannon (3), Strobe ray (4), MineField (5), generic placeholder (6), mining laser (7)"
    if weaponscache==6:
        weaponslist= " auto cannon (3), Strobe ray (4), MineField (5), generic placeholder (6), mining laser (7), particle cannon (8) "
    if weaponscache==7:
        weaponslist= " auto cannon (3), Strobe ray (4), MineField (5), generic placeholder (6), mining laser (7), particle cannon (8), Attack Drone (9)"
    if weaponscache==8:
        weaponslist= "Auto Cannon (3), Strobe Ray (4), MineField (5), Generic Placeholder (6), Mining Laser (7), Particle Cannon (8), Attack Drone (9), Nuclear Strike (10)"



    if Eweaponscache==1:
        Eweaponslist = " auto cannon(3)"
    if Eweaponscache==2:
        Eweaponslist= " auto cannon (3), Strobe ray (4)"
    if Eweaponscache==3:
        Eweaponslist= " auto cannon (3), Strobe ray (4), MineField (5)"
    if Eweaponscache==4:
        Eweaponslist= " auto cannon (3), Strobe ray (4), MineField (5), generic placeholder (6)"
    if Eweaponscache==5:
        Eweaponslist= " auto cannon (3), Strobe ray (4), MineField (5), generic placeholder (6), mining laser (7)"
    if Eweaponscache==6:
        Eweaponslist= " auto cannon (3), Strobe ray (4), MineField (5), generic placeholder (6), mining laser (7), particle cannon (8) "
    if Eweaponscache==7:
        Eweaponslist= " auto cannon (3), Strobe ray (4), MineField (5), generic placeholder (6), mining laser (7), particle cannon (8), Attack Drone (9)"
    if Eweaponscache==8:
        Eweaponslist= "Auto Cannon (3), Strobe Ray (4), MineField (5), Generic Placeholder (6), Mining Laser (7), Particle Cannon (8), Attack Drone (9), Nuclear Strike (10)"

def fiveTurns():

    global turn1
    global turn2
    global turn3
    global turn4
    global turn5
    
    print "First turn:"
    print "move(1) shields (2)" + weaponslist
    turn1=int(raw_input())
    print "Second turn:"
    print "move (1) shields (2)" + weaponslist
    turn2=int(raw_input())
    print "Third turn:"
    print "move (1) shields (2)" + weaponslist
    turn3=int(raw_input())
    print "Fourth turn:"
    print "move (1) shields (2)" + weaponslist
    turn4=int(raw_input())
    print "Fifth turn:"
    print "move (1) shields (2)" + weaponslist
    turn5=int(raw_input())

def Shields():
    if turn1 == 2:
        print "Shield activated"
        spacecopattack= spacecopattack - 10
    

def Mines():
    global turn1
    global turn2
    global turn3
    global turn4
    global turn5
    if turn1 == 5:
        while turnValue == 1:
            print "Where yar placin' a mine?"
            print "        " + space1 + "                      " + space14
            print "    " + space2 + space3 + space4 + "            " + space15 + space16 + space17
            print space5 + space6 + space7 + space8 + space9 + space18 + space19 + space20 + space21 + space22
            print " " + space10 + space11 + space12 + "         " + space23 + space24 + space25
            print "       " + space13 + space26
            jhonnysmine = int(raw_input())
            if jhonnysmine == shipPosition or enemyPosition:
                print "you can't place that there!"
            turnValue = 2
            turnOver = 1
        breakfix =0
    breakfix=27
        

    if turn2 == 5:
        if turnOver == 0:
            while turnvalue == 2:
                print "Where yar placin' a mine?"
                print "        " + space1 + "                      " + space14
                print "    " + space2 + space3 + space4 + "            " + space15 + space16 + space17
                print space5 + space6 + space7 + space8 + space9 + space18 + space19 + space20 + space21 + space22
                print " " + space10 + space11 + space12 + "         " + space23 + space24 + space25
                print "       " + space13 + space26
                jhonnysmine = int(raw_input())
                if jhonnysmine == shipPosition or enemyPosition:
                    print "you can't place that there!"
                turnValue = 3
                turnOver = 1
            breakfix = 30390
        breakfix =6

    if turn3 == 5:
        if turnOver == 0:
            while turnValue == 3:
                print "Where yar placin' a mine?"
                print "        " + space1 + "                      " + space14
                print "    " + space2 + space3 + space4 + "            " + space15 + space16 + space17
                print space5 + space6 + space7 + space8 + space9 + space18 + space19 + space20 + space21 + space22
                print " " + space10 + space11 + space12 + "         " + space23 + space24 + space25
                print "       " + space13 + space26
                jhonnysmine = int(raw_input())
                if jhonnysmine == shipPosition or enemyPosition:
                    print "you can't place that there!"
                turnValue = 4
                turnOver = 1
            breakfix =2000
        breakfix = 23

    if turn4 == 5:
        if turnOver==0:
            while turnValue == 4:
                print "Where yar placin' a mine?"
                print "        " + space1 + "                      " + space14
                print "    " + space2 + space3 + space4 + "            " + space15 + space16 + space17
                print space5 + space6 + space7 + space8 + space9 + space18 + space19 + space20 + space21 + space22
                print " " + space10 + space11 + space12 + "         " + space23 + space24 + space25
                print "       " + space13 + space26
                jhonnysmine = int(raw_input())
                if jhonnysmine == shipPosition or enemyPosition:
                    print "you can't place that there!"
                turnValue = 5
            breakfix = 20
        breakfix=2
    

    if turn5 == 5:
        if turnOver == 0:
            while turnValue == 5:
                print "Where yar placin' a mine?"
                print "        " + space1 + "                      " + space14
                print "    " + space2 + space3 + space4 + "            " + space15 + space16 + space17
                print space5 + space6 + space7 + space8 + space9 + space18 + space19 + space20 + space21 + space22
                print " " + space10 + space11 + space12 + "         " + space23 + space24 + space25
                print "       " + space13 + space26
                jhonnysmine = int(raw_input())
                if jhonnysmine == shipPosition or enemyPosition:
                    print "you can't place that there!"
                turnValue = 1
            breakfix = 33

    

    



def movingForPastOne():
    global turn1
    global turn2
    global turn3
    global turn4
    global turn5
    global turnOver
    global turnValue
    if turn1 == 1:
        if turnOver == 0:
            while turnValue == 1:
                print "        " + space1 + "                      " + space14
                print "    " + space2 + space3 + space4 +            " " + space15 + space16 + space17
                print space5 + space6 + space7 + space8 + space9 + space18 + space19 + space20 + space21 + space22
                print " " + space10 + space11 + space12 + "         " + space23 + space24 + space25
                print "       " + space13 + space26
                print "So whare do ye be wanton' tee move now eh?"
                

    if turn2 == 1:
        if turnOver == 0:
            while turnValue == 2:
                print "        " + space1 + "                      " + space14
                print "    " + space2 + space3 + space4 +            " " + space15 + space16 + space17
                print space5 + space6 + space7 + space8 + space9 + space18 + space19 + space20 + space21 + space22
                print " " + space10 + space11 + space12 + "         " + space23 + space24 + space25
                print "       " + space13 + space26
                print "So whare do ye be wanton' tee move now eh?"
                

    if turn3 == 1:
        if turnOver == 0:
            while turnValue == 3:
                print "        " + space1 + "                      " + space14
                print "    " + space2 + space3 + space4 +            " " + space15 + space16 + space17
                print space5 + space6 + space7 + space8 + space9 + space18 + space19 + space20 + space21 + space22
                print " " + space10 + space11 + space12 + "         " + space23 + space24 + space25
                print "       " + space13 + space26
                print "So whare do ye be wanton' tee move now eh?"
                

    if turn4 == 1:
        if turnOver == 0:
            while turnValue == 4:
                print "        " + space1 + "                      " + space14
                print "    " + space2 + space3 + space4 +            " " + space15 + space16 + space17
                print space5 + space6 + space7 + space8 + space9 + space18 + space19 + space20 + space21 + space22
                print " " + space10 + space11 + space12 + "         " + space23 + space24 + space25
                print "       " + space13 + space26
                print "So whare do ye be wanton' tee move now eh?"
                

    if turn5 == 1:
        if turnOver == 0:
            while turnValue == 5:
                print "        " + space1 + "                      " + space14
                print "    " + space2 + space3 + space4 +            " " + space15 + space16 + space17
                print space5 + space6 + space7 + space8 + space9 + space18 + space19 + space20 + space21 + space22
                print " " + space10 + space11 + space12 + "         " + space23 + space24 + space25
                print "       " + space13 + space26
                print "So whare do ye be wanton' tee move now eh?"
                turnValue = turnValue + 1
                if turnValue == 6
                    turnOver = 1
                    turnValue = 1

    turnOver=0

def moveingForTwo():
        if turn2 == 1:
            print "        " + space1 + "                      " + space14
            print "    " + space2 + space3 + space4 +            " " + space15 + space16 + space17
            print space5 + space6 + space7 + space8 + space9 + space18 + space19 + space20 + space21 + space22
            print " " + space10 + space11 + space12 + "         " + space23 + space24 + space25
            print "       " + space13 + space26
            print "So whare do ye be wanton' tee move now eh?"

jhonnysmine=666
enemyPosition = "spaceTwenty"

def validatePositionR():
    global shipPosition
    global testPosition
    global spcThree
    global spcSix
    global spcTwo
    global spcFour
    global spcFive
    testPosition = int(raw_input())
    if shipPosition == "spaceOne":
        spcThree = "ok"

    if shipPosition == "spaceTwo":
        spcThree="ok"
        spcSix="ok"

    if shipPosition == "spaceThree":
        spcTwo="ok"
        spcOne="ok"
        spcFour="ok"
        spcSeven="ok"

    if shipPosition =="spaceFour":
        spcThree="ok"
        spcEight="ok"

    if shipPosition == "spaceFive":
        spcSix="ok"

    if shipPosition == "spaceSix":
        spcTwo = "ok"
        spcFive = "ok"
        spcTen = "ok"
        spcSeven="ok"

    if shipPosition == "spaceSeven":
        spcThree="ok"
        spcEleven="ok"
        spcSix="ok"
        spcEight="ok"
	    
    if testPosition == 1:
        valVar = spcOne
    if testPosition == 2:
        valVar = spcTwo
    if testPosition == 3:
        valVar = spcThree
    if testPosition == 4:
        valVar = spcFour
    if testPosition == 5:
        valVar = spcFive
    if testPosition == 6:
        valVar = spcSix
    if testPosition == 7:
        valVar = spcSeven
    if testPosition == 8:
        valVar = spcEight
    if testPosition == 9:
        valVar = spcNine
    if testPosition == 10:
        valVar = spcTen
    if testPosition == 11:
        valVar = spcEleven
    if testPosition == 12:
        valVar = spcTwelve
    if testPosition == 13:
        valVar = spcThirteen
    if testPosition == 14:
        valVar = spcFourteen
    if testPosition == 15:
        valVar = spcFifteen
    if testPosition == 16:
        valVar = spcSixteen
    if testPosition == 17:
        valVar = spcSeventeen
    if testPosition == 18:
        valVar = spcEighteen
    if testPosition == 19:
        valVar = spcNineteen
    if testPosition == 20:
        valVar = spcTwenty
    if testPosition == 21:
        valVar = spcTwentyone
    if testPosition == 22:
        valVar = spcTwentytwo
    if testPosition == 23:
        valVar = spcTwentythree
    if testPosition == 24:
        valVar = spcTwentyfour
    if testPosition == 25:
        valVar = spcTwentyfive
    if testPosition == 26:
        valVar = spcTwentysix

    if shipPosition == testPosition:
        print "You're already there!"

    if valVar == "ok":
        shipPosition = testPosition
        



shipPosition = "spaceSeven"

#important but still not sure why
def moveTest():
    Goon = "true"
    if Goon == "true":
        if enemyPosition == "spaceOne":
            space1 = "(E)"
        if enemyPosition == "spaceTwo":
            space2 = "(E)"
        if enemyPosition == "spaceThree":
            space3 = "(E)"
        if enemyPosition == "spaceFour":
            space4 = "(E)"
        if enemyPosition == "spaceFive":
            space5="(E)"
        if enemyPosition == "spaceSix":
            space6="(E)"
        if enemyPosition == "spaceSeven":
            space7="(E)"
        if enemyPosition == "spaceEight":
            space8="(E)"
        if enemyPosition == "spaceNine":
            space9="(E)"
        if enemyPosition == "spaceTen":
            space10="(E)"
        if enemyPosition == "spaceEleven":
            space11="(E)"
        if enemyPosition == "spaceTwelve":
            space12="(E)"
        if enemyPosition == "spaceThirteen":
            space13="(E)"
        if enemyPosition == "spaceFourteen":
            space14="(E)"
        if enemyPosition == "spaceFifteen":
            space15="(E)"
        if enemyPosition == "spaceSixteen":
            space16="(E)"
        if enemyPosition == "spaceSeventeen":
            space17="(E)"
        if enemyPosition == "spaceEighteen":
            space18="(E)"
        if enemyPosition == "spaceNineteen":
            space19="(E)"
        if enemyPosition == "spaceTwenty":
            "space20=(E)"
        if enemyPosition == "spaceTwentyOne":
            space21="(E)"
        if enemyPosition == "spaceTwentyTwo":
            space22="(E)"
        if enemyPosition == "spaceTwentyThree":
            space23="(E)"
        if enemyPosition == "spaceTwentyFour":
            space24="(E)"
        if enemyPosition == "spaceTwentyFive":
            space25="(E)"
        if enemyPosition == "spaceTwentySix":
            space26="(E)"
        if shipPosition == "spaceOne":
            space1 = "(S)"
        if shipPosition == "spaceTwo":
            space2 = "(S)"
        if shipPosition == "spaceThree":
           space3 = "(S)"
        if shipPosition == "spaceFour":
            space4="(S)"
        if shipPosition == "spaceFive":
            space5="(S)"
        if shipPosition == "spaceSix":
            space6="(S)"
        if shipPosition == "spaceSeven":
            space7="(S)"
        if shipPosition == "spaceEight":
            space8="(S)"
        if shipPosition == "spaceNine":
            space9="(S)"
        if shipPosition == "spaceTen":
            space10="(S)"
        if shipPosition == "spaceEleven":
            space11="(S)"
        if shipPosition == "spaceTwelve":
            space12="(S)"
        if shipPosition == "spaceThirteen":
            space13="(S)"
        if shipPosition == "spaceFourteen":
            space14="(S)"
        if shipPosition == "spaceFifteen":
            space15="(S)"
        if shipPosition == "spaceSixteen":
            space16="(S)"
        if shipPosition == "spaceSeventeen":
            space17="(S)"
        if shipPosition == "spaceEighteen":
            space18="(S)"
        if shipPosition == "spaceNineteen":
            space19="(S)"
        if shipPosition == "spaceTwenty":
            space20="(S)"
        if shipPosition == "spaceTwentyOne":
            space21="(S)"
        if shipPosition == "spaceTwentyTwo":
            space22="(S)"
        if shipPosition == "spaceTwentyThree":
            space23="(S)"
        if shipPosition == "spaceTwentyFour":
            space24="(S)"
        if shipPosition == "spaceTwentyFive":
            space25="(S)"
        if shipPosition == "spaceTwentySix":
            space26="(S)" 



def Movement():
    movingForPastOne()
    validatePositionR()
    moveTest()

def ResetBoard():
    space1 = "(1 )"
    space2 = "(2 )"
    space3 = "(3 )"
    space4 = "(4 )"
    space5 = "(5 )"
    space6 = "(6 )"
    space7 = "(7 )"
    space8 = "(8 )"
    space9 = "(9 )"
    space10 = "(10)"
    space11 = "(11)"
    space12 = "(12)"
    space13 = "(13)"
    space14 = "(14)"
    space15 = "(15)"
    space16 = "(16)"
    space17 = "(17)"
    space18 = "(18)"
    space19 = "(19)"
    space20 = "(20)"
    space21 = "(21)"
    space22 = "(22)"
    space23 = "(23)"
    space24 = "(24)"
    space25 = "(25)"
    space26 = "(26)"



moneyMoney = 1,000
rivetRivets = 2,000
space1 = "(1 )"
space2 = "(2 )"
space3 = "(3 )"
space4 = "(4 )"
space5 = "(5 )"
space6 = "(6 )"
space7 = "(7 )"
space8 = "(8 )"
space9 = "(9 )"
space10 = "(10)"
space11 = "(11)"
space12 = "(12)"
space13 = "(13)"
space14 = "(14)"
space15 = "(15)"
space16 = "(16)"
space17 = "(17)"
space18 = "(18)"
space19 = "(19)"
space20 = "(20)"
space21 = "(21)"
space22 = "(22)"
space23 = "(23)"
space24 = "(24)"
space25 = "(25)"
space26 = "(26)"

spaceOne = 1
spaceTwo = 2
spaceThree = 3
spaceFour = 4
spaceFive = 5
spaceSix = 6
spaceSeven = 7
spaceEight = 8
spaceNine = 9
spaceTen = 10
spaceEleven = 11
spaceTwelve = 12
spaceThirteen = 13
spaceFourteen = 14
spaceFifteen = 15
spaceSixteen = 16
spaceSeventeen = 17
spaceEighteen = 18
spaceNineteen = 19
spaceTwenty = 20
spaceTwentyOne = 21
spaceTwentyTwo = 22
spaceTwentyThree = 23
spaceTwentyFour = 24
spaceTwentyFive = 25
spaceTwentySix = 26

#
#Game Starts

userName = raw_input ("Please enter your name.")
print "Welcome Captain", userName
gameStart = 1
password = int(raw_input("Do you have a password? If not enter 1"))
if password == 72:
    gameStart = 0
if password == 2:
    Wait = 0.1
while gameStart == 1:
    print "You are an Irish space pirate stuck on the planet Geotria, in the Trestric Sector."  
    time.sleep(Wait)
    #Loading
    print "Building StarBoat."
    time.sleep(Wait)
    print "Building StarBoat."
    time.sleep(Wait)  
    print "      /\ "
    time.sleep(Wait)
    print "     /  \ "
    time.sleep(Wait)
    print "    / __ \ "
    time.sleep(Wait)
    print "   | /  \ | "
    time.sleep(Wait)
    print "   | \__/ |"
    time.sleep(Wait)
    print "   |      |"
    time.sleep(Wait)
    print "   |      |"
    time.sleep(Wait)
    print "   |      |"
    time.sleep(Wait)
    print "   |      |"
    time.sleep(Wait)
    print "  /|      |\ "
    time.sleep(Wait)
    print " | |      | |"
    time.sleep(Wait)
    print " | |      | |"
    time.sleep(Wait)
    print " \/|      |\/ "
    time.sleep(Wait)
    print "   \______/ "
    time.sleep(Wait)
    #
    #
    #
    #
    #story
    print "*One Day an executive, Mr. Hansen, from ZenCorp approaches you in a black tuxedo.*"
    time.sleep(Wait)
    print "(ZenCorp is one of the largest companies in your sector and has funded many a space pirate, but are known to not be trustworthy and to alert the authorities if things don/'t go their way.)"
    time.sleep(Wait)
    print "'Excuse me", userName, "',says Mr. Hansen, 'I have come with a proposal. Your piloting skills are famous on this planet, we also hear of your dreams to fly a larger ship, so ZenCorp will fund you if, and only if, you do us a small favor. What do you say?'"
    #first choice =)


    firstChoice = int(raw_input("1 accepts the offer 2 declines"))
    if firstChoice == 1:
        print "You won’t regret this!"
        time.sleep(Wait)
        print "Meet us next week at hangar 7 for your ship and more details. It’s your job to get a crew though!"
        time.sleep(Wait)
        print "*An evil smile spreads across his face.*"
        time.sleep(Wait)
        
        print "'Welcome captain, this is your new ship."
        #
        #ship randomizer
            #
            #
        shipHead = random.randint(1,3)#(0,3)
        if shipHead is 1:
            print "         /\ "
            print "        /  \ "
            print "      _/    \_ "
        if shipHead == 2:
            print "       ______ "
            print "      |______| "
            print "      |      | "
            print "      |      | "
        if shipHead == 3:
            print "        ____ "
            print "       /____\ "
            print "      |      | "
            print "      |      | "
        shipBodyMid = random.randint(1,3)#(0,3)
        if shipBodyMid == 1:
            print "     /        \ "
            print "    /          \ "
            print "   |            | "
            print "  /|            |\ "
            print " /_|            |_\ "
            print "   |+=+=+=+=+=+=| "
            print "   |=+=+=+=+=+=+| "
            print "   |            | "
            print "   |            | "
            print "   |            | "
        if shipBodyMid == 2:#is 2
            print "     |        | "
            print "     |        | "
            print "     |        | "
            print "     |        | "
            print "     |        | "
            print "     |        | "
            print "     |        | "
            print "   __|        |__ "
            print "  |              | "
            print "  |              | "
        if shipBodyMid == 3:#is 3
            print "      \      / "
            print "       |    | "
            print "       |    | "
            print "      /      \ "
            print "     |        | "
            print "     |        | "
            print "     |        | "
            print "    /|        |\ "
            print "   /_|        |_\ "
            print "    /          \ "
            print "   /            \ "
        shipEngine = random.randint(1,2)
        if shipEngine == 1:
            print "  /______________\ "
        if shipEngine == 2:
            print "   \            / "
            print "   /|          |\ "
            print "  /_|__________|_\ "
            print "      /______\  "
        shipAttack = 100  #this line is for what purpose?
        if shipHead == 1:
            shipAttack = 75  #should do randomization here, with ranges given as possibilities for each part, obvi w/ a part with better attack having a range built to have better likelyhood of better attack
        if shipHead == 2:
            shipAttack = 40
        if shipHead == 3:
            shipAttack = 58
        if shipBodyMid == 1:
            shipAttack = shipAttack + 10  #also should start ship attack at zero and just add up, start with eg. shipAttack=shipAttack+75, then +10, etc
        if shipBodyMid == 2:
            shipAttack = shipAttack + 20
        if shipBodyMid == 3:
            shipAttack = shipAttack + 30
        print "Attack", shipAttack
        shipDefence = 100
        if shipBodyMid == 1:
            shipDefence = 75
        if shipBodyMid == 2:
            shipDefence = 57
        if shipBodyMid == 3:
            shipDefence = 40
        if shipHead == 1:
            shipDefence = shipDefence + 12
        if shipHead == 2:
            shipDefence = shipDefence + 36
        if shipHead == 3:
            shipDefence = shipDefence + 24
        print "Defence", shipDefence
        shipHealth = 800
        if shipEngine == 1:
            shipHealth = 801
        if shipEngine == 2:
            shipHealth = 725
            shipAttack = shipAttack + 10
            shipDefence = shipDefence + 10
        print "HP", shipHealth
                #
                #more story
                #
                #
        print "You’re finally flying! of course you have no crew, or friends, but we can figure that out later!"
        time.sleep(6)
        print "You see a planet. Land on it?"
        planetOne = int(raw_input("1 lands 2 continues on"))
        if planetOne == 1:
            print "You land successfully"
            print "This planet has almost no commercial stores but you can still look for a crew"
            print "Planet one is a merchant safehold."
            print "Would you like to check the stores?"
            stores = int(raw_input(""))
            if stores == 1:
                print "available for purchase are"
                print "Rivets = 1"
                print "Laser Cannon = 2"
                boughtItem1 = int(raw_input("What will you buy?(press 0 for nothing)"))
            if boughtItem1 == 1: 
                shipRivets = 10000




            print "leave? 1 to leave"
            

          







        #this section will be Jared’s combat code.  I suggest for now I hash through it, then we can look it all over 
        # maybe a gameboard like so?  And when you take a shot, it is aimed based on spaces

        #                         ( )            ( )
        #                      ( )( )( )      ( )( )( )
        #                   ( )( )( )( )( )( )( )( )( )( )
        #                      ( )( )( )      ( )( )( )
        #                         ( )            ( )

        Eweaponscache= random.randint(0,8)
        #ship health code
        enemyPosition = 20
        shipPosition = 7

        #space cop health
        SCHP = 50
        SCBH = 40
        SCFH = 60
        SCEH = 30
        SCBH = 30
        Eweaponscache

        #the below figures are placeholders

        shipHealth = 100
        bridgehealth=40
        fuselagehealth=60
        enginehealth=30
        boostershealth=30
        weaponscache=8

        #weapons cache code has been placed in a module
        #the following weapons are placeholders






    print "An enemy has appeared!  Engage (1)? Or run like a coward (2)? 3 for debug."
    balls=int(raw_input())
    if balls == 1:
        print "You warm up the cannons."
        spacecophealth = 10 * random.randint(6,10)#intger should reflect level
        spacecopbridge = 10 * random.randint (2,5)#
        spacecopfuselage = 10 * random.randint (4,7)#
        spacecopengine = 10 * random.randint (1,4)#
        spacecopboosters = 10 * random.randint (1,3)#
        spacecopattack = 5*random.randint(11,12)# It should if hit at full damage, kill you in 6-7 hits.
        shipPosition = "spaceSeven"
        enemyPosition = "spaceTwenty"
        weaponscache = 1


        playersquare=7
        spacecopsquare=20
        if shipHealth > 0 and spacecophealth > 0:
            print "Your health:"
            print shipHealth
            print "Space Cop health:"
            print spacecophealth
            print "Planning Stage"
            weaponscache = 1
            weaponCache()
            weaponslist = " auto cannon (3), Strobe ray (4), MineField (5)"
            #round 1
                #turn 1
            fiveTurns()
            Movement()
            Shields()
            Mines()
                #turn 2
            Movement()
            Shields()
            Mines()
                #turn 3
            Movement()
            Shields()
            Mines()
                #turn 4
            Movement()
            Shields()
            Mines()
                #turn 5
            Movement()
            Shields()
            Mines()

    if balls==3:
        Movement()

            
    def enemyMovementAI():
        if shipPosition == 5 or 6 or 7 or 8 or 9 or 18 or 19 or 20 or 21 or 22 and enemyPosition == 5 or 6 or 7 or 8 or 9 or 18 or 19 or 20 or 21 or 22:
            randomMove = random.randint(1,9)
            if randomMove == 1 or 3 or 6:
                enemyPosition = random.randiny(15,17)
            if randomMove == 2 or 4:
                enemyPosition = random.randint(23,25)
            if randomMove == 5:
                halfRandomMoves = random.randint(1,2)
                if halfRandomMoves == 1:
                    enemyPosition = 19
                if halfRandomMoves == 2:
                    enemyPosition = 22










    






    

        

   


spacecophealth=0
            
if spacecophealth == 0:
    print "Your enemy explodes in a glorious fireball."
    print "Some money falls from the corpse of the dead cop."
    print "Found 100 Dollars"
    moneyMoney = moneyMoney + 100
    print "Money: " + moneyMoney


    if shipHealth == 0:
        print "You’re dead, loser."
            
    if balls == 2:
        print "Your lack of testes disgusts me."


    if firstChoice == 2:
            print "You'll regret this."
