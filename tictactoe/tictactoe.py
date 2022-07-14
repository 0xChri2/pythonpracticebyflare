import PySimpleGUI as sg
import numpy as np
import sys

    

def change_x_and_o(event, check):
        if check == 0:
            window[event].update('X')
            check = 1
        else:
            window[event].update('O')
            check = 2
        return check

def reset_board():
    for i in range(1,9):
        window[i].update('0')

layoutlogin =[[sg.Text('Tic Tac Toe')],
        [sg.Text('Player 1', size=(10, 1)), sg.InputText(key='P1', size=(10, 1))],
        [sg.Text('Player 2', size=(10, 1)), sg.InputText(key='P2', size=(10, 1))],
        [sg.Button('Play')]]

layoutgame = layout =[[sg.Text('Tic Tac Toe')],
            [sg.Text('Player 1:', size=(10, 1)),sg.Text(key='-OUT-', size=(10, 1)),sg.Text('Player 2:', size=(10, 1)),sg.Text(key='-OUT2-', size=(10, 1))],
            [sg.Button(key='1', size=(10,5)), sg.Button(key='2', size=(10, 5)), sg.Button(key='3', size=(10, 5))], 
            [sg.Button(key='4', size=(10,5)), sg.Button(key='5', size=(10,5)), sg.Button(key='6', size=(10,5))],
            [sg.Button(key='7', size=(10,5)), sg.Button(key='8', size=(10,5)), sg.Button(key='9', size=(10,5))]]

layout = [[sg.Column(layoutlogin, key='-COL1-', visible=True), sg.Column(layoutgame, visible=False, key='-COL2-')]]

sg.theme('Dark Grey 13')
window = sg.Window('Tictaktoe', layout)
check = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
windowlvl = 0
exit = False
while exit == False:
    
    

    event, values = window.read()
    print(event, values)
    print(values)
    
    if event == 'Play':
        window['-COL1-'].update(visible=False)
        window['-COL2-'].update(visible=True)
        window['-OUT-'].update(values['P1'])
        window['-OUT2-'].update(values['P2'])
        windowlvl = 1
    elif windowlvl == 1:
            if event == '1':
                check[1] = change_x_and_o('1', check[1])
            elif  event == '2':
                check[2] = change_x_and_o('2', check[2])
            elif  event == '3':
                check[3] = change_x_and_o('3', check[3])
            elif  event == '2':
                check[2] = change_x_and_o('2', check[2])
            elif  event == '4':
                check[4] = change_x_and_o('4', check[4])
            elif  event == '5':
                check[5] = change_x_and_o('5', check[5])
            elif  event == '6':
                check[6] = change_x_and_o('6', check[6])
            elif  event == '7':
                check[7] = change_x_and_o('7', check[7])
            elif  event == '8':
                check[8] = change_x_and_o('8', check[8])
            elif  event == '9':
                check[9] = change_x_and_o('9', check[9])
            if check[1] == 1 and check[2] == 1 and check[3] == 1:
                sg.popup(' wins')
                windowlvl = 0
                window['-COL1-'].update(visible=True)
                window['-COL2-'].update(visible=False)
                check = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                reset_board()
            #else:
                #sys.exit()

    else:
        sys.exit()


