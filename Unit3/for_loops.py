#For loop
#In each ineration(ineration i), printout i copies of "Hello"


for i in range (3,10,2):
    print("i =",i,"Hello " *i)
print("The end")








#Simulate bee honey production in one week


import random
# Number of forager bees in the hive
need=20000
has=0
deposits=0

for hour in range (7*18):
    #A number of bees that have nectar, drop it off
    dropoff=random.randint(
        has//4,
        3*has//4
    )


    #A bee without nectar may collect it from nearby flowers
    pickups=random.randint (
        need //4,
        3*need//4
    )

    #Update population counts after bees get nectar
    has=has+pickups-dropoff
    need= need-pickups+dropoff
    deposits=deposits+dropoff
   
    #print(str(has) + "(has)")
    #print(str(need)+ "(needs)")

print ("Total nectar deposits =", deposits)
print("Grams of honey produced over a week=", deposits//90)