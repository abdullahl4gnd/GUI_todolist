import functions
import time

now =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(now)

print("Welcome to your to-do list!")

while True:
    user = input("Enter add, show, edit, complete or exit: ")
    user = user.strip()

    if user.startswith("add"):
        todo = user[4:]
        todos = functions.get_todos()
        todos.append(todo + "\n")
        functions.write_todos(todos)
        print(todo.strip() + " has been added to the to-do list")

    elif user.startswith("show"):
        print("Your list:")
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip()
            print(f"{index + 1} - {item}")

    elif user.startswith("edit"):
        try:
            number = int(user[5:])
            index = number - 1
            todos = functions.get_todos()
            old = todos[index].strip()
            new_todo = input("The new name of todo: ")
            todos[index] = new_todo.strip().title() + "\n"
            functions.write_todos(todos)
            print(f"Old todo '{old}' edited to '{new_todo}'")
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("No such item in the list.")
            continue

    elif user.startswith("complete"):
        try:
            number = int(user[9:])
            index = number - 1
            todos = functions.get_todos()
            removed = todos.pop(index).strip()
            functions.write_todos(todos)
            print(f"{removed} todo was removed from the list")
        except IndexError:
            print("There is no item with that number")
            continue
        except ValueError:
            print("Your command is not valid. Enter 'complete' followed by a number.")
            continue

    elif user.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("Bye")
