# Worksheet 1.5: Person class

from datetime import date

class Person:
        """
    Define the person class
    """
    def __init__(self,name, birth):
            """
    Initailise paramters and check inputs
    """
        self.name = name
        self.birth = birth
        if not isinstance(name, (str)):
            raise ValueError("name field cannot be empty")
        if not isinstance(birth, (date)):
            raise TypeError("dob must be a date")
    

    def is_birthday(self):
            """
    Checks the birthday of the person by checking the month and day
    """
        if (self.birth).day == (date.today()).day and (self.birth).month == (date.today()).month:
            return True
        else:
            return False

    """
    A Person, with a name and a date of birth.
    """
    def initials(self): 
            """
    Return iniutials of the person
    """
        initals = ''
        name_list = self.name.split()
        for i in range(0,(len(name_list))):
            initals = initals + (name_list[i][0])
        return initals.upper()

        






    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
