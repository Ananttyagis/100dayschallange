print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster")
    bill = 0
    age = int(input("Please enter your age"))
    if age < 12:
        bill += 5
    elif age > 12 and age < 18:
        bill +=7
    else:
        bill +=12
    photo = str(input("Do you want to take photo? Yes or No"))
    if photo.upper() == "YES":
        bill +=3
        print(f"your bill is {bill}")
    else:
        print(f"Your bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")