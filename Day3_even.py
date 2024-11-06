number = int(input("Please Enter a number to check"))
check_num = number % 2

if check_num == 0:
    print("Its a Even number")

else:
    print("Its a odd number")

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
else:
    print("overweight")