
# the PANCAKE counter, to see how much pancakes you can make
import time
import sys

# this measeruments are for a serving of four pancakes
minAmountMilk = 350 #milliliter
minAmountFlour = 200 #grams
minAmountEggs = 2

# loading...
user = input("Hello?")
time.sleep(2)
print("Hello " + user)
time.sleep(2)
print("Program loading...")
time.sleep(5)
print("Program done loading")
time.sleep(2)

# amount of milk (input from user)
amountMilk = int(input("How much milk do you have (in milliliters)?"))
print("Calculating...")
time.sleep(2)

# amount of flour (input from user)
amountFlour = int(input("How much flour do you have (in grams)?"))
print("Calculating...")
time.sleep(2)

# amount of eggs (input from user)
amountEggs = int(input("How many eggs do you have?"))
print("Calculating...")
time.sleep(2)

# checks if there is even enough to make one batch of pancakes (4)
if amountFlour < minAmountFlour or amountEggs < minAmountEggs or amountMilk < minAmountMilk:
    time.sleep(5)
    sys.exit("You can't have no pancakes today.. :(")
# calculation
else:
    amountFlour /= minAmountFlour 
    amountMilk /= minAmountMilk
    amountEggs /= minAmountEggs

minimum = int(min(amountEggs, amountFlour, amountMilk))

time.sleep(5)
# amount of pancakes and needed materials
print("You can make " + str(minimum*4) + " pancakes.")
time.sleep(2)
print("You need " + str(minimum*int(minAmountMilk)) + " milliliter milk.")
time.sleep(2)
print("You need " + str(minimum*int(minAmountFlour)) + " grams flour.")
time.sleep(2)
print("You need " + str(minimum*int(minAmountEggs)) + " eggs.")
