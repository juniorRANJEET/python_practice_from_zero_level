print("welcome ramjhula")
height =  int(input("enter your height in cm "))
if height > 120:
    print("you can ride")
    age = int(input("enter your age "))
    if age <= 12:
        print("your ticket charges is ₹5")

    elif age >= 13 and age <= 18:
        print("you ve pay ₹7")
    elif age >= 19:
        print("you ve to pey ₹12")

else:
    print("you can not ride")
