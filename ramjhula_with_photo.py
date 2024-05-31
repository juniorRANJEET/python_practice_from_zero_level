print("welcome ramjhula")
height =  int(input("enter your height in cm "))
bill = 0
if height > 120:
    print("you can ride")
    age = int(input("enter your age "))
    if age <= 12:
        bill = 5
        print("your ticket charges is ₹5")

    elif age >= 13 and age <= 18:
        bill = 7
        print("you ve pay ₹7")
    elif age >= 19:
        bill = 12
        print("you ve to pey ₹12")
    want_to_photo = input("do you want to photo Y or N ")
    if want_to_photo == "Y" or "y" or "yes" or "YES":
        bill += 3
    print(f"your final bill is ₹{bill}")
else:
    print("you can not ride")