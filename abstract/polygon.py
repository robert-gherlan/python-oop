from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def number_of_sides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def number_of_sides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def number_of_sides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def number_of_sides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def number_of_sides(self):
        print("I have 4 sides")
