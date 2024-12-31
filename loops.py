# Loops are used to iterate over a sequence (list, tuple, string) or other iterable objects.

# numbers = [1, 2, 3, 4, 5]

# for i in numbers:
#     print(i)

# for i in range(100):
#     print(i)

# name = "Jahir"
# for i in name:
#     print(i)

names = ["Jahir", "Raihan", "Rahat", "Rakib", "Rahim"]
for name in names: 
    print(name)

cars = ["Toyota", "Nissan", "BMW", "Audi", "Mercedes", "Ferrari", "Lamborghini", "Ford", "Chevrolet", "Jeep"]

for car in cars:
    print(car)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = len(numbers)
for number in numbers:
    print(f" {number} + {sum} =  {number+sum}") 