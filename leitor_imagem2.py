import easyocr
from pdf2image import convert_from_path
import numpy as np
import re

# Caminho do Poppler
path_to_poppler = r'C:\Users\giovanni.souza\Desktop\Projetos DEV\Script Dados Repasse\poppler-25.07.0\Library\bin'

def leitor_pdf_provisorio(nome_pdf):
    # 1. Converte o PDF (Apenas uma vez)
    paginas = convert_from_path(
        nome_pdf, 
        first_page=1, 
        last_page=1, 
        poppler_path=path_to_poppler
    )
    imagem_np = np.array(paginas[0])

    # 2. Inicializa o motor (O ideal é que isso fique FORA da função se for ler vários PDFs)
    reader = easyocr.Reader(['pt', 'en'], gpu=False)

    # 3. O EasyOCR processa a imagem (Este é o ponto que demora)
    print("Processando OCR...")
    resultado = reader.readtext(imagem_np)

    # 4. Transformamos o resultado em uma lista simples de strings
    linhas = [item[1] for item in resultado]
    print(linhas)
    # 5. Busca a linha digitável
    for i, linha in enumerate(linhas):
        if "Autenticação Mecânica" in linha:
            inicio = i + 6
            if inicio + 2 < len(linhas):
                # Pegamos as 3 partes e limpamos
                bruto = linhas[inicio] + linhas[inicio + 1] + linhas[inicio + 2]
                linha_digitavel = ''.join(re.findall(r'\d+', bruto))
                
                if len(linha_digitavel) >= 44:
                    print(f"Linha encontrada: {linha_digitavel}")
                    # O RETURN aqui encerra a função NA HORA. 
                    # Nada mais abaixo deste ponto será executado.
                    return linha_digitavel

    return "" # Retorna vazio se não encontrar nada após percorrer tudo

if __name__ == "_main_":
    # Chamada única
    resultado_final = leitor_pdf_provisorio('boleto.pdf')
    print(f"O programa terminou com: {resultado_final}")