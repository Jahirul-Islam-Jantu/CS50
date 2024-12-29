from functions import square
# This is how we import a function from another file in python.
#  We can import a function from another file by using the "from" keyword and the file name and function name.

for i in range(100):
    print(f"The square of {i} is {square(i)}")

# This loop has no function to print the square of the numbers from 1 to 99. So we are importing the function from the functions.py file and calling the function in the loop to print the square of the numbers from 1 to 99.
