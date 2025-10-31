import pyautogui
import time
import keyboard
import fitz  # PyMuPDF
import re
import keyboard





contador = 0


while True:
    #APSDU: Sobe toda a tela
    time.sleep(3)
    pyautogui.moveTo(1910, 274, duration=1)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    #APSDU: Acessa primeiro item da fila ZZR_CONT
    #Vai para o próximo item
    pyautogui.moveTo(412, 300, duration=1)
    pyautogui.click()
    time.sleep(2)
    
    
    contador += 1
    def contador_contrato():
        limite = 0
        while contador > limite:
            pyautogui.press('down')
            time.sleep(0.5)
            limite += 1 

    contador_contrato()
    
        
    pyautogui.hotkey('ctrl', 'c')
    confere_ultimo_contrato = pyperclip.paste()
    if confere_ultimo_contrato == '0JJUB':
        print("Programa Encerrado")
        break

    time.sleep(3)
    pyautogui.click(x=771, y=1052)
    time.sleep(3)
    pyautogui.click(x=1479, y=70)
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    pyperclip.copy("")
    contrato_existente_compara = pyperclip.paste()
    pyautogui.click(x=387, y=201)
    time.sleep(3)
    pyautogui.press('f2')
    pyautogui.hotkey('ctrl', 'c')
    conteudo_contrato = pyperclip.paste()
    if contrato_existente_compara == conteudo_contrato:
        pyautogui.click(x=1776, y=10)
        continue


    time.sleep(0.5)
    nome_arquivo_pdf = pyperclip.paste()
    print(nome_arquivo_pdf)
    pyautogui.press('enter')

    extrai_valor(nome_arquivo_pdf)
    valor_pdf = extrai_valor(nome_arquivo_pdf)
    pyperclip.copy(valor_pdf)


    pyautogui.click(x=1776, y=10)
    time.sleep(3)
    pyautogui.click(x=1910, y=274)
    time.sleep(3)
    pyautogui.click(x=412, y=300)


    
    
    contador_contrato() 

    for _ in range(9):
        pyautogui.press('right')
        time.sleep(0.4)
        
    
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.press('enter')

