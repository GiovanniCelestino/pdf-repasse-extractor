import pyautogui
import time
import keyboard
import re
import pyperclip
#from main import extrai_valor_nota, extrai_texto_boleto
data_vencimento = '25/10/2025'

def buscarContrato():
    #APSDU: Acessa primeiro item da fila ZZR_CONT
    #pyautogui.click(x=367, y=226)
    time.sleep(1) 

    #Copia número do contrato
    pyautogui.hotkey('ctrl', 'c')
    numContrato = pyperclip.paste().strip()  
    return numContrato
    
#Colar informação no apsdu
def colar_info():
   pyautogui.press('enter')
   time.sleep(1)
   pyautogui.hotkey('ctrl', 'v')
   time.sleep(1)


#Pular campo para direita:
def contador_right(cont):
   contador = cont
   while contador != 0:
      time.sleep(1)
      pyautogui.press('right')
      contador -= 1


#Pular campo para a esquerda:
def contador_left(cont):
   contador = cont
   while contador != 0:
      time.sleep(0.5)
      pyautogui.press('left')
      contador -= 1



def preencheDados_nota(valor, numero_nota, data_emissao, cnpj_tomador, cnpj_prestador):
  
  #NUMERO NOTA
  pyperclip.copy(f'0{numero_nota}')
  contador_right(8)
  colar_info()

  #VALOR NOTA
  pyperclip.copy(valor)
  contador_right(1)
  colar_info()

  #DATA EMISSAO
  pyperclip.copy(data_emissao)
  contador_right(1)
  colar_info()

  #DATA VENCIMENTO X
  pyperclip.copy(data_vencimento)
  contador_right(1)
  colar_info()
  time.sleep(1)

  
  #DATA VENCIMENTO Y
  pyperclip.copy(data_vencimento)
  contador_right(1)
  colar_info()
  time.sleep(1)

  

def preencheDados_boleto(resultado_boleto_digt, resultado_nosso_num):
   #NUMERO DIGITAVEL BOLETO
   pyperclip.copy(resultado_boleto_digt)
   contador_right(4)
   colar_info()
   time.sleep(1)

   #NOSSO NUMERO BOLETO
   pyperclip.copy(resultado_nosso_num)
   contador_right(1)
   colar_info()
   time.sleep(1)
   pyautogui.press('enter')
   time.sleep(1)

   


def nomeArq(receber_nome):
   #NOME ARQUIVO
   pyperclip.copy(receber_nome)
   contador_right(6)
   colar_info()
   time.sleep(1)
   contador_right(1)

   colar_info()
   time.sleep(1)
   contador_right(1)

   colar_info()
   time.sleep(1)
   contador_right(1)

def CNPJ(cnpj_tomador, cnpj_prestador):
    #CNPJ TOMADOR:
    time.sleep(1)
    pyperclip.copy(cnpj_tomador)
    colar_info()
    time.sleep(1)
    contador_right(1)

    #CNPJ PRESTADOR:
    time.sleep(1)
    pyperclip.copy(cnpj_prestador)
    colar_info()
    time.sleep(1)
    contador_right(2)    

    #ATUALIZAR STATUS
    pyperclip.copy('P')
    time.sleep(1)
    colar_info()
    time.sleep(1)
    
    #RETORNA COMEÇO
    contador_left(30)
    pyautogui.press('down')
    contador_right(1)



   
    



    
