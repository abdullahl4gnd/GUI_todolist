import functions

import FreeSimpleGUI as sg

label = sg.Text("Welcome to your to-do list!")
input_box = sg.InputText(tooltip="Enter add, show, edit, complete or exit")
add_button = sg.Button("Add")

window = sg.Window("To-Do List", layout=[[label, input_box ,add_button]])
window.read()
window.close()
