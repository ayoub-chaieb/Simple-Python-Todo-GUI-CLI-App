import PySimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.Input(tooltip="Source path")
choose_button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input(tooltip="Destination path")
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button]])

window.read()
print("window closed")
window.close()