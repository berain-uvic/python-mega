while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if(user_action == 'add'):
        todo = input("Enter a todo: ") + "\n"

        with open('app1/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('app1/todos.txt', 'w') as file:
            file.writelines(todos)

    elif(user_action == 'show'):
        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}"
            print(row)

    elif(user_action == 'edit'):
        number = int(input("Number of the todo to edit: "))
        number = number - 1
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo

    elif(user_action == 'complete'):
        number = int(input("Number of the todo to complete: "))
        todos.pop(number - 1)
        
    elif(user_action == 'exit'):
        break
