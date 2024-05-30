print("bmi calculator")
height = float(input("enter ur height in m "))
weight = float(input("enter your weight in kg "))
bmi = round(weight/ (height*height), 2)
print(bmi)
if bmi < 18.5:
    print(f"your bmi is {bmi} and you are Underweight")
elif bmi < 24.9:
    print(f"your bmi is {bmi} and you are Normal")
elif bmi < 29.9:
    print(f"your bmi is {bmi} and you are Overweight")
elif bmi > 30:
    print(f"your bmi is {bmi} and you are Obese")