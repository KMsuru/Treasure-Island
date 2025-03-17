print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island 🏴‍☠️🏝")
print("Your mission is to find the treasure.💰")

direction = input("You are at a cross road.\nWould you like to left⬅ or right➡?:" )

if direction == "left" or direction == "LEFT" or direction == "Left":
    way = input("You have come to lake.\nThere is a island🏝 in the middle of the lake.\nWould you like to swim🏊‍♀️ or wait?:")

else:
    print("Game Over")

if way == "wait":
    door = input(
        "You arrive at the island unharmed.\nThere is a house with 3 doors🚪.\nOne Red, one Yellow and one Blue.\nWhich colour door you wanna choose?:")
else:
    print("Game Over")

if door == "Yellow" or door == "yellow":
    print("You found the treasure💰 You Win!🤩")
elif door == "Red" or door == "red":
    print("This room is full of fire🔥 You Burned!")
elif door == "Blue" or door == "blue":
    print("This room is full of monsters👹 You got Eaten!")
else:
    print("You have entered wrong value. Please try again.")
