# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.

# Open a file called 'user_info.txt' for reading
open_file = open('user_info.txt', 'w')
# Write each piece of information to the file, each on a new line.
write_name = input("What is your name? ")
write_age = input("What is your age? ")
write_colour = input("What is your favourite colour? ")
open_file.write(write_name + "\n")
open_file.write(write_age + "\n")
open_file.write(write_colour + "\n")
# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
