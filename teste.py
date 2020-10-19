import pyautogui
import time

x = 0

i = input('coloque na posicao 1 e aperte enter');

currentUseSpX, currentUseSpY = pyautogui.position();

i = input('coloque na posicao 2 e aperte enter');

currentUseFoX, currentUseFoY = pyautogui.position();

i = input('coloque na posicao 3 e aperte enter');

currentUseFo2X, currentUseFo2Y = pyautogui.position();

i = input('coloque na posicao 4 e aperte enter');

currentUseFo4X, currentUseFo4Y = pyautogui.position();

i = input('coloque na posicao 5 e aperte enter');

currentUseFo5X, currentUseFo5Y = pyautogui.position();

i = input('coloque na posicao 6 e aperte enter');

currentUseFo6X, currentUseFo6Y = pyautogui.position();

while(x<10000):  
    

    pyautogui.click(currentUseFoX, currentUseFoY);
    #print('posicao 1: ', currentUseFoX, currentUseFoY);

    time.sleep(25);
    
    #print('posicao 2: ', currentUseSpX, currentUseSpY);
    pyautogui.click(currentUseSpX, currentUseSpY);

    time.sleep(25);

    #print('posicao 3: ', currentUseSpX, currentUseSpY);
    pyautogui.click(currentUseFo2X, currentUseFo2Y);

    time.sleep(8);

    pyautogui.click(currentUseFo4X, currentUseFo4Y);
    #print('posicao 4: ', currentUseFoX, currentUseFoY);

    time.sleep(4);
    
    #print('posicao 5: ', currentUseSpX, currentUseSpY);
    pyautogui.click(currentUseFo5X, currentUseFo5Y);

    time.sleep(4);

    #print('posicao 6: ', currentUseSpX, currentUseSpY);
    pyautogui.click(currentUseFo6X, currentUseFo6Y);

    time.sleep(2);

    x+=1

    print('mais um ciclo:', x);

    
