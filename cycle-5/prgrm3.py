class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def __lt__(self, other):
        self_area = self.__length * self.__breadth
        other_area = other.__length * other.__breadth
        if self_area < other_area:
            print("rect 1 is lesser")
        else:
            print("rect 2  is lesser")


Ob1 = Rectangle(10, 20)
Ob2 = Rectangle(20, 30)
Ob3 = Ob1 < Ob2
print(Ob3)