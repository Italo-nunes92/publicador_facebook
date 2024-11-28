from .configuracoes import IMAGENS, hr, hora_atual
from PIL import Image

def compactar_imagem(img):
    imagem = Image.open(img)
    imagem_reduzida = imagem.resize((1000,1000))
    imagem_reduzida.save(img,dpi=(72,72))


def selecionar_imagem():
    cronogama =[
        ['img01.png','img11.png','img20.png','img02.png'],
        ['img12.png','img21.png','img03.png','img13.png'],
        ['img22.png','img04.png','img14.png','img23.png'],
        ['img05.png','img15.png','img24.png','img06.png'],
        ['img16.png','img25.png','img07.png','img17.png'],
        ['img26.png','img08.png','img18.png','img27.png'],
        ['img09.png','img19.png','img28.png','img10.png']
    ]

    if hora_atual in range(0,11):
        img = 0
    elif hora_atual in range(11,15):
        img = 1
    elif hora_atual in range(15,19):
        img = 2
    else:
        img = 3

    img = IMAGENS / (cronogama[hr.weekday()][img])
    
    compactar_imagem(img)
    
    return img