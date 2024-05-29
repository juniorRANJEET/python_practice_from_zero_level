print("welcome to tip calculator")
total_bill = float(input("what is the total bill "))
tip = float(input("how much tips would you like to give 10,12 or 15 percentage "))
number_of_people= int(input("how many number to split the bill "))
bill_with_tip = tip /100 * total_bill + total_bill
bill_per_person = round(bill_with_tip / number_of_people ,2)
print(f"per person have to pay ₹{bill_per_person} ")