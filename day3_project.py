print("Welcome to Treaure Island. Your mission is to find the treasure")

direction = input("Which direction you want to go? L ->left, R -> Right: ")
if direction.upper() == "L":
    activity = input("What do you want to do? S -> Swim or W -> Wait: ")
    if activity.upper() == "W":
        door = input("Which door you want to open? R -> Red, B -> Blue, Y -> Yellow: ")
        if door.upper() == "Y":
            print("You Won!")
        elif door.upper() == "R" or door.upper() =="B":
            print("Game over!")
    elif activity.upper() == "S":
        print("Eaten by Crokodial, Gameover!")
elif direction.upper() == "R":
    print("Hit by Car, Game over!")