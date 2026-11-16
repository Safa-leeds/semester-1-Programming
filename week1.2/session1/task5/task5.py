# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Bristol"] = "Avon"
rivers['kizilirmak'] = 'kizilirmak'

# Display all the keys
display_keys = list(rivers.keys())
print(display_keys)

# Display all the values
display_values = list(rivers.values())
print(display_values)

# Display all the key:value pairs, as tuples
display_items = list(rivers.items())
print(display_items)

# Delete an entry from the rivers database
del rivers["kizilirmak"]
