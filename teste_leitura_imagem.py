import pytesseract
import cv2


def read_img(name_img):
    #ler a imagem
    imagem = cv2.imread(name_img)

    #caminho da biblioteca
    caminho = r"C:\Program Files\Tesseract-OCR"

    #executa o aplicativo tesseract.exe
    pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

    #pedir pro tesseract extrair o texto da imagem
    texto = pytesseract.image_to_string(imagem, lang="por")

    #print(texto)

    return texto