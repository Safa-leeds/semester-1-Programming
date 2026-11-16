import random
number = int(input('enter a number '))

openfile = open("random.txt", "w")
for i in range(number):
    numbers=random.randint(1,100)
    openfile.write(str(numbers) + '\n')





# Get user to input how many random numbers they want

# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line
