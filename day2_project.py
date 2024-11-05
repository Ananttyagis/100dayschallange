print ("Welcome to tip Calculator")

total_bill = input ("What is the total bill: $")
tip = input("How much tip would you like ot give ? 10, 12 or 15%? ")
people = input ("How many people to split the bill?")

total = int(total_bill) + (int(total_bill) * int(tip))/100

per_person = total / int(people)

final_amount = round(per_person, 2)

print (f"Each person should pay: {final_amount}")
