import random  
print ("The Coin Flip Game\n")

heads = 0
tails = 0
count = 0

while count<  2:
    coin = random.randrange(2)
    if coin == 0:
        heads = heads + 1
    else:
        tails = tails + 1
    count += 1

print ("Heads: ", heads)
print ("Tails: ", tails)

input("\nPress enter to exit.")