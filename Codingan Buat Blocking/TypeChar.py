import PySimpleGUI as sg
import os.path

file_list_column = [
    sg.Text("Image Folder"),
    sg.Input(size=(25, 1), enable_events=True, key="-FOLDER-"),
    sg.FolderBrowse(),
    sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")
]

image_viewer_column = [
    [sg.Text("Choose an image from the list on the left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")]
]
layout = [
    [sg.Column(file_list_column), sg.Column(image_viewer_column)]
]
window = sg.Window("Image Viewer", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        if os.path.isdir(folder):
            file_list = os.listdir(folder)
            file_list = [f for f in file_list if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            window["-FILE LIST-"].update(file_list)

    if event == "-FILE LIST-":
        try:
            filename = values["-FILE LIST-"][0]
            filepath = os.path.join(values["-FOLDER-"], filename)
            window["-IMAGE-"].update(filename=filepath)
            window["-TOUT-"].update(filename)
        except IndexError:
            pass

window.close()
