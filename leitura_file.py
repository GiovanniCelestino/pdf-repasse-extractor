#BIBLIOTECAS
import fitz  # PyMuPDF
import re
import pytesseract 
from PIL import Image
import io
import os

#ARQUIVOS
from boleto_para_imagem import transform_img
from teste_leitura_imagem import read_img






#EXTRAI VALORES DA NOTA FISCAL
def extrai_valor_nota(nome_arquivo_pdf):  #CORRIGIR CAMINHO:
    #caminho_pdf = rf"C:\Users\Giovanni\Desktop\HAPVIDA\NOTA FISCAL\{nome_arquivo_pdf}.pdf"

    #doc = fitz.open(caminho_pdf)
    doc_nota_fiscal = fitz.open(nome_arquivo_pdf)
    

    #Lista do numero da nota
    list_num_nota = []

    
    for pagina in doc_nota_fiscal:
        texto = pagina.get_text()
        
        
        linhas = texto.split('\n')

        for i, linha in enumerate(linhas):
            #EXTRAIR VALOR:
            if "Desconto Condicionado" in linha:
               
                if i + 1 < len(linhas):
                    valor_bruto = linhas[i + 1].strip()

                    # Usa regex para garantir que é um número
                    match = re.search(r'\d{1,3}(?:[.\,]\d{3})*[.,]\d{2}', valor_bruto)
                    if match:
                        valor = match.group()
            
                    else:
                        print("Valor não encontrado após 'Desconto Condicionado'")
                else:
                    print("Linha seguinte não existe")
            
            #EXTRAIR NUMERO DA NOTA:
            
            if "NFS-e" in linha:
                
                if i + 1 < len(linhas):
                    
                    num_nota = linhas[i + 1].strip()
                    list_num_nota.append(num_nota)

            #EXTRAIR DATA EMISSÃO:
            if "Local da Prestação" in linha:
                
                if i + 1 < len(linhas):

                    data_hr_emis = linhas[i + 1].strip()
                    data_emis = data_hr_emis[:10]


            #CNPJ TOMADOR DE SERVIÇO
            if "(-) Retenções Federais" in linha:
                
                if i + 2 < len(linhas):

                    cnpj_tomador = linhas[i + 2].strip()
                    # Extrai todos os números (incluindo decimais)
                    numeros = re.findall(r'\d+', cnpj_tomador)

                    # Junta todos os números em uma única string
                    result_cnpj_tomador = ''.join(numeros)
                    


            #CNPJ PRESTADOR DE SERVIÇO
            if "Insc Municipal" in linha:
                
                if i + 1 < len(linhas):

                    cnpj_prestador = linhas[i + 1].strip()
                    # Extrai todos os números (incluindo decimais)
                    numeros = re.findall(r'\d+', cnpj_prestador)

                    # Junta todos os números em uma única string
                    result_cnpj_prestador = ''.join(numeros)
                    
                    
                        

    
        print(f'DADOS NOTA FISCAL:\nValor:R${valor}\nNúmero Nota:{list_num_nota[1]}\nData Emissão:{data_emis}\n'\
              f'CNPJ Tomador:{result_cnpj_tomador}\nCNPJ Prestador:{result_cnpj_prestador}\n')
        #return valor, list_num_nota[1], data_emis, result_cnpj_tomador, result_cnpj_prestador         

    doc_nota_fiscal.close()


#EXTRAI VALORES DO BOLETO:
def extrai_texto_boleto(nome_arquivo_pdf):
    nome_pdf = nome_arquivo_pdf

    #transforma pdf para imagem
    transform_img(nome_pdf)

    #realiza leitura da imagem
    texto_gerado = read_img('boleto_img.jpg')

    linhas = texto_gerado.split('\n')

    for i, linha in enumerate(linhas):
    # Verifica se a linha contém uma das expressões
        #EXTRAI LINHA DIGITAVEL BOLETO
        if ": HAPVIDA ASSISTENCIA MEDICA LTDA" in linha or ": CENTRO CLINICO" in linha:
            if i + 2 < len(linhas):
                linha_boleto_digitavel = linhas[i + 2].strip()

                # Extrai todos os números (incluindo decimais)
                numeros = re.findall(r'\d+', linha_boleto_digitavel)

                # Junta todos os números em uma única string
                resultado_boleto_digt = ''.join(numeros)

        #EXTRAI 'NOSSO NUMERO' BOLETO
        if "Nosso Número" in linha:
            verifica_valor = linhas[i + 2].strip()
            if i + 1 < len(linhas) and verifica_valor == 'Numero do Documento':
                nosso_numero = linhas[i + 1].strip()

                # Extrai todos os números (incluindo decimais)
                numeros = re.findall(r'\d+', nosso_numero)

                # Junta todos os números em uma única string
                resultado_nosso_num = ''.join(numeros)



    print(f'DADOS BOLETO:\nLinha Digitavel:{resultado_boleto_digt}\nNosso Número:{resultado_nosso_num}')
    #return resultado_boleto_digt, resultado_nosso_num


#Chamada de função
extrai_valor_nota('pasta_arquivos/arquivo.pdf')
extrai_texto_boleto('teste.pdf')
