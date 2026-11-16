# Week 1.7, Session 2: Task 1 - ValueError

# Run this program and observe what happens

user_profile = {"username": "alice99", "role": "admin"}

for key in user_profile: # seperted key and value to void errors
	print(f"{key} : ")
	
for value in user_profile:
	print(f"{value}")