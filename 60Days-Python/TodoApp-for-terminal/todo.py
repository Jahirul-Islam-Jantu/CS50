
while True:
    user_input = input("Please Type add , show, edit, complete or exit: ")
    user_input = user_input.strip()
    match user_input:
        case "add":
            todo = input("Add Item: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "show":
            for index, item in enumerate(todos):
                item = item.title()
                print(f"{index+1}: {item}")
        case "edit":
            number = int(input("Enter a Number for Edit Todo: "))
            number = number - 1
            new_todo = input("Enter new Todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Enter a Number for complete Todo: "))
            todos.pop(number - 1)
        case "exit":
            break
        case _:
            print("Hey, You entered Wrong keyword")



print(f"Bye Bye Dear. Your Todos are Here! {todos}")