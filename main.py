#Treasure HUNT GAME

# print(f"{q}{r}{e}{a}{s}{u}{r}{e}")
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("WELCOME TO TREASURE ISLAND.\nYOUR MISSION IS TO FIND THE TREASURE!!!")
rl=input("You\'re at across road. Where do you want to go? Type'left' or 'right'\n")
lrl=rl.lower()
if lrl=='left':
    sw=input("You come to a lake. There is an island in the middle of lake. Type 'wait' to wait for boat or type'swim' to swim across\n")
    swl=sw.lower()
    if swl=='wait':
        print("Now you have came to the island by boat.")
        d=input("Now there are three color doors is front of you which you like to chose and go? Type 'red'/'yellow'/'blue'\n")
        dl=d.lower()
        if dl=='yellow':
            print("You Win!! You have found the treasure...")
        elif d1=='red':
            print("It's a room full of fire.Game Over!!!")
        
        elif d1=='bule':
            print("You have got attacked by the beast.Game Over!!!")
    else:
        print("Game Over!!! Crocodile Ate you.")

else:
    print("You Fell Into a Hole.GAME OVER!!!")
