import facebook
import json
from datetime import date
from datetime import datetime
import filtro_das_chaves
from compactar_imagem import compactar_imagem
from tqdm import tqdm


data_hj = date.today()
hr = datetime.today()
img = 0
cronogama ={
    '0' : ['img01.png','img11.png','img20.png','img02.png'],
    '1' : ['img12.png','img21.png','img03.png','img13.png'],
    '2' : ['img22.png','img04.png','img14.png','img23.png'],
    '3' : ['img05.png','img15.png','img24.png','img06.png'],
    '4' : ['img16.png','img25.png','img07.png','img17.png'],
    '5' : ['img26.png','img08.png','img18.png','img27.png'],
    '6' : ['img09.png','img19.png','img28.png','img10.png']
}

if hr.hour in range(0,11):
    img = 0
elif hr.hour in range(11,15):
    img = 1
elif hr.hour in range(15,19):
    img = 2
else:
    img = 3

dia = cronogama.get(str(data_hj.weekday()))
dia_do_mes = str(data_hj.day)

LOCAL_RAIZ = '\\\\192.42.103.17\\propaganda\\publicador_facebook\\'
TOKENS_ARQUIVO = f'{LOCAL_RAIZ}tokens_lojas.json'


img_selc = f'{LOCAL_RAIZ}img\\{dia[img]}'
compactar_imagem(img_selc)

tokens = {}
postagens = {}



try:
    with open(TOKENS_ARQUIVO, 'r', encoding='utf8') as arquivo:
        tokens = json.load(arquivo)
    

except FileNotFoundError: 
    print('Tokens não encontrados')

for loja in tokens.keys():
 
    msg_txt = 'loja'+loja+'.txt'
    loja_msg = f'{LOCAL_RAIZ}msg\\{msg_txt}'
    
    try:
        with open(loja_msg, 'r', encoding='utf8') as arquivo:
            msg = arquivo.read()
        pag = facebook.GraphAPI(tokens.get(loja))
        id_postagem = pag.put_photo(image=open(img_selc, 'rb'), message=msg)
        dia_chave = dia_do_mes + dia[img]

        postagem_chave = {dia_chave: str(id_postagem.get('id'))}
                
        arquivo_select = loja + '.json'    
        postagem_loja = f'{LOCAL_RAIZ}postagens\\{arquivo_select}'

        try:
            with open(postagem_loja, 'r', encoding='utf8') as arquivo:
                loja_arquivo = json.load(arquivo)
        
            loja_arquivo.update(postagem_chave)
        
            with open(postagem_loja, 'w', encoding='utf8') as arquivo:
                json.dump(loja_arquivo, arquivo, indent=2, ensure_ascii=False)
                
            print(f'Postagem na Página {loja} foi efetuada com sucesso.')

        except FileNotFoundError:
            with open(postagem_loja, 'w', encoding='utf8') as arquivo:
                json.dump(postagem_chave, arquivo, indent=2, ensure_ascii=False)
                
        
            

    except facebook.GraphAPIError:
        with open(f'{LOCAL_RAIZ}erro_log.txt', 'a') as arquivo:
            arquivo.write(f'{hr} - {loja} Token Inválido\n')
        break

    except FileNotFoundError:
        with open(f'{LOCAL_RAIZ}erro_log.txt', 'a') as arquivo:
            arquivo.write(f'{hr} - {img_selc} não foi encontrada\n')
            
        break
    


    

    

    

    