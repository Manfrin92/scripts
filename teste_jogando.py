import pyautogui
from pynput.keyboard import Key, Listener
import keyboard
import time

i = input('coloque na posicao 1 e aperte enter');
currentX1, currentY1 = pyautogui.position();

i = input('coloque na posicao 2 e aperte enter');
currentX2, currentY2 = pyautogui.position();

i = input('coloque na posicao 3 e aperte enter');
currentX3, currentY3 = pyautogui.position();

i = input('coloque na posicao 4 e aperte enter');
currentX4, currentY4 = pyautogui.position();

i = input('coloque na posicao 5 e aperte enter');
currentX5, currentY5 = pyautogui.position();

i = input('coloque na posicao 6 e aperte enter');
currentX6, currentY6 = pyautogui.position();

i = input('coloque na posicao 7 e aperte enter');
currentX7, currentY7 = pyautogui.position();

i = input('coloque na posicao 8 e aperte enter');
currentX8, currentY8 = pyautogui.position();

i = input('coloque na posicao 9 e aperte enter');
currentX9, currentY9 = pyautogui.position();

i = input('coloque na posicao da knife');
currentXKnife, currentYKnife = pyautogui.position();

# Lootiando
def looting():
    pyautogui.click(currentX1, currentY1, button='right');
    pyautogui.click(currentX2, currentY2, button='right');
    pyautogui.click(currentX3, currentY3, button='right');
    pyautogui.click(currentX4, currentY4, button='right');
    pyautogui.click(currentX5, currentY5, button='right');
    pyautogui.click(currentX6, currentY6, button='right');
    pyautogui.click(currentX7, currentY7, button='right');
    pyautogui.click(currentX8, currentY8, button='right');
    pyautogui.click(currentX9, currentY9, button='right');
# Pegando couro
def skinning():
    pyautogui.click(currentXKnife, currentYKnife);
    #time.sleep(0.5);
    pyautogui.click(currentX6, currentY6);    
##    pyautogui.click(currentXKnife, currentYKnife);
##    time.sleep(0.5);
##    pyautogui.click(currentX2, currentY2);    
##    pyautogui.click(currentXKnife, currentYKnife);
##    time.sleep(0.5);
##    pyautogui.click(currentX3, currentY3);
##    pyautogui.click(currentXKnife, currentYKnife);
##    time.sleep(0.5);
##    pyautogui.click(currentX4, currentY4);
##    pyautogui.click(currentXKnife, currentYKnife);
##    time.sleep(0.5);
##    pyautogui.click(currentX5, currentY5);
##    pyautogui.click(currentXKnife, currentYKnife);
##    time.sleep(0.5);
##    pyautogui.click(currentX6, currentY6);
##    pyautogui.click(currentXKnife, currentYKnife);
##    time.sleep(0.5);
##    pyautogui.click(currentX7, currentY7);
##    pyautogui.click(currentXKnife, currentYKnife);
##    time.sleep(0.5);
##    pyautogui.click(currentX8, currentY8);
##    pyautogui.click(currentXKnife, currentYKnife);
##    time.sleep(0.5);
##    pyautogui.click(currentX9, currentY9);

def onPress(key):
    try:
        print('chave : ', key);
    except AttributeError:
        print('special key pressed', key);
def on_release(key):
    if key == Key.esc:
        print('desligando')
        return False
    else:
        if key == Key.backspace:      
            skinning();
        if key == Key.enter:   
            looting();

with Listener(
        onPress=onPress,
        on_release=on_release) as listener:    listener.join()
