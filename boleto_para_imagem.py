#https://youtu.be/PyF1Vh9040Y
import pdf2image


def transform_img(nome_arquivo_pdf):
    texto = pdf2image.pdf2image.convert_from_path(nome_arquivo_pdf, poppler_path=r'poppler-25.07.0\Library\bin')

    for i, txt in enumerate(texto):
        if i == 0:
            txt.save('boleto_img.jpg')