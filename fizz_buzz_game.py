# fizzBuzz game
print("welcome to FizzBuzz game ")
target = 100
for number in range (1,target+1):
    if number % 15 == 0:
        print("fizzbuzz")
    elif number % 3 == 0 :
        print("Fizz")
    elif number % 5 ==0 :
        print("buzz")
    else:
        print(number)
