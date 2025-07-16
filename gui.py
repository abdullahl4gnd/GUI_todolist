import functions

import FreeSimpleGUI as sg

label = sg.Text("Welcome to your to-do list!")
input_box = sg.InputText(tooltip="Enter add, show, edit, complete or exit",key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box ,add_button]],
                   font=("Helvetica", 20))

while True :
    event , values  = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo= values["todo"].strip()
            todos.append(new_todo + "\n")
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()
