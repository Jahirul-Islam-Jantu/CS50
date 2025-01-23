

todos = []
while True:
    user_input = input("Please Type add , show, edit or exit: ")
    user_input = user_input.strip()
    match user_input:
        case "add":
            todo = input("Add Item: ")
            todos.append(todo)
        case "show":
            for item in todos:
                item = item.title()
                print(item)
        case "edit":
            number = int(input("Enter a Number for Edit Todo: "))
            number = number - 1
            new_todo = input("Enter new Todo: ")
            todos[number] = new_todo
        case "exit":
            break
        case _:
            print("Hey, You entered Wrong keyword")



print(f"Bye Bye Dear. Your Todos are Here! {todos}")