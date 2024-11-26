from PIL import Image
from tqdm.notebook import tqdm
import time
import os

def compactar_imagem(img):
    imagem = Image.open(img)
    imagem_reduzida = imagem.resize((1000,1000))
    imagem_reduzida.save(img,dpi=(72,72))
lista = list(range(100))   

# bar = tqdm(total=len(lista),unit=' Página', ncols=100, colour='blue',nrows=5 )
for i in tqdm(lista):    
    print(i)
    time.sleep(1)
    
    
