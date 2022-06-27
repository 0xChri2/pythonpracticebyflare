import pyautogui as pt
import pydirectinput as pdi
from time import sleep

def move(key, keyduration, action='walking'):
    pdi.keyDown(key)
    if action == 'walking':
         print(action, "  with", keyduration, "seconds and key ", key)
    elif action == 'running':
        pdi.keyDown('shift')
        print(action, "  with", keyduration, "seconds and key ", key)
    sleep(keyduration)
    pdi.keyUp(key)
    pdi.keyUp('shift')
    print(action, " stopped")

def move_mouse(x, y):
    pt.moveTo(x, y)
    print("Mouse moved to", x, y)
    return 0

sleep(3)
move('w', 10, 'running')