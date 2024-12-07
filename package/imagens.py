from .configuracoes import IMAGENS, hr, hora_atual
from PIL import Image
import requests

def exibirPublicacao(pag, post_selecionado):
    try: 
        post = pag.get_object(id=post_selecionado, fields='full_picture')
        data = requests.get(post['full_picture']).content
        f = open('img.jpg','wb') 
        f.write(data) 
        f.close() 
        img = Image.open('img.jpg') 
        img.show()
        return False
    except:
        return True
        

def compactar_imagem(img):
    imagem = Image.open(img)
    imagem_reduzida = imagem.resize((1000,1000))
    imagem_reduzida.save(img,dpi=(72,72))


def selecionar_imagem():
    cronogama =[
        ['img01.jpg','img11.jpg','img20.jpg','img02.jpg'],
        ['img12.jpg','img21.jpg','img03.jpg','img13.jpg'],
        ['img22.jpg','img04.jpg','img14.jpg','img23.jpg'],
        ['img05.jpg','img15.jpg','img24.jpg','img06.jpg'],
        ['img16.jpg','img25.jpg','img07.jpg','img17.jpg'],
        ['img26.jpg','img08.jpg','img18.jpg','img27.jpg'],
        ['img09.jpg','img19.jpg','img28.jpg','img10.jpg']
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
    
    # Usar apenas em imagens PNG
    # compactar_imagem(img) 
    
    return img