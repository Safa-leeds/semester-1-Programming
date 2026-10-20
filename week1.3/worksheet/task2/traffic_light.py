"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }
state_order = ["red", "red_amber", "green", "amber"]
state_time = [4, 3, 5, 3]
systime = 0
maxtime = int(input())  # read an integer number of steps (>0)
state = "red"
counter = 1
place = 0
print(f"Time {systime:03} State {state}")
while systime < maxtime:
    systime = systime + 1
    counter = counter + 1
    print(f"Time {systime:03} State {state}")

    if counter == states[state]:
        place = (place+1) % len(state_order)
        state = state_order[place] 
        counter = 0

            






