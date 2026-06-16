import easyocr
import cv2
from matplotlib import pyplot as plt

#Bibliotecas necessárias:
#pip install torch torchvision torchaudio
#pip install matplotlib
#pip install easyocr

#Leitor de arquivos pdf
img = 'nota.pdf'

# Inicializa o leitor EasyOCR para português
reader = easyocr.Reader(['pt'])
result = reader.readtext(img)

# Carrega a imagem:
img = cv2.imread(img)

for detection in result:
    #Converte coordenadas para inteiros
    top_left = tuple(map(int, detection[0][0]))
    bottom_right = tuple(map(int, detection[0][2]))
    text =  detection[1]

    # Desenha o retângulo ao redor do texto detectado
    img = cv2.rectangle(img, top_left, bottom_right, (0, 225, 0), 3)

    # Adiciona o texto acima da caixa delimitadora
    img = cv2.putText(img, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 0), 2, cv2.LINE_AA)



# Converte a imagem para RGB para exibição no Matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off') # Desativa os eixos para uma visualização mais limpa
plt.show()
