import random


#random values between 0 and 1
for i in range(3):
    print(random.random())


#random value between 10 and 20
for i in range(3):
    print(random.randint(10,20))


#Picks a random position from this list
members = ["John","Marry","Bob"]
leader = random.choice(members)
print(leader)