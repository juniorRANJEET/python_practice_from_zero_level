print("love calculator game")
name1 = input("what is ur name ")
name2 = input("what is their name ")
combined_name = name1 + name2
lower_name = combined_name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

firs_digt = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

second_digt = l + o + v + e

score = int(str(firs_digt) + str(second_digt))

if (score <= 10 ) and (score >= 90) :
    print(f"your score is {score} , and you can go for coke and mentos")
elif (score <= 40) and (score >= 50) :
    print(f"your love score is {score}  and you live together ")

else:
    print(f"your score is {score}")