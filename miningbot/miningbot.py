from turtle import pos, position
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

def move_mouse(x, y):
    pt.dragRel(x, y)
    print("Mouse moved to", x, y)
    
def detectandmove(image):
    location = pt.locateCenterOnScreen(image, confidence=.7)
    if location:
        pt.click(location[0],location[1])
        print ("Clicked on", image)
    else:
        print ("Could not find", image)

def detect_image(image):
    location = pt.locateCenterOnScreen(image, confidence=.6)
    return location

def mining(duration):
    # leftclick = k
    # rightklick = i
    pt.press('3')
    pt.keyDown('k')
    sleep(duration)
    pt.keyUp('k')

sleep(3)
detectandmove('backtogame.PNG')
while True:
    move('w', 0.5, 'walking')
    mining(1)
    


