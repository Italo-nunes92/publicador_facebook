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
        