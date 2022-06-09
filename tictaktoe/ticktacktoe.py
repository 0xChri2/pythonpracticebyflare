import PySimpleGUI as sg

error = 0

layoutlogin =[[sg.Text('Tic Tac Toe')],
        [sg.Text('Player 1', size=(10, 1)), sg.InputText(key='-IN-', size=(10, 1))],
        [sg.Text('Player 2', size=(10, 1)), sg.InputText(key='-IN2-', size=(10, 1))],
        [sg.Button('Play')]]

layoutgame = layout =[[sg.Text('Tic Tac Toe')],
            [sg.Text('Player 1:', size=(10, 1)),sg.Text(key='-OUT-', size=(10, 1)),sg.Text('Player 2:', size=(10, 1)),sg.Text(key='-OUT2-', size=(10, 1))]]

layout = [[sg.Column(layoutlogin, key='-COL1-', visible=True), sg.Column(layoutgame, visible=False, key='-COL2-')]]

sg.theme('Dark Grey 13')
window = sg.Window('Tictaktoe', layout)

while True:
    event, values = window.read()
    print(event, values)
    print(values)
    if event == 'Play':
        window['-COL1-'].update(visible=False)
        window['-COL2-'].update(visible=True)
        window['-OUT-'].update(values['-IN-'])
        window['-OUT2-'].update(values['-IN2-'])
    else: 
        break
        window.close()
        exit()
