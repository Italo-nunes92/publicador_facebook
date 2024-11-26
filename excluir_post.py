import facebook
import json
from pathlib import Path
import filtro_das_chaves
from funcoes import exibirPublicacao
import os
from tqdm import tqdm
os.system('cls')

LOCAL = '\\\\192.42.103.17\\propaganda\\publicador_facebook\\'
TOKENS_ARQUIVO = f'{LOCAL}tokens_lojas.json'

try:
    with open(TOKENS_ARQUIVO, 'r', encoding='utf8') as arquivo:
        tokens = json.load(arquivo)
    
except FileNotFoundError: 
    print('Tokens não encontrados')


selecao = input('Digite a data+imagem+.png para exclusão: ')
primeiraVez = True

for loja in tqdm(tokens.keys()):

    arquivo_select = loja + '.json'    
    postagem_loja = f'{LOCAL}postagens\\{arquivo_select}'

    with open(postagem_loja, 'r', encoding='utf8') as arquivo:
            post = json.load(arquivo)

    pag = facebook.GraphAPI(tokens.get(loja))
    
    if primeiraVez == True:
        primeiraVez = exibirPublicacao(pag , post.get(selecao))
        if primeiraVez == False: 
            escolha = input('Deseja realmente excluir? [1]SIM ou [2]NÃO: ')
            if escolha == '2' : break         

    try:
        objeto_id = pag.get_object(id=post.get(selecao),fields='id')
        pag.delete_object(id=objeto_id['id'])
        print(f'Postagem da loja {loja} excluida com sucesso')
        
    except facebook.GraphAPIError:
        print('Publicação já foi excluida nessa página - '+ loja )
