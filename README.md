<h1 align="center"> Read PDF Repasse </h1>

<h4 align="center"> ⛔Projeto em desenvolvimento ⛔ </h4> 

<p>Sistema em Python para leitura e extração de informações de arquivos PDF, com foco em documentos de repasse financeiro como boletos e notas fiscais.
Ideal para automatizar tarefas repetitivas e organizar dados de forma etruturada.</p>

## 🚀 Funcionalidades:
- Leitura de arquivos PDF (Boleto e Nota Fiscal)
- Extração de valores e datas
- Exportação dos dados para sistema o sistema Protheus
- Interface simples via terminal

## 🛠 Tecnologias utilizadas:
- Python 3.13.7
- PyAutoGUI
- pdfplumber
- PyMuPDF
- pypdfium2
- pillow
- keyboard
- MouseInfo
- pyperclip
- PyGetWindow
- PyMsgBox
- Poppler

## ❕ Requisitos:
1. Ter o Python instalado
2. Instalar as dependências:
```bash
pip install -r requirements.txt
```
3. Baixar os binários do Poppler na pasta do projeto e configurar o caminho no código do arquivo **boleto_para_imagem.py**:
```bash
texto = pdf2image.pdf2image.convert_from_path(nome_arquivo_pdf, poppler_path=r'poppler-25.07.0\Library\bin')
```

4. Baixar e instalar o tesseract. No arquivo **teste_leitura_imagem.py**, ajustar o caminho da pasta:
```bash
    #caminho da biblioteca
    caminho = r"C:\Program Files\Tesseract-OCR"

    #executa o aplicativo tesseract.exe
    pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
```

## 📂 Estrutura do Projeto

```
SCRIPT DADOS REPASSE/
├── poppler-25.07.0/
├── boleto_para_imagem.py
├── leitura_file.py
├── main.py
├── nota.pdf
├── position_mouse.py
├── teste_leitura_imagem.py
├── requeriments.txt
├── .gitignore
└── README.md
```

## ▶ Como executar

Executar através do arquivo: **leitura_file.py**