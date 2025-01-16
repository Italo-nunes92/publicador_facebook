import facebook
import json
import os
from dotenv import load_dotenv
from .configuracoes import LOCAL_RAIZ, JSON, MENSAGENS, ERROS, getDataHora, getHoraAtual, getDiaMesAno

def erro_log(msg):
    with open((ERROS / 'erro_log.txt'), 'a',encoding='utf8') as arquivo:
            arquivo.write(f'{getDataHora()} : {msg}\n')
            
def conectar_token_pag(pag):
    graph = facebook.GraphAPI(access_token = pag)
    return graph
            
def conectar_token():
    load_dotenv()
    token = os.environ['token']
    graph = facebook.GraphAPI(access_token = token)
    return graph

def get_data():
    graph = conectar_token()
    token_pagina = graph.get_connections('me','accounts?limit=50')
    
    return token_pagina

def get_tokens():    
    token_pagina = get_data()
    with open((JSON / 'lojas_jmahfuz.json'), 'r') as arquivo:
        lojas_numeros = json.load(arquivo)
        
    lojas_ativas = {}
    for i in lojas_numeros.items():
        for loja in token_pagina.get('data'):
            if i[1][0] == loja.get('id'):
                lojas_ativas.update({i[0]:[loja.get('access_token'),loja.get('name')]})
    return lojas_ativas

def get_todas_paginas():
    token_pagina = get_data()
    paginas_jmahfuz = {}
    
    for i in token_pagina.get('data'):        
        pagina_jmahfuz = {i.get('name'):[i.get('id'),i.get('name')]}
        paginas_jmahfuz.update(pagina_jmahfuz)
    
    ordenado = sorted(paginas_jmahfuz.items())
    paginas_jmahfuz.clear()
    
    print('Digite "0" para remover a página da lista')
    for i in ordenado:        
        numero = input(f'{i[0]} = Nº: ')
        pagina_jmahfuz = {numero:i[1]}
        paginas_jmahfuz.update(pagina_jmahfuz)
        
    lista_completa = {}
    for i in sorted(paginas_jmahfuz.items()):
        lista = {i[0]:i[1]}
        lista_completa.update(lista)
        
    lista_completa.pop('0')
        
            
    with open((JSON / 'lojas_jmahfuz.json'), 'w', encoding='utf8') as arquivo:
                json.dump(lista_completa, arquivo, indent=2, ensure_ascii=False)
                

def publicar_post(loja, img_selc, token):
    
    loja_msg = MENSAGENS / f'loja{loja}.txt'
    try:
        with open(loja_msg, 'r', encoding='utf8') as arquivo:
            msg = arquivo.read()
    except:
        erro_msg = f'Mesagem da loja {loja} não foi encontrada'
        erro_log(erro_msg)        
        raise FileNotFoundError(erro_msg)
        
    try:
                
        pag = facebook.GraphAPI(token)
        id_postagem = pag.put_photo(image=open(img_selc, 'rb'), message=msg)
        dia_chave = f'{getDiaMesAno()}-{getHoraAtual()}'

        postagem_chave = {dia_chave: str(id_postagem.get('post_id'))}
        postagem_loja = LOCAL_RAIZ / 'postagens' / (loja + '.json' )

        try:
            with open(postagem_loja, 'r', encoding='utf8') as arquivo:
                loja_arquivo = json.load(arquivo)
        
            loja_arquivo.update(postagem_chave)
        
            with open(postagem_loja, 'w', encoding='utf8') as arquivo:
                json.dump(loja_arquivo, arquivo, indent=2, ensure_ascii=False)
                
        except FileNotFoundError:
            with open(postagem_loja, 'w', encoding='utf8') as arquivo:
                json.dump(postagem_chave, arquivo, indent=2, ensure_ascii=False)
                
        print(f'Postagem na Página {loja} foi efetuada com sucesso.')
        
    except facebook.GraphAPIError:
        erro_msg = f'{loja} Token Inválido'
        erro_log(erro_msg)      
        raise KeyError("Token Inválido")
        

    except FileNotFoundError:
        erro_msg = f'{img_selc} não foi encontrada'
        erro_log(erro_msg)
        raise FileNotFoundError('Imagem Inválida')
            
        
def excluir_publicacao(loja, token, selecao):
    
    post = abrir_postagens(loja)
    pag = facebook.GraphAPI(token)
    
    try:
        postagem_loja = LOCAL_RAIZ / 'postagens' / (loja + '.json' )
        objeto_id = pag.get_object(id=post.get(selecao),fields='id')
        pag.delete_object(id=objeto_id['id'])
        print(f'Postagem da loja {loja} excluida com sucesso')
        
        post.pop(selecao)
        
        with open(postagem_loja, 'w', encoding='utf8') as arquivo:
            json.dump(post, arquivo, indent=2, ensure_ascii=False)
        
    except facebook.GraphAPIError:
        print('Publicação já foi excluida nessa página - '+ loja )
        
def abrir_postagens(loja):
    postagem_loja = LOCAL_RAIZ / 'postagens' / (loja + '.json' )

    with open(postagem_loja, 'r', encoding='utf8') as arquivo:
            post = json.load(arquivo)
    return post
        