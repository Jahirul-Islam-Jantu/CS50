# Class based programming is called OOP 
# class Point():
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2

# p = Point(10, 20)
# print(p.x)
# print(p.y)
# print(f"The value{p.x} and {p.y} is the points of a class, when we multiply {p.x * p.y} it will return ")

# This is the basic structure of a class in python. and we are calling the class with two parameters and multiply them.
# __init__ is called itself every times when value changes


#  Let's create a airline ticket booking system

#
# class Flight():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []
#
#     def add_passengers(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True
#
#     def open_seats(self):
#         return self.capacity - len(self.passengers)
#
#
# flight = Flight(3)
#
# peoples = ["Jahir", "Sahana", "Tawhid", "Samayrah", "Anamul", "Rana", "Keya"]
#
# for people in peoples:
#     if flight.add_passengers(people):
#         print(f"Added {people} in Passenger list for the flight")
#     else:
#         print(f"{people} not added because of no seats available")


class ClassRoom():
    def __init__(self, capacity):
        self.capacity = capacity
        self.students = []

    def add_student(self, name):
        if not self.open_capacity():
            return False
        self.students.append(name)
        return True

    def open_capacity(self):
        return self.capacity - len(self.students)


classroom = ClassRoom(3)

studentsList = ["Jahir","Jantu", "Keya", "Sahana"]

for student in studentsList:
    if classroom.add_student(student):
        print(f"Student added Successfully, Name: {student}")
    else:
        print(f"No seat for {student}")