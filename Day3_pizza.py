print("Welcome to Pizza Deliveries")
size = input("What size of Pizza do you want? S, M or L: ")
price = 0
if size.upper() == "S":
    price += 15
elif size.upper() == "M":
    price += 20
elif size.upper() == "L":
    price += 25

pepperoni = input("Do you want pepperoni on your pizzea? Y or N: ")
if pepperoni.upper() == "Y" and size.upper() =="S":
    price += 2
else:
    price += 3
cheese = input("Do you want to add extra cheese? Y or N:")

if cheese.upper() == "Y":
    price += 1

print(f"Your final bill is ${price}")