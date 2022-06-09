import PySimpleGUI as sg

error = 0
sg.theme('Dark Grey 13')
layout =[[sg.Text('Tic Tac Toe')],
        [sg.Text('Player 1', size=(10, 1)), sg.InputText('Player 1', size=(10, 1))],
        [sg.Text('Player 2', size=(10, 1)), sg.InputText('Player 2', size=(10, 1))],
        [sg.Button('Play')]]
    
window = sg.Window('Tictaktoe', layout)
event, values = window.read()

Player1 = values[0]
Player2 = values[1]
print(Player1)
print(Player2)

if Player1 == Player2:
    print("Player 1 and Player 2 are the same")
    error = 1
else:
    layout =[[sg.Text('Tic Tac Toe')],
    [sg.Test(Player1, size=(10, 1)), sg.Test(Player2, size=(10, 1))]]
    window.refresh()

window.close()
