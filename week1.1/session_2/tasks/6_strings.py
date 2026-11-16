# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") # print the original string
print(f"Modified String 1: {user_string.lower()}")# prints string alll lowercase
print(f"Modified String 2: {user_string.upper()}")#prints all uppercase
print(f"Modified String 3: {user_string.strip()}")# removes whitespaces
print(f"Modified String 4: {user_string.replace('a', '@')}")# replaces all a with @
print(f"Modified String 5: {user_string.capitalize()}")#capitalises first letter
print(f"Modified String 6: {user_string[::-1]}") # reverses the string
print(f"Modified String 7: {user_string.title()}") #capitalises the first letter of each word
print(f"Modified String 8: {len(user_string)}") # prints the length of the string
print(f"Modified String 9: {user_string.find('a')}") #finds where a is in the string
print(f"Modified String 10: {user_string.count('a')}")#counts number of a's
print(f"Modified String 11: {user_string.startswith('Hello')}") #check to start with hello
print(f"Modified String 12: {user_string.endswith('!')}")#check to see if it ends with !
print(f"Modified String 13: {user_string.isalnum()}")#checking if the string is alphanumeric
print(f"Modified String 14: {user_string.isalpha()}")# checking if the string is alphabetic
print(f"Modified String 15: {user_string.isdigit()}")#checks if number is a digit



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!