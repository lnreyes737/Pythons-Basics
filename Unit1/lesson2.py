name = input("What is your name? ")
print("Hello " + name)
age = input("How old are you? ")
age = int(age)
print("Wow! You are",age)
if age > 50:
    print("YOU'RE OLD")
    print("Sorry",name)
    print("You have been old for",age-50,"years!")
else:
    print("Congragulations", name,"! You aren't old. Enjoy it.")
    print("You have",50-age, "years until you're old")