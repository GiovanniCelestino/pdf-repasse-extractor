import pyautogui
import time
import keyboard
import re
import pyperclip



def buscarContrato():
    #APSDU: Sobe toda a tela
    time.sleep(3)
    pyautogui.click(x=1354, y=202)
    time.sleep(1)
    #APSDU: Acessa primeiro item da fila ZZR_CONT
    pyautogui.click(x=367, y=226)
    time.sleep(2) 

    #Copia número do contrato
    pyautogui.hotkey('ctrl', 'c')
    numContrato = pyperclip.paste().strip()  
    



    
