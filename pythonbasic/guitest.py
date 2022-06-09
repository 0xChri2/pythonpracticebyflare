import PySimpleGUI as sg

# 2 - Layout definition
layout = [[sg.Text('My layout')],
          [sg.Input(key='-IN-')],
          [sg.Text('You entered:'), sg.Text(size=(20,1), key='-OUT-')],
          [sg.Button('OK'), sg.Button('Cancel')]]

# 3 - Create window
window = sg.Window('Update window with input value', layout)

# 4 - Event Loop
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Cancel'):
        break
    window['-OUT-'].update(values['-IN-'])
# 5 - Close window
window.close()

exit()