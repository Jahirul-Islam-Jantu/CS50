number = int(input("Number: "))
if number > 0:
    print(f"{number} is Positive")
elif number < 0:
    print(f"{number} is Negative")
else:
    print("The Number is zero")

    #  This is the basic structure of a if, elseif, else condition to check. but in the input section we are taking the value from the user is like String value. str value is not comparable with numbers. that's why we have to call a default function called int and wrapped the input.