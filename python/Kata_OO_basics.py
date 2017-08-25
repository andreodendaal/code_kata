"""
1. Create Rectangle and Square classes with a method called calculate_perimeter that calculates the perimeter of 
the shapes they represent. Create Rectangle and Square objects and call the method on both of them.
"""

class Shape():
    def what_am_i(self):
        print("I am a shape.", self)


class Rectangle(Shape):
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def calculate_perimeter(self):
        self.perimeter = (self.side_1 + self.side_2) * 2
        return self.perimeter

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        self.perimeter = self.side * 4
        return self.perimeter

    def change_size(self, value):
        self.side += value

a_shape = Shape()
a_shape.what_am_i()

rectangle = Rectangle(5, 4)

print(rectangle.calculate_perimeter())
square = Square(10)
print(square.calculate_perimeter())
square.change_size(-2)
print(square.calculate_perimeter())
square.what_am_i()
rectangle.what_am_i()

"""
2. Define a method in your Square class called change_size that allows you to pass in a number that increases 
or decreases (if the number is negative) each side of a Square object by that number
"""

"""
3. Create a class called Shape. Define a method in it called what_am_i that prints "I am a shape" when called. 
Change your Square and Rectangle classes from the previous challenges to inherit from Shape, 
create Square and Rectangle objects, and call the new method on both of them. 

4. Create a class called Horse and a class called Rider. Use composition to model a horse that has a rider. 

Solutions: http://tinyurl.com/hz9qdh3.

"""