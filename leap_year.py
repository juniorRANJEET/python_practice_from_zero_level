print("check whelther a year is leap yr or not")
year = int (input("enter year which you want to check "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"enter year {year} is leap")
        else:
            print(f"enter year {year} is not leap")
    else:
        print(f"enter year {year} is leap")
else:
    print(f"enter year {year} is not leap")