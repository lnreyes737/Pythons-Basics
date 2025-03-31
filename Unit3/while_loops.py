#Flip coin until we get 10 tails
#After we get ten tails we print the amount of heads

import random
tails=0
heads=0
flip=random.randint (1,2)
while tails <10:
    flip=random.randint (1,2)
    if flip==1:
        heads=heads +1
    else:
        tails=tails+1
print (heads)

#Use a while loop to find average sum of two dice rolls
#For each two dice rolls, calculate the sum
#Average the sum of the dice rolls over all simulations

N= int(input("How many times do you want to roll the dice "))
roll_count=0
sum_sum=0
while roll_count < N:
    roll=random.randint(1,6)
    roll2=random.randint(1,6)
    sum = roll+roll2
    print(sum)
    sum_sum=sum_sum+sum
    roll_count+= 1
sum_sum= sum_sum/N
print("The average sum is", sum_sum)