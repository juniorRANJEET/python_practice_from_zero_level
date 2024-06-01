print("welcome to pizza point center ")
size = input('what size pizza do you want "s" "m" "l" ')
add_peproni = input('do you want peporrini "y" or "n" ')
add_extra_cheese = input('do you want extra chesee "y" "n" ')
bill = 0
if size == "S":
    bill += 15


elif size =="M":
    bill += 20

elif size == "L":
    bill += 25

if add_peproni == "Y":
    if size == "S":
        bill +=2
    else:
        bill += 3

if add_extra_cheese =="Y":
    bill += 1

print(f"your total bill is ₹{bill}")


# print("Thank you for choosing Python Pizza Deliveries!")
# size = input('What size pizza do you want? "S", "M", or "L" ')
# add_pepperoni = input('Do you want pepperoni? "Y" or "N" ')
# extra_cheese = input('Do you want extra cheese? "Y" or "N" ')
#
# # Your code below this line 👇
# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25
#
# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3
#
# if extra_cheese == "Y":
#   bill += 1
#
# print(f"Your final bill is: ${bill}.")
