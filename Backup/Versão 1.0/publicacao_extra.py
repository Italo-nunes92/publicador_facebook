import facebook
import json
from datetime import date
import filtro_das_chaves

LOCAL_RAIZ = '\\\\192.42.103.17\\propaganda\\publicador_facebook\\'
TOKENS_ARQUIVO = f'{LOCAL_RAIZ}tokens_lojas.json'

tokens = {}
postagens = {}
data_hj = date.today()
dia_do_mes = str(data_hj.day)

img_selc = f'{LOCAL_RAIZ}img_extra\\extra.png'
loja_msg = f'{LOCAL_RAIZ}img_extra\\msg.txt'

with open(loja_msg, 'r', encoding='utf8') as arquivo:
            msg = arquivo.read()

try:
    with open(TOKENS_ARQUIVO, 'r', encoding='utf8') as arquivo:
        tokens = json.load(arquivo)
    
except FileNotFoundError: 
    print('Tokens não encontrados')

for loja in tokens.keys():

    try:
        pag = facebook.GraphAPI(tokens.get(loja))
        id_postagem = pag.put_photo(image=open(img_selc, 'rb'), message=msg)
        dia_chave = dia_do_mes + 'extra'

        postagem_chave = {dia_chave: str(id_postagem.get('post_id'))}

        
        arquivo_select = loja + '.json'    
        postagem_loja = f'{LOCAL_RAIZ}postagens\\{arquivo_select}'
        
        print(f'Postagem na Página {loja} foi efetuada com sucesso.')

        try:
            with open(postagem_loja, 'r', encoding='utf8') as arquivo:
                loja_arquivo = json.load(arquivo)
        
            loja_arquivo.update(postagem_chave)
        
            with open(postagem_loja, 'w', encoding='utf8') as arquivo:
                json.dump(loja_arquivo, arquivo, indent=2, ensure_ascii=False)

        except FileNotFoundError:
            with open(postagem_loja, 'w', encoding='utf8') as arquivo:
                json.dump(postagem_chave, arquivo, indent=2, ensure_ascii=False)
            

    except facebook.GraphAPIError:
        with open(f'{LOCAL_RAIZ}erro_log.txt', 'a') as arquivo:
            arquivo.write(f'{loja} Token Inválido\n')
        break

    except FileNotFoundError:
        with open(f'{LOCAL_RAIZ}erro_log.txt', 'a') as arquivo:
            arquivo.write(f'{img_selc} não foi encontrada\n')
            
        break

    

    

    

    