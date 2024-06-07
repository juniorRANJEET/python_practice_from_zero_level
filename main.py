# print("tip calculator")
# bill = float(input("total bill "))
# person = int(input("total person "))
# tips = int(input("tips percent to waiter like 5,10 or 20 "))
# total_bill = tips/100 * bill + bill
# per_person_bill = round(total_bill/person,2)
# print(f"per person have to pay {per_person_bill}")


print("tip calculator")
bill = float(input("total bill "))
person = int(input("total person "))
discount = int(input("discount percent like 5,10 or 20 "))
total_bill = bill - discount/100 * bill
per_person_bill = round(total_bill/person,2)
print(f"per person have to pay {per_person_bill}")