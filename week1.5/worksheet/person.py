# Worksheet 1.5: Person class

from datetime import date

class Person:
    def __init__(self,name, dob):
        self.name = name
        self.dob = dob
        if not isinstance(name, (str)):
            raise ValueError("name field cannot be empty")
        if not isinstance(dob, (date)):
            raise TypeError("dob must be a date")
    

    def is_birthday(self):
        if (self.dob).day == (date.today()).day and (self.dob).month == (date.today()).month:
            return True
        else:
            return False

    """
    A Person, with a name and a date of birth.
    """
    def initials(self):
        initals = ''
        name_list = self.name.split()
        for i in range(0,(len(name_list))):
            initals = initals + (name_list[i][0])
        return initals
        print(initals)
        
person = Person("longest name ever", date(2000, 10, 26))
print(person.initials())
print(person.is_birthday())





    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
