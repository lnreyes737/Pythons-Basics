import random
#swimulate a biased coin flip and print outcome
N= 100
heads = 0
tails= 0
for i in range (N):
    flip_int= random. randint(1,100)

    if flip_int <= 30:
        heads=heads+1
    else:
        tails=tails+1
print("During this experiment you got heads", heads/N * 100, "percent of the time.")