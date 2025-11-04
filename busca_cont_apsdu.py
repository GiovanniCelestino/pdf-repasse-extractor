import pyautogui
import time
import keyboard
import re
import pyperclip
#from main import extrai_valor_nota, extrai_texto_boleto
data_vencimento = '30/10/2025'





def verificaValorCampo():
   pyperclip.copy('')
   pyautogui.hotkey('ctrl', 'c')
   valor_campo = pyperclip.paste().strip()
   return valor_campo


def arquivoRecebido():
   cont = 0
   while cont != 3:
        
        valor_do_campo = verificaValorCampo()
        if valor_do_campo != 'S':
            pyperclip.copy('S')
            colar_info()
            time.sleep(1)
        pyautogui.press('right')
        time.sleep(1)
        
        cont +=1 


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
  contador_right(3)
  arquivoRecebido()
  #NUMERO NOTA
  contador_right(2)
  valor_do_campo = verificaValorCampo()
  if valor_do_campo == '':
        if len(numero_nota) == 6:
          pyperclip.copy(f'000{numero_nota}')
        else:
          pyperclip.copy(f'0{numero_nota}')
        colar_info()

  #VALOR NOTA
  contador_right(1)
  valor_do_campo = verificaValorCampo()
  if valor_do_campo == '0.00':
      pyperclip.copy(valor)
      colar_info()

  #DATA EMISSAO
  contador_right(1)
  valor_do_campo = verificaValorCampo()
  if valor_do_campo == '/ /':
      pyperclip.copy(data_emissao)
      colar_info()

  #DATA VENCIMENTO X
  contador_right(1)
  valor_do_campo = verificaValorCampo()
  if valor_do_campo == '/ /':
      pyperclip.copy(data_vencimento)
      colar_info()
      time.sleep(1)

  
  #DATA VENCIMENTO Y
  contador_right(1)
  valor_do_campo = verificaValorCampo()
  if valor_do_campo == '/ /':
      pyperclip.copy(data_vencimento)
      colar_info()
      time.sleep(1)

  

def preencheDados_boleto(resultado_boleto_digt, resultado_nosso_num):

   #NUMERO DIGITAVEL BOLETO
   contador_right(4)
   valor_do_campo = verificaValorCampo()
   if valor_do_campo == '':
      pyperclip.copy(resultado_boleto_digt)
      colar_info()
      time.sleep(1)

   #NOSSO NUMERO BOLETO
   contador_right(1)
   valor_do_campo = verificaValorCampo()
   if valor_do_campo == '':
      pyperclip.copy(resultado_nosso_num)
      colar_info()
      time.sleep(1)
      pyautogui.press('enter')



def nomeArq(receber_nome):
   #NOME ARQUIVO
   
   contador_right(6)
   valor_do_campo = verificaValorCampo()
   if valor_do_campo == '':
      pyperclip.copy(receber_nome)
      colar_info()
      time.sleep(1)
   contador_right(1)

   valor_do_campo = verificaValorCampo()
   if valor_do_campo == '':
      pyperclip.copy(receber_nome)
      colar_info()
      time.sleep(1)
   contador_right(1)

   valor_do_campo = verificaValorCampo()
   if valor_do_campo == '':
      pyperclip.copy(receber_nome)
      colar_info()
      time.sleep(1)
   contador_right(1)

def CNPJ(cnpj_tomador, cnpj_prestador):
    #CNPJ TOMADOR:
    time.sleep(1)
    valor_do_campo = verificaValorCampo()
    if valor_do_campo == '':
      pyperclip.copy(cnpj_tomador)
      colar_info()
      time.sleep(1)
    contador_right(1)

    #CNPJ PRESTADOR:
    time.sleep(1)
    valor_do_campo = verificaValorCampo()
    if valor_do_campo == '':
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



   
    



    
