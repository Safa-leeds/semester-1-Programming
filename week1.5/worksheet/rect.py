# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        if not isinstance(width, (int)):
            raise TypeError("width must be an integer")
        if not isinstance(height, (int)):
            raise TypeError("height must be an integer")
        if isinstance(height<=0, (bool)):
            raise ValueError("cannot be less tham zero")
        if isinstance(width<=0, (bool)):
            raise ValueError("cannot be less tham zero")
    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width) * 2 + (self.height) * 2





        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)


    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
