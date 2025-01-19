

todos = []
while True:
    user_input = input("Please Type add , show or exit: ")
    match user_input:
        case "add":
            todo = input("Add Item: ")
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            break

print(f"Bye Bye Dear. Your Todos are Here! {todos}")