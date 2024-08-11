print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input("Do you go left or right? ").lower()
if choice1 == "left":
    print(
        "You enter the dark forest and you have 2 ways to go. You can by road or you can go through the forest."
    )
    choice2 = input("Do you go by road or through the forest? ").lower()
    if choice2 == "road":
        print("you have selected a better way to go.")
        print("wait for some time still the vehicle arives .")
        choice3 = input(
            "choose the vehicle through which you have to go  bus or car or bike.? "
        ).lower()
        if choice3 == "bike":
            print(
                "You selected bike which can go faster and through narrow road also and you have reached treasure! You win!"
            )
        elif choice3 == "bus":
            print(
                "You selected bus ,sorry you have to wait untill the bus gets filled and bus cant go through narrow road  . Game over."
            )
        elif choice3 == "car ":
            print(
                "You selected car,sorry you cant go through narrow road . Game over."
            )
        else:
            print("You selected  a vehicle that doesn't exist. Game over.")
else:
  print("You have selected a way that doesn't exist. Game over.")

