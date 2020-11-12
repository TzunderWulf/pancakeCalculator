
# the PANCAKE counter, to see how much pancakes you can make
from time import sleep
from sys import exit

# this measeruments are for a serving of four pancakes
minAmountMilk = 350 #milliliter
minAmountFlour = 200 #grams
minAmountEggs = 2

# loading...
user = input("Hello?")
sleep(2)
print("Hello " + user)
sleep(2)
print("Program loading...")
sleep(5)
print("Program done loading")
sleep(2)

# amount of milk (input from user)
amountMilk = int(input("How much milk do you have (in milliliters)?"))
print("Calculating...")
sleep(2)

# amount of flour (input from user)
amountFlour = int(input("How much flour do you have (in grams)?"))
print("Calculating...")
sleep(2)

# amount of eggs (input from user)
amountEggs = int(input("How many eggs do you have?"))
print("Calculating...")
sleep(2)

# checks if there is even enough to make one pancake
if amountFlour < minAmountFlour or amountEggs < minAmountEggs or amountMilk < minAmountMilk:
    sleep(5)
    exit("You can't have no pancakes today.. :(")
# calculation
else:
    amountFlour = amountFlour / minAmountFlour 
    amountMilk = amountMilk / minAmountMilk
    amountEggs = amountEggs / minAmountEggs

minimum = int(min(amountEggs, amountFlour, amountMilk))

sleep(5)
# amount of pancakes and needed materials
print("You can make " + str(minimum*4) + " pancakes.")
sleep(2)
print("You need " + str(minimum*int(minAmountMilk)) + " milliliter milk.")
sleep(2)
print("You need " + str(minimum*int(minAmountFlour)) + " grams flour.")
sleep(2)
print("You need " + str(minimum*int(minAmountEggs)) + " eggs.")