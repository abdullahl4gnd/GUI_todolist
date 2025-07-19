import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass  # Create the file if it doesn't exist

sg.theme("DarkBrown4")  # Set the theme for the GUI

clock = sg.Text("", key="clock")
label = sg.Text("Welcome to your to-do list!")
input_box = sg.InputText(tooltip="Enter add, show, edit, complete or exit",key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size =[ 45, 10 ])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")



window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label], [input_box ,add_button],
                           [list_box,edit_button , complete_button ],
                           [exit_button]],
                   font=("Helvetica", 20))

while True :
    event , values  = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo= values["todo"]+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                selected_todo = values["todos"][0]
                new_text = values["todo"].strip() + "\n"

                todos = functions.get_todos()
                index = todos.index(selected_todo)
                todos[index] = new_text
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please: 1) Select an item 2) Edit the text 3) Click Edit" , font=("Helvetica", 20))

        case "Complete":
            try :
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please: 1) Select an item 2) Click Complete", font=("Helvetica", 20))

        case "todos":
            window["todo"].update(value=values["todos"][0].strip())
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break



window.close()
